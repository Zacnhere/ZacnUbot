__MODULE__ = "vctools"
__HELP__ = """
<blockquote>
<b> 『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ  ᴠᴄᴛᴏᴏʟs 』 </b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}jvc</code>
   <i>untuk bergabung ke voice chat group</i>
   
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}lvc</code>
   <i>untuk meninggalkan dari voice chat group</i>
   
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}startvc</code>
   <i>untuk memulai voice chat group</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopvc</code>
   <i>untuk mengakhiri voice chat group</i>
   </blockquote>
"""
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from asyncio import get_event_loop
from functools import partial
from yt_dlp import YoutubeDL
from pytgcalls import filters as fl
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pytgcalls.types import ChatUpdate
from pytgcalls.types import GroupCallParticipant
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoQuality
from pytgcalls.types import Update
from pyrogram.errors.exceptions.bad_request_400 import UserBannedInChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, GetGroupCall
from pyrogram.raw.types import InputGroupCall
from random import randint
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel, InputPeerChat
from pyrogram.errors import FloodWait, MessageNotModified

import asyncio
import math
import os
from datetime import timedelta
from time import time
from pytgcalls.exceptions import NotInCallError
import wget
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch
from pyrogram.enums import ChatType
from PyroUbot import *


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))

async def YoutubeDownload(url, as_video=False):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])" if as_video else "bestaudio[ext=m4a]",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "nocheckcertificate": True,
        "geo_bypass": True,
        "cookiefile": "cookies.txt",
    }
    data_ytp = "<blockquote><b><emoji id=6005994005148471369>💡</emoji> ᴍᴇᴍᴜᴛᴀʀ {}\n\n<emoji id=5904544038643569182>🏷</emoji> ɴᴀᴍᴀ: {}\n<emoji id=6030547358222127917>🧭</emoji> ᴅᴜʀᴀsɪ: {}\n<emoji id=5233246225146332642>👀</emoji> ᴅɪʟɪʜᴀᴛ: {}\n<emoji id=6005896024059547548>📢</emoji> ᴄʜᴀɴɴᴇʟ: {}\n<emoji id=6005993794695076239>🔗</emoji> ᴛᴀᴜᴛᴀɴ: <a href={}>youtube</a>\n\n<emoji id=5801170880272797821>⚡</emoji> ᴘᴏᴡᴇʀᴇᴅ ʙʏ: {}</b></blockquote>"
    ydl = YoutubeDL(ydl_opts)
    ytdl_data = await run_sync(ydl.extract_info, url, download=True)
    file_name = ydl.prepare_filename(ytdl_data)
    videoid = ytdl_data["id"]
    title = ytdl_data["title"]
    url = f"https://youtu.be/{videoid}"
    duration = ytdl_data["duration"]
    channel = ytdl_data["uploader"]
    views = f"{ytdl_data['view_count']:,}".replace(",", ".")
    thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    return file_name, title, url, duration, views, channel, thumb, data_ytp

async def playing_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    if message.reply_to_message and message.reply_to_message.audio:
        audio = message.reply_to_message.audio
        infomsg = await message.reply_text(f"{prs}<b>ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ...</b>", quote=False)
        file_name = await client.download_media(audio)
        title = audio.title or "Audio"
        duration = audio.duration or 0
        url = audio.file_id
        channel = "Local Audio"
        views = "N/A"
        thumb = None
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                f"<blockquote>{ggl}<b>ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ! ᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ</b></blockquote>",
            )
        infomsg = await message.reply_text(f"{prs}<b>ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
        try:
            search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()["result"][0]
            link = f"https://youtu.be/{search['id']}"
        except Exception as error:
            return await infomsg.edit(f"{prs}pencarian...\n\n{error}")
        try:
            file_name, title, url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(link, as_video=False)
        except Exception as error:
            return await infomsg.edit(f"{ggl}downloader..\n\n{error}")

    await client.call_py.play(message.chat.id, MediaStream(
        file_name,
        video_flags=MediaStream.Flags.IGNORE,
        audio_parameters=AudioQuality.STUDIO,
        ),
    )

    if message.reply_to_message and message.reply_to_message.audio:
        await infomsg.edit(f"{sks}<b>ᴍᴇᴍᴜᴛᴀʀ ᴀᴜᴅɪᴏ:</b> {title}")
    else:
        await infomsg.delete()
        await message.reply_text(data_ytp.format(
            "audio",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention),
            disable_web_page_preview=True,
        )
    for files in (thumb, file_name):
        if files and os.path.exists(files):
            os.remove(files)


async def check_gcch(client, message):
    ggl = await EMO.GAGAL(client)
    chat_id = message.chat.id
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL):
        return await message.reply_text(f"<blockquote><b>{ggl}ɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴜᴘ ᴀᴛᴀᴜ ᴄʜᴀɴɴᴇʟ !</b></blockquote>")
    return None

@PY.UBOT("play")
async def play_music(client, message):
    result = await check_gcch(client, message)
    if result:
        return

    ggl = await EMO.GAGAL(client)
    chat_id = message.chat.id
    calls = await client.call_py.calls
    chat_call = calls.get(chat_id)

    if chat_call:
        status = chat_call.status
        if status == Call.Status.IDLE:
            return await message.reply(f"<blockquote><b>{ggl}ᴀᴋᴜɴ ᴋᴀᴍᴜ sᴇᴅᴀɴɢ ʙᴇʀᴀᴅᴀ ᴅɪ ᴏʙʀᴏʟᴀɴ\nᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ʟᴠᴄ !</b></blockquote>")
        elif status in (Call.Status.PLAYING, Call.Status.PAUSED):
            return await message.reply(f"<blockquote><b>{ggl}ʜᴀʀᴀᴘ ᴛᴜɴɢɢᴜ ʟᴀɢᴜɴʏᴀ sᴇʟᴇsᴀɪ !</b></blockquote>")
    else:
        await playing_cmd(client, message)


@PY.UBOT("lvc")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)

    try:
        # Mendapatkan ID grup dari argumen atau gunakan grup saat ini
        args = message.text.split()
        if len(args) > 1:
            target_group_id = int(args[1])
            chat = await client.get_chat(target_group_id)
        else:
            target_group_id = message.chat.id
            chat = message.chat

        # Kirim pesan pemrosesan
        mex = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")

        # Keluar dari Voice Chat di grup target
        await client.call_py.leave_call(target_group_id)

        # Kirim pesan sukses
        await mex.edit(
            f"<blockquote>{brhsl}<b>╭sᴜᴄᴄᴇss ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>\n"
            f"{grp}<b>╰ɢʀᴏᴜᴘ :</b> <code>{chat.title}</code></blockquote>"
        )
    except NotInCallError:
        await mex.edit(
            f"<blockquote>{ggl}<b>ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ʏᴇᴛ</b></blockquote>"
        )
    except ValueError:
        await mex.edit(f"{ggl}<b>Error:</b> Invalid group ID.")
    except UserBannedInChannel:
        await mex.edit(f"{ggl}<b>Error:</b> You are banned from the channel.")
    except Exception as r:
        await mex.edit(
            f"{ggl}<b>Failed to leave the voice chat.</b>\n<code>{r}</code>"
        )
        logging.error(f"Error in leaving VC for group {target_group_id}:", exc_info=True)
     

@PY.UBOT("jvc")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)

    try:
        # Mendapatkan ID grup dari argumen atau gunakan grup saat ini
        args = message.text.split()
        if len(args) > 1:
            target_group_id = int(args[1])
            chat = await client.get_chat(target_group_id)
        else:
            target_group_id = message.chat.id
            chat = message.chat

        # Kirim pesan pemrosesan
        mex = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")

        # Cek apakah file media tersedia
        if not os.path.exists("storage/vc.mp3"):
            await mex.edit(f"{ggl}<b>Error:</b> Media file not found.")
            return

        # Memulai Voice Chat di grup target
        await client.call_py.play(target_group_id, MediaStream("storage/vc.mp3"))
        await client.call_py.mute_stream(target_group_id)

        # Kirim pesan sukses
        await mex.edit(
            f"<blockquote>{brhsl}<b>╭sᴜᴄᴄᴇss ᴊᴏɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>\n"
            f"{grp}<b>╰ɢʀᴏᴜᴘ :</b> <code>{chat.title}</code></blockquote>"
        )
    except ChatAdminRequired:
        await mex.edit(
            f"<blockquote>{ggl}<b>sᴏʀʀʏ, ɪ ᴄᴀɴ'ᴛ ᴊᴏɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ ʀᴇQᴜɪʀᴇᴅ.</b></blockquote>"
        )
    except ValueError:
        await mex.edit(f"{ggl}<b>Error:</b> Invalid group ID.")
    except UserBannedInChannel:
        await mex.edit(f"{ggl}<b>Error:</b> You are banned from the channel.")
    except Exception as r:
        await mex.edit(
            f"{ggl}<b>Failed to join the voice chat.</b>\n<code>{r}</code>"
        )
        logging.error(f"Error in joining VC for group {target_group_id}:", exc_info=True)


@PY.UBOT("stream")
@PY.ULTRA
@PY.GROUP
async def _(c, m):
    if len(m.command) != 2:
        return await m.reply_text("<b>stream url</b>")
    
    url = m.command[1]
    cukimay = await c.call_py.play(
        m.chat.id,
        MediaStream(
            url,
        ),
    )
    print(cukimay)


@PY.UBOT("startvc")
@PY.GROUP
async def _(client, message):
    flags = " ".join(message.command[1:])
    _msg = "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    vctitle = get_arg(message)

    args = f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ\nᴄʜᴀᴛ :</b> {message.chat.title}"

    try:
        if vctitle:
            args += f"\n<b>ᴛɪᴛʟᴇ :</b>  {vctitle}"

        await client.invoke(
            CreateGroupCall(
                peer=(await client.resolve_peer(message.chat.id)),
                random_id=randint(10000, 999999999),
                title=vctitle if vctitle else None,
            )
        )
        await msg.edit(args)
    except Exception as e:
        await msg.edit(f"INFO: {e}")
     

@PY.UBOT("stopvc")
@PY.GROUP
async def _(client, message):
    _msg = "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    group_call = await get_group_call(client, message)

    if not group_call:
        return await msg.edit("<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏʙʀᴏʟᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ</b>")

    await client.invoke(DiscardGroupCall(call=group_call))
    await msg.edit(
        f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴅɪᴀᴋʜɪʀɪ\nᴄʜᴀᴛ :</b> {message.chat.title}"
    )
