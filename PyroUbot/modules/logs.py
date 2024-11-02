import wget

from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent)

from PyroUbot import *


__MODULE__ = "logs"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ʟᴏɢs 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}logs</code> [on/off]
    <i>mengaktifkan atau menonaktifkan logs</i>
    </blockquote>
"""


async def send_log(client, chat_id, message, message_text, msg):
    try:
        await client.send_message(chat_id, message_text, disable_web_page_preview=True)
        await message.forward(chat_id)
    except Exception as error:
        print(f"{msg} ERROR: GAGAL MENERUSKAN PESAN")


@PY.NO_CMD_UBOT("LOGS_PRIVATE", ubot)
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ᴘʀɪᴠᴀᴛᴇ"
        user_link = f"{message.from_user.first_name} {message.from_user.last_name or ''}"
        message_link = (
            f"tg://openmessage?user_id={message.from_user.id}&message_id={message.id}"
        )
        link = f"[ᴋʟɪᴋ ᴅɪsɪɴɪ]({message_link})"
        message_text = f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>

  <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> {type}
  <b>•> ʟɪɴᴋ ᴘᴇsᴀɴ:</b> {link}
    
<b>⤵️ ᴘеsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ:</b> {user_link}
"""
        await send_log(client, int(logs), message, message_text, "LOGS_PRIVATE")


@PY.NO_CMD_UBOT("LOGS_GROUP", ubot)
async def _(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")

    if logs and on_logs:
        type = "ɢʀᴏᴜᴘ"
        user_link = f"{message.from_user.first_name} {message.from_user.last_name or ''}"
        message_link = message.link
        link = f"[ᴋʟɪᴋ ᴅɪsɪɴɪ]({message_link})"
        message_text = f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>

  <b>•> ᴛɪᴘᴇ ᴘᴇsᴀɴ:</b> {type}
  <b>•> ʟɪɴᴋ ᴘᴇsᴀɴ:</b> {link}
    
<b>⤵️ ᴘеsᴀɴ ᴛᴇʀᴜsᴀɴ ᴅᴀʀɪ:</b> {user_link}
"""
        await send_log(client, int(logs), message, message_text, "LOGS_GROUP")


@PY.UBOT("logs")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

  
    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴏɴ/ᴏғғ]</b>"
        )

    query = {"on": True, "off": False, "none": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply(f"<b>{ggl}ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ!!</b>")

    value = query[command]

    vars = await get_vars(client.me.id, "ID_LOGS")

    if not vars:
        logs = await create_logs(client)
        await set_vars(client.me.id, "ID_LOGS", logs)

    if command == "none" and vars:
        try:
            await client.delete_channel(vars)
        except Exception:
            pass
        await set_vars(client.me.id, "ID_LOGS", value)

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(
        f"<b>{brhsl}LOGS ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ:</b> {value}"
    )


async def create_logs(client):
    logs = await client.create_channel(f"Logs Ubot: {bot.me.username}")
    url = wget.download("https://files.catbox.moe/oo62ji.jpg")
    photo_video = {"video": url} if url.endswith(".mp4") else {"photo": url}
    await client.set_chat_photo(
        logs.id,
        **photo_video,
    )
    await client.send_message(
        logs.id, "<b>ʟᴏɢs ʙᴇʀʜᴀsɪʟ ᴅɪʙᴜᴀᴛ\nᴊᴀɴɢᴀɴ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ɪɴɪ ʏᴀ"
    )
    os.remove(url)
    return logs.id


