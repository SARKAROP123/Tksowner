from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝑨∂∂ 𝐌є 𝒀συя 𝑮яσυρ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✰𝑯єℓρ✰",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺єттιиgѕ", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝑨∂∂ 𝐌є 𝒀συя 𝑮яσυρ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="★𝑯єℓρ★", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ 𝐆яσυρ ❣", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🍷 𝑶ωиєя 🍷", user_id=OWNER 
            )
        ],
        [
            InlineKeyboardButton(
                text="✪𝑺туℓє✰𝑵αмє✪", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons
