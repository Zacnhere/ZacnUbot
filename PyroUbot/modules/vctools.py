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
    """Menjalankan fungsi secara sinkron dalam event loop."""
    loop = asyncio.get_running_loop()
    return loop.run_in_executor(None, partial(func, *args, **kwargs))

async def YoutubeDownload(url, as_video=False):
    """Mengunduh audio/video dari YouTube."""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])" if as_video else "bestaudio[ext=m4a]",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "nocheckcertificate": True,
        "geo_bypass": True,
        "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None,  # Pastikan file cookie ada
    }
    
    try:
        ydl = YoutubeDL(ydl_opts)
        ytdl_data = await run_sync(ydl.extract_info, url, download=True)
        file_name = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data.get("id", "")
        title = ytdl_data.get("title", "Unknown")
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data.get("duration", 0)
        channel = ytdl_data.get("uploader", "Unknown")
        views = f"{ytdl_data.get('view_count', 0):,}".replace(",", ".")
        thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
        
        return file_name, title, url, duration, views, channel, thumb
    except Exception as e:
        return None, None, None, None, None, None, None, str(e)

async def playing_cmd(client, message: Message):
    """Memainkan audio dari YouTube atau file lokal."""
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
            return await message.reply_text(f"<blockquote>{ggl}<b>Masukkan judul video dengan benar.</b></blockquote>")
        
        infomsg = await message.reply_text(f"{prs}<b>ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
        try:
            search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()["result"][0]
            link = f"https://youtu.be/{search['id']}"
        except Exception as error:
            return await infomsg.edit(f"{prs}pencarian gagal...\n\n{error}")
        
        try:
            file_name, title, url, duration, views, channel, thumb = await YoutubeDownload(link, as_video=False)
            if not file_name:
                raise Exception("Gagal mengunduh video.")
        except Exception as error:
            return await infomsg.edit(f"{ggl}downloader gagal..\n\n{error}")

    await client.call_py.play(
        message.chat.id, 
        MediaStream(file_name, video_flags=MediaStream.Flags.IGNORE, audio_parameters=AudioQuality.STUDIO)
    )

    if message.reply_to_message and message.reply_to_message.audio:
        await infomsg.edit(f"{sks}<b>Memutar audio:</b> {title}")
    else:
        await infomsg.delete()
        await message.reply_text(
            f"<b>Memutar Audio:</b> {title}\n"
            f"<b>Durasi:</b> {timedelta(seconds=duration)}\n"
            f"<b>Views:</b> {views}\n"
            f"<b>Channel:</b> {channel}\n"
            f"<b>Link:</b> <a href='{url}'>YouTube</a>",
            disable_web_page_preview=True,
        )

    for files in (thumb, file_name):
        if files and os.path.isfile(files):
            os.remove(files)

async def check_gcch(client, message: Message):
    """Memeriksa apakah perintah dijalankan di grup atau channel."""
    ggl = await EMO.GAGAL(client)
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL):
        return await message.reply_text(f"<blockquote><b>{ggl}Gunakan di grup atau channel!</b></blockquote>")
    return None

@PY.UBOT("play")
async def play_music(client, message: Message):
    """Perintah untuk memainkan musik."""
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
            return await message.reply(f"<blockquote><b>{ggl}Sedang berada di obrolan. Gunakan di LVC!</b></blockquote>")
        elif status in (Call.Status.PLAYING, Call.Status.PAUSED):
            return await message.reply(f"<blockquote><b>{ggl}Harap tunggu lagu selesai!</b></blockquote>")
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
