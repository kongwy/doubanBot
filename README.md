# doubanBot

(DEPRECATED) Simple Telegram inline bot for Douban Books & Movies.

:) Douban has closed their API service of personal use.

## Note

**This is an idiot newbie work.**

## Deploy

Library [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) is needed to run the bot:

    $ pip install python-telegram-bot

Replace the token in `bot.py` with yours:

    updater = Updater(token='REPLACE WITH YOUR TOKEN')

Run `bot.py`:

    $ py -3 bot.py
