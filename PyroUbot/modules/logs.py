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
    url = wget.download("https://telegra.ph//file/18143a0381f7084e76389.mp4")
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

from pyrogram import Client, filters
import os


@PY.on_message(filters.media)
async def media_logger(client, message):
    aktif = await get_vars(client.me.id, "ON_LOGS")
    logs_id = await get_vars(client.me.id, "ID_LOGS")

    # Tidak melakukan apapun jika log tidak aktif atau belum di-set
    if not aktif or not logs_id:
        return

    try:
        # Info pengirim
        pengirim = "Tidak diketahui"
        if message.from_user:
            pengirim = f"{message.from_user.first_name} (ID: {message.from_user.id})"
        elif message.sender_chat:
            pengirim = f"{message.sender_chat.title} (ID: {message.sender_chat.id})"

        # Info asal chat
        asal = f"{message.chat.title} (ID: {message.chat.id})" if message.chat.title else f"Private Chat (ID: {message.chat.id})"

        # Caption asli + info tambahan
        original_caption = message.caption or ""
        caption = f"{original_caption}\n\n📥 Dari: {asal}\n👤 Pengirim: {pengirim}"

        # Download media
        file = await client.download_media(message)

        # Kirim ulang media ke channel log
        if message.photo:
            await client.send_photo(logs_id, file, caption=caption)
        elif message.video:
            await client.send_video(logs_id, file, caption=caption)
        elif message.audio:
            await client.send_audio(logs_id, file, caption=caption)
        elif message.voice:
            await client.send_voice(logs_id, file, caption=caption)
        else:
            await client.send_document(logs_id, file, caption=caption)

        os.remove(file)

    except Exception as e:
        print(f"[LOG ERROR] {e}")
      
