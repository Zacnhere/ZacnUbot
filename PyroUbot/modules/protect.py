import asyncio
import random

from pyrogram import *
from gc import get_objects
from asyncio import sleep

from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *


__MODULE__ = "protect"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴘʀᴏᴛᴇᴄᴛ 』</b>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}protect</code> [on/off]
   <i>mengaktifkan atau menonaktifkan protect</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}word</code>
   <i>menambahkan kata ke daftar listword</i> 

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delword</code>
   <i>menghapus kata dari daftar listword</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listword</code>
   <i>melihat daftar word/kata yang di larang</i>
  
"""


cached_word_list = []
cache_expiry_time = None

async def get_word_list(client):
    global cached_word_list, cache_expiry_time
    if cache_expiry_time is None or cache_expiry_time < asyncio.get_event_loop().time():
        cached_word_list = await get_vars(client.me.id, "WORD_LIST") or []
        cache_expiry_time = asyncio.get_event_loop().time() + 60
    
    return cached_word_list

@PY.NO_CMD_UBOT("HANDLE_WORD_USER", ubot)
async def process_message(client, message):
    try:
        word_split = message.text.lower().split()
    except AttributeError:
        pass
    
    word_list = await get_word_list(client)
    try:
        for x in word_split:
            if x in word_list:
                try:
                    await message.delete()
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    pass
    except UnboundLocalError:
        pass


@PY.UBOT("protect")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    grp = await EMO.BL_GROUP(client)
    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴏɴ/ᴏғғ]</b>"
        )

    query = {"on": True, "off": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴏɴ/ᴏғғ]</b>"
        )

    txt = (
        f"<b>{brhsl}ᴘʀᴏᴛᴇᴄᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ\n{grp}ɢʀᴏᴜᴘ:</b><code>{message.chat.title}</code>"
        if command == "on"
        else f"<b>{brhsl}ᴘʀᴏᴛᴇᴄᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n{grp}ɢʀᴏᴜᴘ:</b><code>{message.chat.title}</code>"
    )
    await set_vars(client.me.id, f"chat_{message.chat.id}", query[command])
    await message.reply(txt)


@PY.UBOT("word")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    vars = await get_vars(client.me.id, "LIST_WORD") or []
    text = get_arg(message).split()
   
    add_word = [x for x in text if x not in vars]
    vars.extend(add_word)
    await set_vars(client.me.id, "LIST_WORD", vars)
   
    if add_word:
        response = (
            f"<b>{brhsl}ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜ ᴋᴇ ᴘʀᴏᴛᴇᴄᴛ</b>\n"
            f"<b>{ktrng}ᴋᴀᴛᴀ:</b> <code>{''.join(add_word)}</code>"
        )
    else:
        response = f"<b>{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪᴛᴀᴍʙᴀʜ.</b>"

    return await message.reply(response)

@PY.UBOT("listword")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    vars = await get_vars(client.me.id, "LIST_WORD") or []
    if vars:
        msg = f"<b>{brhsl}ᴅᴀғᴛᴀʀ ᴡᴏʀᴅ</b>\n\n"
        for x in vars:
            msg += f" • <code>{x}</code>\n"
        msg += f"<b>\n{ktrng}ᴛᴏᴛᴀʟ ᴡᴏʀᴅ: {len(vars)}</b>"
    else:
        msg = f"<b>{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴡᴏʀᴅ</b>"
        
    return await message.reply(msg, quote=True)


@PY.UBOT("delword")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    vars = await get_vars(client.me.id, "LIST_WORD") or []
    _, *text = message.command
    removed_list = [x for x in text if x in vars]
    vars = [x for x in vars if x not in removed_list]
    await set_vars(client.me.id, "LIST_WORD", vars)

    if removed_list:
        response = (
            f"<b>{brhsl}ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴘʀᴏᴛᴇᴄᴛ</b>\n"
            f"<b>{ktrng}ᴋᴀᴛᴀ:</b> <code>{''.join(removed_list)}</code>"
        )
    else:
        response = f"<b>{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪʜᴀᴘᴜs.</b>"

    return await message.reply(response)

@PY.NO_CMD_UBOT("PROTECT", ubot)
async def _(client, message):
    if await get_vars(client.me.id, f"chat_{message.chat.id}"):
        word_split = message.text.split()
        word_list = await get_vars(client.me.id, "LIST_WORD") or []
        mention = (
            f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
            if message.from_user
            else "."
        )
        for x in word_split:
            if x in word_list:
                try:
                    await message.delete()
                    msg = await message.reply(
                        f"{mention}, <i>**ᴋᴀᴛᴀ-ᴋᴀᴛᴀ ᴀɴᴅᴀ ᴀᴅᴀ ᴅɪ ᴘʀᴏᴛᴇᴄᴛ**</i>"
                    )
                    await asyncio.sleep(5)
                    return await msg.delete()
                except Exception:
                    pass
