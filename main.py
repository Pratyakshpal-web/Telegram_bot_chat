import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load credentials 
load_dotenv()

TOKEN = os.getenv('telegram_token')
CHAT_ID = os.getenv('telegram_chat_id')

if not TOKEN or not CHAT_ID:
    raise SystemExit("telegram_token or telegram_chat_id missing in .env")


def send_telegram_message(message_body):
    """Send a text message to your Telegram chat through the bot."""
    try:
        r = requests.post(
            f'https://api.telegram.org/bot{TOKEN}/sendMessage',
            data={'chat_id': CHAT_ID, 'text': message_body},
            timeout=15
        )
        data = r.json()
        if data.get('ok'):
            print('Message sent successfully!')
        else:
            print(f'Telegram error: {data}')
    except Exception as e:
        print(f'An error occurred: {e}')


# User input
name = input('Enter the recipient name: ')
message_body = input(f'Enter the message to send to {name}: ')
date_str = input('Enter date (YYYY-MM-DD): ')
time_str = input('Enter time (HH:MM, 24-hour): ')

# Parse the date and time
try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
except ValueError:
    raise SystemExit('Invalid date/time format. Use YYYY-MM-DD and HH:MM.')

# Calculate how long to wait
delay_seconds = (schedule_datetime - datetime.now()).total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
    print('Keep this window open until the message is sent...')
    time.sleep(delay_seconds)
    send_telegram_message(f'Hi {name}, {message_body}')