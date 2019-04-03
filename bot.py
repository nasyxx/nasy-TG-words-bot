#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Apr  3, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : bot.py
project  : words_bot
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Other Packages
from jieba import lcut as lc
from jieba import initialize
from telegram import InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import Updater, CallbackContext, InlineQueryHandler
from telegram.update import Update

from config import BOT_TOKEN

initialize()


def words(update: Update, context: CallbackContext) -> None:
    """Words the inline message."""
    query = update.inline_query.query
    res = " ".join(lc(query, cut_all=False))
    print(query)
    print(res, end="\n\n")
    context.bot.answer_inline_query(
        update.inline_query.id,
        [
            InlineQueryResultArticle(
                id=query[:5],
                title="Words",
                input_message_content=InputTextMessageContent(res),
            )
        ],
    )


def main() -> None:
    """Main function."""
    bot = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = bot.dispatcher
    dispatcher.add_handler(InlineQueryHandler(words))

    bot.start_polling()


if __name__ == "__main__":
    main()
