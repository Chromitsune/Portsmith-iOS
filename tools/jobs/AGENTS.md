# Background job helpers

`bg.sh`/`notify.sh` manage host-side long commands with `tmux`, append logs under ignored `logs/`, and send best-effort notifications. They do not make the wrapped command safe: review the command before launch. Do not put device write/reset operations in unattended jobs without current explicit authorization. Keep the MIT adaptation attribution in the script headers and `CREDITS.md`.
