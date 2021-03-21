import re
import telegram_send

def is_after_work(element):
    return "07:30 PM" in element.text

def has_available_spot(element):
    return int(re.search('.*Asia/Singapore \((\d+)/.*\)', element.text).group(1)) > 0

def retry_until_success(callback):
    status = False
    while not status:
        try:
            callback()
            status = True
        except Exception as e:
            continue

def send_message(message: str) -> None:
    telegram_send.send(messages=[f"{message}"])