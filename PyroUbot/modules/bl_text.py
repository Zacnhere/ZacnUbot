import asyncio
import random

from gc import get_objects
from asyncio import sleep

from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *


__MODULE__ = "bltext"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ʙʟᴀᴄᴋʟɪsᴛ ᴛᴇxᴛ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}bltext</code> [ᴏɴ/ᴏғғ]
   <i>mengaktifkan atau menonaktifkan bltext</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}atext</code> [ᴋᴀᴛᴀ/ʀᴇᴘʟʏ]
   <i>menambahkan kata ke daftar listword</i> 

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}dtext</code>
   <i>menghapus kata dari daftar listtext</i> [ᴋᴀᴛᴀ]

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listtext</code>
   <i>melihat daftar word/kata yang di larang</i>
   </blockquote>
"""
import asyncio
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


@PY.UBOT("bltext")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
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
        f"<b>{sks}ʙʟ_ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>"
        if command == "on"
        else f"<b>{sks}ʙʟ_ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>"
    )
    await set_vars(client.me.id, "ON_OFF_WORD", query[command])
    await message.reply(txt)


@PY.UBOT("atext")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    vars = await get_vars(client.me.id, "WORD_LIST") or []
    text = get_arg(message).split()
   
    add_word = [x for x in text if x not in vars]
    vars.extend(add_word)
    await set_vars(client.me.id, "WORD_LIST", vars)
   
    if add_word:
        response = (
            f"<b>{sks}ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜ ᴋᴇ ʙʟ_ᴛᴇxᴛ</b>\n"
            f"<b>{ktrng}ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪᴛᴀᴍʙᴀʜ:</b> {''.join(add_word)}"
        )
    else:
        response = f"<b>{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪᴛᴀᴍʙᴀʜ</b>"

    return await message.reply(response)


@PY.UBOT("listtext")
@PY.ULTRA
async def _(client, message):
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    vars = await get_vars(client.me.id, "WORD_LIST") or []
    if vars:
        msg = f"<b>{ktrng} ᴅᴀғᴛᴀʀ ᴡᴏʀᴅ</b>\n\n"
        for x in vars:
            msg += f" ⌦ <code>{x}</code>\n"
        msg += f"<b>\n{sks} ᴛᴏᴛᴀʟ ᴡᴏʀᴅ: {len(vars)}</b>"
    else:
        msg = f"{ggl}<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴡᴏʀᴅ</b>"
        
    return await message.reply(msg, quote=True)


@PY.UBOT("dtext")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    vars = await get_vars(client.me.id, "WORD_LIST") or []
    _, *text = message.command
    removed_list = [x for x in text if x in vars]
    vars = [x for x in vars if x not in removed_list]
    await set_vars(client.me.id, "WORD_LIST", vars)

    if removed_list:
        response = (
            f"<b>{sks}ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ʙʟ_ᴛᴇxᴛ</b>\n"
            f"<b>{ktrng}ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪʜᴀᴘᴜs:</b> {''.join(removed_list)}"
        )
    else:
        response = f"<b>{ggl}ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴋᴀᴛᴀ ʏᴀɴɢ ᴅɪʜᴀᴘᴜs</b>"

    return await message.reply(response)
