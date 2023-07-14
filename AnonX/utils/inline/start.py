from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝑨𝑫𝑫 𝒀𝑶𝑼𝑹 𝑮𝑹𝑶𝑼𝑷➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝑬𝑳𝑷",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺𝑬𝑻𝑻𝑰𝑵𝑮𝑺", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝑨𝑫𝑫 𝒀𝑶𝑼𝑹 𝑮𝑹𝑶𝑼𝑷➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝑬𝑳𝑷", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ 𝑱𝑶𝑰𝑵 ❣", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🍷 𝑶𝑾𝑵𝑬𝑹 🍷", user_id=OWNER 
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱 𝑼𝑷𝑫𝑨𝑻𝑬 🌱", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons
