from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from engine import MenuController, load_profile  # noqa: E402
from preview import render_svg  # noqa: E402


class MenuEngineTests(unittest.TestCase):
    def setUp(self):
        self.profile = load_profile(ROOT / "profiles/portable-example.json")

    def test_loads_profiles_and_safe_options(self):
        self.assertEqual(self.profile.look["look_id"], "icon-stack")
        self.assertEqual(self.profile.options["options_id"], "safe-defaults")
        self.assertFalse(self.profile.options["auto_boot"])
        self.assertFalse(self.profile.options["persist_selection"])

    def test_default_focus_does_not_execute_target(self):
        ctl = MenuController(self.profile)
        self.assertEqual(ctl.selected.id, "system-a")
        self.assertIsNone(ctl.handle("down"))
        self.assertEqual(ctl.selected.id, "system-b")
        self.assertEqual(ctl.handle("select"), "opaque:system-b")

    def test_disabled_entries_are_skipped_and_cannot_start(self):
        ctl = MenuController(self.profile, "system-b")
        self.assertEqual(ctl.move(1).id, "system-a")
        self.assertEqual(ctl.move(-1).id, "system-b")
        with self.assertRaises(ValueError):
            MenuController(self.profile, "recovery")

    def test_unknown_event_is_rejected(self):
        ctl = MenuController(self.profile)
        with self.assertRaises(ValueError):
            ctl.handle("flash")

    def test_renderer_uses_responsive_canvas_and_no_upstream_art(self):
        ctl = MenuController(self.profile)
        svg = render_svg(self.profile, ctl, 1280, 800)
        self.assertIn('viewBox="0 0 1280 800"', svg)
        self.assertIn("System A", svg)
        self.assertIn("no boot action is executed", svg)
        self.assertNotIn("github.com", svg)

    def test_profile_rejects_command_target(self):
        source = json.loads((ROOT / "profiles/portable-example.json").read_text())
        source["entries"][0]["target_id"] = "fastboot flash boot"
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "bad.json"
            tmp.write_text(json.dumps(source))
            with self.assertRaises(ValueError):
                load_profile(tmp)


if __name__ == "__main__":
    unittest.main()
