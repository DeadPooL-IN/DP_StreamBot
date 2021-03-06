# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π­ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

π‘ **Find out all the Bot's commands and how they work by clicking on the Β» π Commands button!**


π  [π³π΄π°π³πΏπΎπΎπ»](https://t.me/DeadPooL_IN) **if you have any problem contact**

β **To know how to use this bot, please click on the Β» β Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Add me to your Group β",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("β Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("π Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("β€ Owner", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "π₯ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "π£ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "π³π΄π°π³πΏπΎπΎπ»", url="https://t.me/DeadPooL_IN"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β **Basic Guide for using this bot:**

1.) **First, Add me to your Group.**
2.) **Then promote me as admin and give all permissions except anonymous admin.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video.**
5.) **All the command list you can see on Β» π Commands button, find it on start home, tap the Β» Go Back button below.**

π‘ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""π Here is the Commands list:

Β» /play - play music on voice chat
Β» /stream - enter the radio link
Β» /vplay - play video on video chat
Β» /vstream - for m3u8/live link
Β» /playlist - show you the playlist
Β» /video (query) - download video from youtube
Β» /song (query) - download song from youtube
Β» /lyric (query) - scrap the song lyric
Β» /search (query) - search a youtube video link
Β» /queue - show you the queue list (admin only)
Β» /pause - pause the stream (admin only)
Β» /resume - resume the stream (admin only)
Β» /skip - switch to next stream (admin only)
Β» /stop - stop the streaming (admin only)
Β» /userbotjoin - invite the userbot to join chat (admin only)
Β» /userbotleave - order userbot to leave from group (admin only)
Β» /reload - update the admin list (admin only)
Β» /rmw - clean raw files (sudo only)
Β» /rmd - clean downloaded files (sudo only)
Β» /leaveall - order userbot leave from all group (sudo only)

β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
