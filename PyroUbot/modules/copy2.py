import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot import *


@PY.UBOT("copypv")
async def copy_private_channel(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        await message.reply_text("❌ Balas pesan yang berisi link channel private.")
        return

    link = reply.text.strip()
    if not link.startswith("https://t.me/c/"):
        await message.reply_text("❌ Link tidak valid. Pastikan itu adalah link dari channel private.")
        return

    try:
        chat_id = int("-100" + link.split("/")[-2])
        msg_id = int(link.split("/")[-1]) 

        get = await client.get_messages(chat_id, msg_id)

        if not get.media:
            await message.reply_text("⚠️ Tidak ada media dalam pesan ini.")
            return

        media = await client.download_media(get)

        await client.send_video(
            message.chat.id, 
            video=media,
            caption="✅ Media berhasil disalin dari channel private."
        )

    
    except Exception as e:
        await message.reply_text(f"❌ Gagal mengambil media{(e)}")
