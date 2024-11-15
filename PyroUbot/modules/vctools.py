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

async def YoutubeDownload(url, as_video=False):
    if as_video:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    else:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    data_ytp = "<b><emoji id=6005994005148471369>💡</emoji> ʙᴇʀʜᴀsɪʟ ᴍᴇᴍᴜᴛᴀʀ ᴍᴜsɪᴄ {}</b>\n\n<b><emoji id=5904544038643569182>🏷</emoji> ɴᴀᴍᴀ:</b> {}<b>\n<b><emoji id=6030547358222127917>🧭</emoji> ᴅᴜʀᴀsɪ:</b> {}\n<b><emoji id=5233246225146332642>👀</emoji> ᴅɪʟɪʜᴀᴛ:</b> {}\n<b><emoji id=6005896024059547548>📢</emoji> ᴄʜᴀɴɴᴇʟ:</b> {}\n<b><emoji id=6005993794695076239>🔗</emoji> ᴛᴀᴜᴛᴀɴ:</b> <a href={}>ʏᴏᴜᴛᴜʙᴇ</a>\n\n<b><emoji id=5801170880272797821>⚡</emoji> ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> {}"
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

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "kb", 2: "mb", 3: "gb", 4: "tb"}
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
        + (f"{str(milliseconds)} mikrodetik, " if milliseconds else "")
    )
    return tmp[:-2]


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("⊯" for _ in range(math.floor(percentage / 10))),
            "".join("~" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nestimasi: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    f"""
<b>{type_of_ps}</b>

<b>file_id:</b> <code>{file_name}</code>

<b>{tmp}</b>
"""
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit(f"{type_of_ps}\n{tmp}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass

async def check_admin_permissions(client, chat_id):
    member = await client.get_chat_member(chat_id, client.me.id)
    return member.status == "administrator" and member.can_manage_voice_chats
 

@PY.UBOT("play")
@PY.GROUP
@PY.ULTRA
async def play_handler(client: Client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    if len(message.command) < 2 or message.command[1] == '':
        return await message.reply_text(
            f"{ggl}<b>ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ</b>",
        )
    await message.delete()
    infomsg = await message.reply_text(f"<b>{prs}ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>{prs}ᴘᴇɴᴄᴀʀɪᴀɴ...</b>\n\n{error}")
    try:
        (
            file_name,
            title,
            url,
            duration,
            views,
            channel,
            thumb,
            data_ytp,
        ) = await YoutubeDownload(link, as_video=False)
    except Exception as error:
        return await infomsg.edit(f"<b>{prs}ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    await client.send_message(
        message.chat.id,
        text=data_ytp.format(
            "audio",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        reply_to_message_id=message.id,
        disable_web_page_preview=True,
    )
    await infomsg.delete()
    await client.call_py.play(
        message.chat.id,
        MediaStream(
        file_name,
        AudioQuality.STUDIO,
        ),
    )
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)

@PY.UBOT("lvc")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    try:
        mex = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")
        cc = await client.call_py.leave_call(message.chat.id)
        await mex.edit(f"<blockquote>{brhsl}<b>╭sᴜᴄᴄᴇss ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>\n{grp}<b>╰ɢʀᴏᴜᴘs :</b><code>{message.chat.title}</code></blockquote>")
    except NotInCallError:
        await mex.edit(f"<blockquote>{ggl}<b>ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ʏᴇᴛ</b></blockquote>")
    except UserBannedInChannel:
        pass
    except Exception as r:
        print(r)

@PY.UBOT("jvc")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    try:
        mex = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ...</b>")
        await client.call_py.play(message.chat.id, MediaStream("storage/vc.mp3"))
        await client.call_py.mute_stream(message.chat.id)
        await mex.edit(f"<blockquote>{brhsl}<b>╭sᴜᴄᴄᴇss ᴊᴏɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>\n{grp}<b>╰ɢʀᴏᴜᴘs :</b><code>{message.chat.title}</code></blockquote>")        
    except ChatAdminRequired:
        await mex.edit(f"<blockquote>{gg}<b>sᴏʀʀʏ, ɪ ᴄᴀɴ'ᴛ ᴊᴏɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b></blockquote>")
    except UserBannedInChannel:
        pass
    except Exception as r:
        print(r)

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
async def start_vc(client: Client, message: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
   
    flags = " ".join(message.command[1:])
    _msg = f"<b>{prs} Processing...</b>"

    msg = await message.reply(_msg)
    vctitle = get_arg(message)  # Fungsi ini diasumsikan mengambil judul dari argumen pesan
    chat_id = message.chat.id if message.chat.type == ChatType.CHANNEL else message.chat.title

    args = f"<b>{brhsl} Voice Chat Started\nChat:</b> {chat_id}"

    try:
        if vctitle:
            args += f"\n<b>Title:</b>  {vctitle}"

        await client.invoke(
            CreateGroupCall(
                peer=(await client.resolve_peer(chat_id)),
                random_id=randint(10000, 999999999),
                title=vctitle if vctitle else None,
            )
        )
        await msg.edit(args)
    except Exception as e:
        await msg.edit(f"INFO: {e}")


@PY.UBOT("stopvc")
@PY.GROUP
async def stop_vc(client: Client, message: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    _msg = f"<b>{prs} Processing...</b>"

    msg = await message.reply(_msg)
    
    # Dapatkan panggilan grup saat ini
    group_call = await get_group_call(client, message)  # Fungsi ini diasumsikan memeriksa panggilan grup

    if not group_call:
        await msg.edit(f"<b>{ggl} No ongoing voice chat in this group.</b>")
        return

    try:
        await client.invoke(DiscardGroupCall(call=group_call))
        await msg.edit(
            f"<b>{brhsl} Voice Chat Ended\nChat:</b> {message.chat.title}"
        )
    except Exception as e:
        await msg.edit(f"ERROR: {e}")
