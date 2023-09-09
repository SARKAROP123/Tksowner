from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/153d1b0c97111b767fd2a.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐃ɱ❤️𝐎ɯɳҽɾ𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥︻┻┳═सरकार🔥", url=f"https://t.me/ll_SARKAR_BABE_ll")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/153d1b0c97111b767fd2a.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐃ɱ❤️𝐎ɯɳҽ𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥︻┻┳═सरकार🔥", url=f"https://t.me/ll_SARKAR_BABE_ll")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("group")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a3d20f525637eed3cc092.jpg",
        caption=f"""🍁𝐂ʅυƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσɾ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"https://t.me/TKS_JOIN")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("group")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a3d20f525637eed3cc092.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"https://t.me/TKS_JOIN")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("group")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a3d20f525637eed3cc092.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσɾ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"https://t.me/TKS_JOIN")
                ]
            ]
        ),
    )

