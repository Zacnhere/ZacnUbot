import math
import wget
import os
import asyncio
import yt_dlp
from random import randint

from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel, InputPeerChat
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch

from datetime import timedelta
from time import time

from PyroUbot import *



def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "KB", 2: "MB", 3: "GB", 4: "TB"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return f"{str(round(size, 2))} {dict_power_n[raised_to_pow]}"

def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        (f"{str(days)} hari, " if days else "")
        + (f"{str(hours)} jam, " if hours else "")
        + (f"{str(minutes)} menit, " if minutes else "")
        + (f"{str(seconds)} detik, " if seconds else "")
    )
    return tmp.strip(", ")

async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff if diff != 0 else 0
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000 if speed != 0 else 0
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("█" for _ in range(math.floor(percentage / 10))),
            "".join("░" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nEstimasi: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            text = f"{type_of_ps}\nFile: {file_name}\n{tmp}"
        else:
            text = f"{type_of_ps}\n{tmp}"

        try:
            await message.edit(text)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except MessageNotModified:
            pass


async def search_youtube(query):
    ydl_opts = {
        "quiet": True,
        "default_search": "ytsearch1",
        "extract_flat": True,
        "force_generic_extractor": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if "entries" in info and len(info["entries"]) > 0:
            video = info["entries"][0]
            return {"title": video["title"], "id": video["id"], "url": f"https://youtu.be/{video['id']}"}
    return None

async def vsong_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Masukkan judul video dengan benar.")

    infomsg = await message.reply_text("🔍 Mencari...", quote=False)

    search = await search_youtube(message.text.split(None, 1)[1])
    if not search:
        return await infomsg.edit("❌ Pencarian gagal.")

    link = search["url"]
        

async def vsong_cmd(client, message):
    """Mengunduh dan mengirim video YouTube"""
    if len(message.command) < 2:
        return await message.reply_text("❌ Masukkan judul video dengan benar.")

    infomsg = await message.reply_text("🔍 Mencari...", quote=False)

    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"❌ Pencarian gagal.\n\n{error}")

    try:
        file_name, title, url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(link, as_video=True)
        if not file_name:
            raise Exception("Gagal mengunduh video.")
    except Exception as error:
        return await infomsg.edit(f"🔥 Download gagal.\n\n{error}")

    thumbnail = wget.download(thumb)
    
    await client.send_video(
        message.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format("video", title, timedelta(seconds=duration), views, channel, url, client.me.mention),
        progress=progress,
        progress_args=(infomsg, time.time(), "📥 Mengunduh...", f"{search['id']}.mp4"),
        reply_to_message_id=message.id,
    )

    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)

@PY.UBOT("vsong")
async def _(client, message):
    await vsong_cmd(client, message)

@PY.UBOT("song")
async def song_cmd(client, message):
    """Mengunduh dan mengirim audio dari YouTube"""
    if len(message.command) < 2:
        return await message.reply_text("❌ Masukkan judul lagu dengan benar.")

    infomsg = await message.reply_text("🔍 Mencari...", quote=False)

    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"❌ Pencarian gagal.\n\n{error}")

    try:
        file_name, title, url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(link, as_video=False)
        if not file_name:
            raise Exception("Gagal mengunduh lagu.")
    except Exception as error:
        return await infomsg.edit(f"🔥 Download gagal.\n\n{error}")

    thumbnail = wget.download(thumb)

    await client.send_audio(
        message.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format("audio", title, timedelta(seconds=duration), views, channel, url, client.me.mention),
        progress=progress,
        progress_args=(infomsg, time.time(), "📥 Mengunduh...", f"{search['id']}.mp3"),
        reply_to_message_id=message.id,
    )

    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)
    
