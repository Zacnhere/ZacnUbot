import asyncio
import random

from pyrogram import *
from pyrogram import types
from asyncio import sleep

from PyroUbot import *

__MODULE__ = "antiuser"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴᴛɪᴜsᴇʀ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}antiuser</code> <b>ᴏɴ/ᴏғғ</b>
   <i>untuk menhidupkan dan mematikan</i>
   
<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}dor</code>
   <i>tambahkan pengguna dalam blacklist</i>
   
<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}undor</code>
   <i>hapus pengguna dalam blacklist</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}getuser</code>
   <i>melihat daftar blacklist</i>
   
<b>➢ ɴᴏᴛᴇs:</b> 
   <i>pengguna yang di tambahkan tidak bisa
     mengirim pesan di group yang anda admin</i>
     </blockquote>
"""

import asyncio
import random

from pyrogram import *
from pyrogram import types
from asyncio import sleep
from PyroUbot.config import OWNER_ID
from PyroUbot import *
from pyrogram.errors.exceptions import FloodWait

@PY.UBOT("antiuser")
@PY.ULTRA
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"<blockquote><b>{ggl}ɢᴜɴᴀᴋᴀɴ ᴏɴ/ᴏғғ</b></blockquote>")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "ON_OFF_ANTI_USER", type)
    return await txt.edit(f"<blockquote><b>{sks}ᴀɴᴛɪᴜsᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b></blockquote>")


@PY.UBOT("dor")
@PY.ULTRA
async def add_user_to_blacklist(c, m):
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)

    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"<blockquote>{ggl}<b>ғᴏʀᴍᴀᴛ [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])
    if user_id == OWNER_ID:
        return await m.reply(f"<blockquote>{ggl}<b>ɢᴜᴀ ʏᴀɴɢ ᴘᴜɴʏᴀ ʙᴏᴛ ᴛᴏᴅ!</b></blockquote>")
    user_ids = await get_user_ids(c.me.id)
    if user_id not in user_ids:
        user_ids.append(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"<blockquote>{brhsl}<b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴᴛɪᴜsᴇʀ!!</b></blockquote>", quote=True)
    else:
        await m.reply_text(f"<blockquote>{ggl}<b>sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ᴀɴᴛɪᴜsᴇʀ!!</b></blockquote>", quote=True)

@PY.UBOT("undor")
@PY.ULTRA
async def remove_user_from_blacklist(c, m):
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)

    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"<blockquote>{ggl}<b>ғᴏʀᴍᴀᴛ [ʀᴇᴘʟʏ_ᴘᴇꜱᴀɴ]</b></blockquote>", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    user_ids = await get_user_ids(c.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"<blockquote><b>ᴜsᴇʀ</b> : `{user_id}` \n<b>{brhsl}ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</b></blockquote>", quote=True)
    else:
        await m.reply_text(f"<blockquote>{ggl}<b>ᴜsᴇʀ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ</b></blockquote>", quote=True)

@PY.UBOT("getuser")
@PY.ULTRA
@PY.TOP_CMD
async def display_blacklist(client, message):
    sks = await EMO.BERHASIL(client)
    try:
        daftar = await get_user_ids(client.me.id)
        pesan = "\n".join(f"<blockquote><b>{sks}ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</b>\n\n ⌦ <code>`{x}`</code></blockquote>" for x in daftar)
        await message.reply(pesan)
    except Exception as r:
        await message.reply(r)
       
# Mengatur dan memproses perintah antiuser (on/off)
@PY.UBOT("antipc")
@PY.ULTRA
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"<blockquote><b>{ggl}ɢᴜɴᴀᴋᴀɴ ᴏɴ/ᴏғғ</b></blockquote>")

    # Menyimpan status antiuser pada ID pengguna bot (client)
    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "ON_OFF_ANTI_USER", type)
    return await txt.edit(f"<blockquote><b>{sks}ᴀɴᴛɪᴜsᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b></blockquote>")


# Menambahkan pengguna ke dalam blacklist berdasarkan chat pribadi
@PY.UBOT("tambah")
@PY.ULTRA
async def add_user_to_blacklist(c, m):
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)

    # Mengecek apakah format perintah sudah benar (perlu user_id atau reply)
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"<blockquote>{ggl}<b>ғᴏʀᴍᴀᴛ [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>", quote=True)
        return

    # Mendapatkan user_id yang akan diblacklist, baik dari reply atau perintah
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    # Cek jika user_id adalah pemilik bot, tidak bisa diblacklist
    if user_id == OWNER_ID:
        return await m.reply(f"<blockquote>{ggl}<b>ɢᴜᴀ ʏᴀɴɢ ᴘᴜɴʏᴀ ʙᴏᴛ ᴛᴏᴅ!</b></blockquote>")
    
    # Mendapatkan daftar ID pengguna yang diblacklist berdasarkan chat pribadi
    user_ids = await get_user_ids(c.me.id)
    if user_id not in user_ids:
        # Menambahkan user_id ke dalam daftar blacklist
        user_ids.append(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"<blockquote>{brhsl}<b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴᴛɪᴜsᴇʀ!!</b></blockquote>", quote=True)
    else:
        # Jika user sudah ada dalam blacklist
        await m.reply_text(f"<blockquote>{ggl}<b>sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ᴀɴᴛɪᴜsᴇʀ!!</b></blockquote>", quote=True)


# Menghapus pengguna dari blacklist berdasarkan chat pribadi
@PY.UBOT("hapus")
@PY.ULTRA
async def remove_user_from_blacklist(c, m):
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)

    # Mengecek apakah format perintah sudah benar (perlu user_id atau reply)
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"<blockquote>{ggl}<b>ғᴏʀᴍᴀᴛ [ʀᴇᴘʟʏ_ᴘᴇꜱᴀɴ]</b></blockquote>", quote=True)
        return

    # Mendapatkan user_id yang akan dihapus dari blacklist
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    # Mendapatkan daftar ID pengguna yang diblacklist berdasarkan chat pribadi
    user_ids = await get_user_ids(c.me.id)
    if user_id in user_ids:
        # Menghapus user_id dari daftar blacklist
        user_ids.remove(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"<blockquote><b>ᴜsᴇʀ</b> : `{user_id}` \n<b>{brhsl}ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</b></blockquote>", quote=True)
    else:
        # Jika user tidak ada dalam blacklist
        await m.reply_text(f"<blockquote>{ggl}<b>ᴜsᴇʀ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴇʀ</b></blockquote>", quote=True)


# Menampilkan daftar pengguna dalam blacklist
@PY.UBOT("antipclist")
@PY.ULTRA
@PY.TOP_CMD
async def display_blacklist(client, message):
    sks = await EMO.BERHASIL(client)
    try:
        # Mendapatkan daftar ID pengguna yang ada dalam blacklist
        daftar = await get_user_ids(client.me.id)
        pesan = "\n".join(f"<blockquote><b>{sks}ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</b>\n\n ⌦ <code>`{x}`</code></blockquote>" for x in daftar)
        await message.reply(pesan)
    except Exception as r:
        await message.reply(r)
