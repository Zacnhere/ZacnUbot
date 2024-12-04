import requests
from pyrogram import filters
from PyroUbot import *
from pyrogram.errors.exceptions.bad_request_400 import MediaInvalid
from pyrogram.types import Message, InputMediaPhoto
import wget
import os
import glob

__MODULE__ = "Pinterest"
__HELP__ = """
<b>『 ᴘɪɴᴛᴇʀᴇsᴛ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pint</code> <b>ᴊᴜᴍʟᴀʜ/ᴋᴀᴛᴀ_ᴋᴜɴᴄɪ</b> 
   <i>penjelasan:</b> untuk mendownload media di pinterest</i>
"""

@PY.UBOT("pint")
async def pinterest(client, message):
    chat_id = message.chat.id

    if len(message.command) < 3:
        return await message.reply("<emoji id=6161479118413106534>❌</emoji>ɢᴜɴᴀᴋᴀɴ .pint ᴊᴜᴍʟᴀʜ ᴋᴀᴛᴀ_ᴋᴜɴᴄɪ")

    msg = await message.reply("<b><emoji id=6226405134004389590>🔍</emoji>sᴇᴅᴀɴɢ ᴍᴇɴᴄᴀʀɪ...</b>")

    try:
        jumlah = int(message.command[1])
        query = ' '.join(message.command[2:])
    except (IndexError, ValueError):
        return await msg.edit("<emoji id=5019523782004441717>❌</emoji> sᴀʟɪɴ ᴜʀʟ ᴅᴀʀɪ ᴘɪɴᴛᴇʀᴇsᴛ ᴅᴀɴ ᴋᴇᴛɪᴋ .pint ᴊᴜᴍʟᴀʜ ᴋᴀᴛᴀ_ᴋᴜɴᴄɪ 🔍")

    try:
        response = requests.get(f"https://pinterest-api-one.vercel.app/?q={query}")
        response.raise_for_status()
    except requests.RequestException as e:
        return await msg.edit(f"ɢᴀɢᴀʟ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ ᴅᴀʀɪ ᴀᴘɪ: {e}")

    images = response.json().get("images", [])
    if not images:
        return await msg.edit("ᴛɪᴅᴀᴋ ᴀᴅᴀ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")

    media_group = []
    for url in images[:jumlah]:
        try:
            image_response = requests.get(url, stream=True)
            if image_response.status_code == 200:
                potonya = wget.download(url)
                media_group.append(InputMediaPhoto(media=potonya))
            else:
                await message.reply(f"ᴜʀʟ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪᴊᴀɴɢᴋᴀᴜ: {url}")
        except requests.RequestException as e:
            await msg.edit(f"Gagal mengakses URL: {url} - Error: {e}")

    if media_group:
        try:
            await client.send_media_group(chat_id, media_group)
        except MediaInvalid:
            for meki in images[:jumlah]:
                try:
                    await client.send_photo(chat_id, meki)
                except:
                    pass
        except Exception as e:
            await msg.edit(f"Gagal mengirim media: {e}")
    else:
        await msg.edit("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴍᴇᴅɪᴀ ʏᴀɴɢ ᴠᴀʟɪᴅ ᴜɴᴛᴜᴋ ᴅɪᴋɪʀɪᴍ.")

    await msg.delete()
    try:
        os.system("rm -rf *.jpg")
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")
