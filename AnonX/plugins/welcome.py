import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonX import app  

photo = [
    "https://telegra.ph//file/e93568652d5e3f0049426.jpg",
    "https://telegra.ph//file/2824cacb65731a51e003e.jpg",
    "https://telegra.ph//file/dcff35cb85a452dfe44a5.jpg",
    "https://telegra.ph//file/424b9606c0add3ece482e.jpg",
    "https://telegra.ph//file/68cff20efea5bc8ae4507.jpg",
    "https://telegra.ph//file/68cff20efea5bc8ae4507.jpg",
    "https://telegra.ph//file/68cff20efea5bc8ae4507.jpg",
    "https://telegra.ph/file/471339bb1901a007c0c2f.jpg",
    "https://telegra.ph/file/ab7d958d707ef649bc3c3.jpg",
    "https://telegra.ph/file/4f877f2843f31fcc32242.jpg",
    "https://telegra.ph/file/ecefaa3e00fb911826673.jpg",
    "https://telegra.ph/file/2a10683a2166f7cf4940b.jpg",
    "https://telegra.ph/file/cda35ca740e1229626e48.jpg",
    "https://telegra.ph/file/9f7186cd3d87199426e03.jpg",
    "https://telegra.ph/file/7fe39f1baa1a93b9a3f0e.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**💥𝐇𝐄𝐘 {message.from_user.mention} 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 𝐁𝐀𝐁𝐘💥**\n\n"
                f"**💥𝐂𝐇𝐀𝐓 𝐍𝐀𝐌𝐄:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐂𝐇𝐀𝐓 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**📍𝐔𝐒𝐄𝐑 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🥵𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐌𝐄𝐌𝐁𝐄𝐑🕊️ {count} 𝐌𝐄𝐌𝐁𝐄𝐑 𝐀𝐋𝐋**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"➕𝐀𝐃𝐃 𝐌𝐄 𝐁𝐀𝐁𝐘➕", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
