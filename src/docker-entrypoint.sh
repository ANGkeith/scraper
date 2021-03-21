#!/bin/sh
set -o pipefail
set -o nounset
set -o errexit

mkdir -p "$HOME/.config"
cat << EOF > $HOME/.config/telegram-send.conf
[telegram]
token = $TELEGRAM_TOKEN
chat_id = $CHAT_ID
EOF

python3 -u start.py &

# Use to prevent the script from exiting
tail -f /dev/null
