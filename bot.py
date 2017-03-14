import fetch
import logging
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

updater = Updater(token='REPLACE WITH YOUR TOKEN')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='这是一个 inline bot，请在输入框内调用。')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def inline(bot, update):
    query = update.inline_query.query
    results = list()
    if not query:
        for movie in fetch.inTheater():
            results.append(
                InlineQueryResultArticle(
                    id=movie['id'],
                    title=movie['title'],
                    input_message_content=InputTextMessageContent(
                        message_text='[' + movie['title'] + '](' + movie['alt'] + ')',
                        parse_mode='Markdown'
                    ),
                    thumb_url=movie['images']['large']
                )
            )
    else:
        books = fetch.getBook(query)
        movies = fetch.getMovie(query)
        for movie in movies:
            results.append(
                InlineQueryResultArticle(
                    id=movie['id'],
                    title=movie['title'],
                    input_message_content=InputTextMessageContent(
                        message_text='[' + movie['title'] + '](' + movie['alt'] + ')',
                        parse_mode='Markdown'
                    ),
                    thumb_url=movie['images']['large']
                )
            )
        for book in books:
            results.append(
                InlineQueryResultArticle(
                    id=book['id'],
                    title=book['title'],
                    input_message_content=InputTextMessageContent(
                        message_text='[' + book['title'] + '](' + book['alt'] + ')',
                        parse_mode='Markdown'
                    ),
                    thumb_url=book['images']['large']
                )
            )
    bot.answerInlineQuery(update.inline_query.id, results)


inlineWork_handler = InlineQueryHandler(inline)
dispatcher.add_handler(inlineWork_handler)

updater.start_polling()
