from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑭𝒆𝒂𝒕𝒖𝒓𝒆𝒔 ⚙",
                callback_data="settings_back_helper",
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝑨𝒅𝒅 𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌 𝑭𝒆𝒂𝒕𝒖𝒓𝒆𝒔 ⚙", callback_data="settings_back_helper"
            )
            InlineKeyboardButton(
                text="𝑾𝒚𝒏𝒌",
                url=f"https://wynk.in/music",
            )
        ],
     ]
    return buttons
