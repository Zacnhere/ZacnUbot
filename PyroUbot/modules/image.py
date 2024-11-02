import asyncio
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *

__MODULE__ = "image"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ɪᴍᴀɢᴇ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}wall</code> 
    <i>mendapatkan gambar anime secara acak</i> 

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}waifu</code>
    <i>mendapatkan gambar waifu anime</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}rbg</code>
    <i>menghapus latar belakang gambar</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}blur</code>
    <i>memberikan efek blur ke gambar</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}miror</code>
    <i>memberikan efek cermin ke gambar</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}negative</code>
    <i>memberikan efek negaticv ke gambar</i>
    </blockquote>

"""



async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": RMBG_API,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )


@PY.UBOT("rbg")
async def _(client, message):
    if RMBG_API is None:
        return
    if message.reply_to_message:
        reply_message = message.reply_to_message
        xx = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
        try:
            if (
                isinstance(reply_message.media, raw.types.MessageMediaPhoto)
                or reply_message.media
            ):
                downloaded_file_name = await client.download_media(
                    reply_message, "./downloads/"
                )
                await xx.edit("<b><emoji id=4963233485356533176>👤</emoji>ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ᴅᴀʀɪ ɢᴀᴍʙᴀʀ ɪɴɪ...</b>")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await xx.edit("<b><emoji id=4963233485356533176>👤</emoji>ʙᴀɢᴀɪᴍᴀɴᴀ ᴄᴀʀᴀ ᴍᴇɴɢʜᴀᴘᴜs ʟᴀᴛᴀʀ ʙᴇʟᴀᴋᴀɴɢ ɪɴɪ ?</b>")
        except Exception as e:
            await xx.edit(f"{(str(e))}")
            return
        contentType = output_file_name.headers.get("content-type")
        if "image" in contentType:
            with io.BytesIO(output_file_name.content) as remove_bg_image:
                remove_bg_image.name = "rbg.png"
                await client.send_document(
                    message.chat.id,
                    document=remove_bg_image,
                    force_document=True,
                    reply_to_message_id=message.id,
                )
                await xx.delete()
        else:
            await xx.edit(
                "<b><emoji id=6161479118413106534>❌</emoji>ᴋᴇsᴀʟᴀʜᴀɴ (ᴋᴜɴᴄɪ ᴀᴘɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ, sᴀʏᴀ ᴋɪʀᴀ ?)</b>\n<i>{}</i>".format(
                    output_file_name.content.decode("UTF-8")
                ),
            )
    else:
        return await message.reply("<b><emoji id=6161479118413106534>❌</emoji>sɪʟᴀʜᴋᴀɴ ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ</b>")


@PY.UBOT("blur")
async def _(client, message):
    ureply = message.reply_to_message
    xd = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if not ureply:
        return await xd.edit("<b><emoji id=6161479118413106534>❌</emoji>ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ</b>")
    yinsxd = await client.download_media(ureply, "./downloads/")
    if yinsxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", yinsxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(yinsxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yin = cv2.imread(file)
    ayiinxd = cv2.GaussianBlur(yin, (35, 35), 0)
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await xd.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(yinsxd)


@PY.UBOT("negative")
async def _(client, message):
    ureply = message.reply_to_message
    ayiin = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if not ureply:
        return await ayiin.edit("<b><emoji id=6161479118413106534>❌</emoji>ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ</b>")
    ayiinxd = await client.download_media(ureply, "./downloads/")
    if ayiinxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", ayiinxd, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(ayiinxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yinsex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(yinsex)
    cv2.imwrite("yin.jpg", kntlxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await ayiin.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(ayiinxd)


@PY.UBOT("miror")
async def _(client, message):
    ureply = message.reply_to_message
    kentu = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇᴍᴘʀᴏsᴇs</b>")
    if not ureply:
        return await kentu.edit("<b><emoji id=6161479118413106534>❌</emoji>ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ</b>")
    xnxx = await client.download_media(ureply, "./downloads/")
    if xnxx.endswith(".tgs"):
        cmd = ["lottie_convert.py", xnxx, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("yin.png", tol)
        file = "yin.png"
    yin = cv2.imread(file)
    mmk = cv2.flip(yin, 1)
    ayiinxd = cv2.hconcat([yin, mmk])
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await kentu.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(xnxx)


@PY.UBOT("wall|waifu")
async def _(client, message):
    msg = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>", quote=True)
    if message.command[0] == "wall":
        photo = await API.wall(client)
        try:
            await photo.copy(message.chat.id, reply_to_message_id=message.id)
            return await msg.delete()
        except Exception as error:
            return await msg.edit(error)
    elif message.command[0] == "waifu":
        photo = API.waifu()
        try:
            await message.reply_photo(photo, quote=True)
            return await msg.delete()
        except Exception as error:
            return await msg.edit(error)
