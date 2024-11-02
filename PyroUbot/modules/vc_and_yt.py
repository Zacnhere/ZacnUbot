import math
import wget
import os
import asyncio
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
    dict_power_n = {0: "", 1: "ᴋʙ", 2: "ᴍʙ", 3: "ɢʙ", 4: "ᴛʙ"}
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
        (f"{str(days)} ʜᴀʀɪ, " if days else "")
        + (f"{str(hours)} ᴊᴀᴍ, " if hours else "")
        + (f"{str(minutes)} ᴍᴇɴɪᴛ, " if minutes else "")
        + (f"{str(seconds)} ᴅᴇᴛɪᴋ, " if seconds else "")
        + (f"{str(milliseconds)} ᴍɪᴋʀᴏᴅᴇᴛɪᴋ, " if milliseconds else "")
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
            "".join("•" for _ in range(math.floor(percentage / 10))),
            "".join("~" for _ in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nᴇsᴛɪᴍᴀsɪ: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    f"""
<b>{type_of_ps}</b>

<b>ғɪʟᴇ_ɪᴅ:</b> <code>{file_name}</code>

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

@PY.UBOT("vsong")
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b><emoji id=6161479118413106534>❌</emoji>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,</b>\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.",
        )
    infomsg = await message.reply_text("<b>ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<emoji id=5188217332748527444>🔍</emoji><b>ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}</b>")
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
        ) = await YoutubeDownload(link, as_video=True)
    except Exception as error:
        return await infomsg.edit(f"<b>ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    await client.send_video(
        message.chat.id,
        video=file_name,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption=data_ytp.format(
            "ᴠɪᴅᴇᴏ",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        progress=progress,
        progress_args=(
            infomsg,
            time(),
            "<b>ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...</b>",
            f"{search['id']}.mp4",
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)


@PY.UBOT("song")
async def song_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b><emoji id=6161479118413106534>❌</emoji>ᴀᴜᴅɪᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ,</b>\nᴍᴏʜᴏɴ ᴍᴀsᴜᴋᴀɴ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ ᴅᴇɴɢᴀɴ ʙᴇɴᴀʀ.",
        )
    infomsg = await message.reply_text("<b><emoji id=5188217332748527444>🔍</emoji>ᴘᴇɴᴄᴀʀɪᴀɴ...</b>", quote=False)
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()[
            "result"
        ][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as error:
        return await infomsg.edit(f"<emoji id=5188217332748527444>🔍</emoji><b>ᴘᴇɴᴄᴀʀɪᴀɴ...\n\n{error}</b>")
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
        return await infomsg.edit(f"<b>ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...\n\n{error}</b>")
    thumbnail = wget.download(thumb)
    await client.send_audio(
        message.chat.id,
        audio=file_name,
        thumb=thumbnail,
        file_name=title,
        performer=channel,
        duration=duration,
        caption=data_ytp.format(
            "ᴀᴜᴅɪᴏ",
            title,
            timedelta(seconds=duration),
            views,
            channel,
            url,
            bot.me.mention,
        ),
        progress=progress,
        progress_args=(
            infomsg,
            time(),
            "<b>ᴅᴏᴡɴʟᴏᴀᴅᴇʀ...</b>",
            f"{search['id']}.mp3",
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_name):
        if files and os.path.exists(files):
            os.remove(files)


# async def get_group_call(client, message):
    # chat_peer = await client.resolve_peer(message.chat.id)
    # if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        # if isinstance(chat_peer, InputPeerChannel):
            # full_chat = (
                # await client.invoke(GetFullChannel(channel=chat_peer))
            # ).full_chat
        # elif isinstance(chat_peer, InputPeerChat):
            # full_chat = (
                # await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            # ).full_chat
        # if full_chat is not None:
            # return full_chat.call
    # await message.reply("<b>ɴᴏ ɢʀᴏᴜᴘ ᴄᴀʟʟ</b>")
    # return False

# @PY.UBOT("startvc")
# @PY.GROUP
# async def _(client, message):
    # flags = " ".join(message.command[1:])
    # _msg = "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    # msg = await message.reply(_msg)
    # vctitle = get_arg(message)
    # chat_id = message.chat.title if flags == ChatType.CHANNEL else message.chat.id

    # args = f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴀᴋᴛɪꜰ\nᴄʜᴀᴛ :</b> {chat_id}"

    # try:
        # if vctitle:
            # args += f"\n<b>ᴛɪᴛʟᴇ :</b>  {vctitle}"

        # await client.invoke(
            # CreateGroupCall(
                # peer=(await client.resolve_peer(chat_id)),
                # random_id=randint(10000, 999999999),
                # title=vctitle if vctitle else None,
            # )
        # )
        # await msg.edit(args)
    # except Exception as e:
        # await msg.edit(f"INFO: {e}")


# @PY.UBOT("stopvc")
# @PY.GROUP
# async def _(client, message):
    # _msg = "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    # msg = await message.reply(_msg)
    # group_call = await get_group_call(client, message)

    # if not group_call:
        # return await msg.edit("<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴏʙʀᴏʟᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ</b>")

    # await client.invoke(DiscardGroupCall(call=group_call))
    # await msg.edit(
        # f"<b>ᴏʙʀᴏʟᴀɴ ꜱᴜᴀʀᴀ ᴅɪᴀᴋʜɪʀɪ\nᴄʜᴀᴛ :</b> {message.chat.title}"
    # )


# @PY.UBOT("joinvc")
# @PY.GROUP
# async def _(client, message):
    # prs = await EMO.PROSES(client)
    # brhsl = await EMO.BERHASIL(client)
    # _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    # msg = await message.reply(_msg)
    # chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    # try:
        # await client.group_call.start(chat_id, join_as=client.me.id)
    # except Exception as e:
        # return await msg.edit(f"ERROR: {e}")
    # await msg.edit(
        # "{} <b>ʙᴇʀʜᴀsɪʟ ɴᴀɪᴋ ᴋᴇ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ\n• ᴄʜᴀᴛ :</b> {}".format(brhsl,message.chat.title)
    # )
    # await asyncio.sleep(5)
    # await client.group_call.set_is_mute(True)


# @PY.UBOT("leavevc")
# @PY.GROUP
# async def _(client, message):
    # prs = await EMO.PROSES(client)
    # brhsl = await EMO.BERHASIL(client)
    # _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    # msg = await message.reply(_msg)
    # try:
        # await client.group_call.stop()
    # except Exception as e:
        # return await msg.edit(f"ERROR: {e}")
    # await msg.edit(f"<b>{brhsl}ʙᴇʀʜᴀsɪʟ ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>")
