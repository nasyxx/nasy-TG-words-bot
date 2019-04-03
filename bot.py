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
from jieba import lcut as jc
from jieba import initialize
from pkuseg import pkuseg
from thulac import thulac
from telegram import InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import Updater, CallbackContext, InlineQueryHandler
from telegram.update import Update

from config import BOT_TOKEN

initialize()

tc = thulac(seg_only=True).cut  # pylint: disable=C0103
pc = pkuseg().cut  # pylint: disable=C0103


def words(update: Update, context: CallbackContext) -> None:
    """Words the inline message."""
    query = update.inline_query.query

    resj = " ".join(jc(query, cut_all=False))
    rest = tc(query, text=True)
    resp = " ".join(pc(query))

    print("--" * 10)
    print(query, end="\n")
    print("-" * 10)
    print("jieba: " + resj, "thulac: " + rest, "pkuseg: " + resp, sep="\n")
    print("--" * 10, end="\n\n")

    context.bot.answer_inline_query(
        update.inline_query.id,
        [
            InlineQueryResultArticle(
                id=query[:5] + "|j",
                title="jieba",
                description=resj,
                input_message_content=InputTextMessageContent(resj),
            ),
            InlineQueryResultArticle(
                id=query[:5] + "|t",
                title="thulac",
                description=rest,
                input_message_content=InputTextMessageContent(rest),
            ),
            InlineQueryResultArticle(
                id=query[:5] + "|p",
                title="pkuseg",
                description=resp,
                input_message_content=InputTextMessageContent(resp),
            ),
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
