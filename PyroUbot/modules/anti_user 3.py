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


async def _(client, message):
    user = message.from_user
    nopm_on = await get_vars(client.me.id, "NOPM_STATUS")  # Ambil status NoPM dari database
    datanya = await get_list_from_vars(client.me.id, "BL_ID")
    if nopm_on:
          if user.id not in datanya:
              await client.delete_messages(message.chat.id, message.id)
              return

# Perintah untuk mengaktifkan atau menonaktifkan NoPM
@PY.UBOT("nopm")
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴏɴ/ᴏғғ]</b>"
        )

    toggle_options = {"off": False, "on": True}
    toggle_option = message.command[1].lower()

    if toggle_option not in toggle_options:
        return await message.reply(f"{ggl}ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. Hᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'.")

    value = toggle_options[toggle_option]
    text = "diaktifkan" if value else "dinonaktifkan"

    await set_vars(client.me.id, "NOPM_STATUS", value)
    await message.reply(f"<b>{brhsl}NoPM berhasil {text}</b>")



# Perintah untuk menerima pengguna (acc)
@PY.UBOT("acc|oke")
async def accept_user(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"<blockquote><b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>"
    msg = await message.reply(_msg)
    try:
        user = message.chat
        datanya = await get_list_from_vars(client.me.id, "BL_ID")
        if user.id in datanya:
            txt = f"""
<blockquote>{brhsl} [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})\n<b>Okey i'm acc you to send messages!</b></blockquote>
"""
        else:
            await add_to_vars(client.me.id, "BL_ID", user.id)
            txt = f"""
<blockquote>{brhsl} [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})\n<b>Done to acc!</b></blockquote>
"""
    
        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))
       
# Perintah untuk menolak pengguna (reject)
@PY.UBOT("reject|tangkis")
async def reject_user(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    user = message.chat
    datanya = await get_list_from_vars(client.me.id, "BL_ID")
    
    if user.id not in datanya:
        await message.reply(f"🙏🏻 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) <b>NoPM activated Block User</b>")
        try:
            await client.block_user(user.id)
        except Exception:
            pass
        
    else:
        await remove_from_vars(client.me.id, "BL_ID", user.id)
        return await message.reply(
            f"🙏🏻 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) <b>You can't send messages again</b>"
   )
