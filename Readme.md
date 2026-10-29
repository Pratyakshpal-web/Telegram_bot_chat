# Telegram Message Scheduler

A simple Python automation tool that schedules a message and sends it to your Telegram chat at a time you choose, using the Telegram Bot API.

## Features

- Schedule a message for any future date and time
- Sends through a Telegram bot (free, no templates or approval needed)
- Keeps secrets (bot token, chat ID) in a `.env` file, not in the code
- Input validation for date/time format and past times
- Error handling for failed requests

## Requirements

- Python 3.8 or higher
- A Telegram account
- Packages: `requests`, `python-dotenv`

## Setup

### 1. Install the packages

```
pip install requests python-dotenv
```

### 2. Create your Telegram bot

1. Open Telegram and search for **@BotFather**.
2. Send `/newbot` and follow the steps (choose a name and a username ending in `bot`).
3. Copy the **bot token** that BotFather gives you.
4. Search for your new bot, open it, press **Start**, and send it any message.

### 3. Get your chat ID

1. In Telegram, search for **@userinfobot** and press **Start**.
2. Copy the **Id** number it replies with.

### 4. Create a `.env` file

In the same folder as the script, create a file named `.env`:

```
telegram_token=YOUR_BOT_TOKEN_HERE
telegram_chat_id=YOUR_CHAT_ID_HERE
```

No spaces and no quotes around the values.

## Usage

```
python main.py
```

You will be asked for:

| Prompt | Example |
|---|---|
| Recipient name | `Pratyaksh` |
| Message | `Time to study!` |
| Date (YYYY-MM-DD) | `2026-10-30` |
| Time (HH:MM, 24-hour) | `18:30` |

Keep the terminal window open until the scheduled time. The script waits, then sends the message and prints `Message sent successfully!`.

### Time format note

Time uses the 24-hour clock: `00:45` is 12:45 AM, `12:45` is 12:45 PM, and `21:30` is 9:30 PM.

## How it works

1. Loads the bot token and chat ID from `.env`.
2. Reads the name, message, date and time from the user.
3. Calculates the number of seconds until the scheduled time.
4. Waits with `time.sleep()`.
5. Sends the message through the Telegram `sendMessage` API endpoint.

## Project structure

```
automation/
├── main.py       # the scheduler script
├── .env          # your secrets (never commit this)
├── .gitignore    # should contain: .env
└── README.md
```

## Security

- Never share your bot token or commit `.env` to GitHub.
- Add this line to a `.gitignore` file:

```
.env
```

- If your token leaks, open **@BotFather**, send `/revoke`, and generate a new one.

## Limitations

- The script must keep running until the message is sent, so the terminal can't be closed and the computer can't sleep.
- It sends one message per run.
- Messages go to the chat ID in `.env` only.

## Future improvements

- Support multiple reminders stored in a file or database
- Run in the background with APScheduler or on a free hosting service
- Let users schedule reminders by messaging the bot directly

## Tech used

Python, Telegram Bot API, `requests`, `python-dotenv`