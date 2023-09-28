from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝗔∂∂ 𝗠є 𝗬συя 𝗚яσυρ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✰𝗛𝗘𝗟𝗣✰",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="★𝗦𝗘𝗧𝗧𝗜𝗡𝗚★", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕𝗔∂∂ 𝗠є 𝗬συя 𝗚яσυρ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="★𝗛𝗘𝗟𝗣★", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="★𝗦𝗨𝗣𝗣𝗢𝗥𝗧★", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="★𝗢𝗪𝗡𝗘𝗥★", user_id=OWNER 
            )
        ],
        [
            InlineKeyboardButton(
                text="★𝗨𝗣𝗗𝗔𝗧𝗘★", url=config.SUPPORT_GROUP
            )
        ],
     ]
    return buttons
