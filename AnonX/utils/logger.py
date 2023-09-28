from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐂𝐇𝐀𝐓"
        logger_text = f""" ━━━━━━━━━━━━━━━━━━━━━━━     
**{MUSIC_BOT_NAME} 𝐏𝐋𝐀𝐘 𝐋𝐎𝐆𝐆𝐄𝐑**
┏━━━━━━━━━━━━━━━━━┓
 ༺★𝐂𝐇𝐀𝐓 𝐈𝐍𝐅𝐎★༻
┗━━━━━━━━━━━━━━━━━┛      
┣★**𝐂𝐇𝐀𝐓:** {message.chat.title} [`{message.chat.id}`]
┣★**𝐂𝐇𝐀𝐓 𝐋𝐈𝐍𝐊:** {chatusername}
┏━━━━━━━━━━━━━━━━━┓
  ༺★𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨★༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐔𝐒𝐄𝐑:** {message.from_user.mention}

┣★**𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄:** @{message.from_user.username}
┣★**𝐈𝐃:** `{message.from_user.id}`
┏━━━━━━━━━━━━━━━━━┓
  ༺★𝐏𝐋𝐀𝐘 𝐈𝐍𝐅𝐎★༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐒𝐄𝐀𝐑𝐂𝐇 𝐒𝐎𝐍𝐆:** {message.text}

┣★**𝐒𝐓𝐑𝐄𝐀𝐌 𝐓𝐘𝐏𝐄:** {streamtype}
━━━━━━━━━━━━━━━━━━━━━━━"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
