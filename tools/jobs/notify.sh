#!/bin/sh
# Adapted from akshaynexus/iOSPlus10 (MIT); see UPSTREAM-LICENSE and CREDITS.md.
# Desktop notification (macOS: terminal-notifier or osascript; Linux: notify-send). Never fails.
#   tools/jobs/notify.sh "message" [title]
msg=${1:-done}; title=${2:-Portsmith}
if command -v terminal-notifier >/dev/null 2>&1; then
  terminal-notifier -title "$title" -message "$msg" -group portsmith >/dev/null 2>&1 || true
elif [ "$(uname -s)" = Darwin ]; then
  osascript -e "display notification \"$msg\" with title \"$title\"" >/dev/null 2>&1 || true
elif command -v notify-send >/dev/null 2>&1; then
  notify-send "$title" "$msg" || true
fi
exit 0
