import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *

__MODULE__ = "blacklist"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ʙʟᴀᴄᴋʟɪsᴛ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addbl</code>
   <i>memasukan group ke daftar blacklist</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unbl</code>
   <i>menghapus group dari daftar blacklist</i>
  
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}rallbl</code>
   <i>menghapus semua daftar blacklist group</i>
  
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listbl</code>
   <i>memeriksa daftar blacklist group</i>
   </blockquote> 
"""

@PY.UBOT("addbl")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    try:
        chat_id = message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id in blacklist:
            txt = f"""
<blockquote><b>{grp}ɢʀᴏᴜᴘ:</b> {message.chat.title}
<b>{ktrng}ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>ᴀʟʀᴇᴀᴅʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ</code></b></blockquote>
"""
        else:
            await add_to_vars(client.me.id, "BL_ID", chat_id)
            txt = f"""
<blockquote><b>{grp}ɢʀᴏᴜᴘ:</b> {message.chat.title}
<b>{ktrng}ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>ʙʟᴀᴄᴋʟɪsᴛᴇᴅ</code></b></blockquote>
"""

        return await msg.edit(txt)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("unbl")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    grp = await EMO.BL_GROUP(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    try:
        chat_id = get_arg(message) or message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID")

        if chat_id not in blacklist:
            response = f"""
<blockquote><b>{grp}ɢʀᴏᴜᴘ:</b> {message.chat.title}
<b>{ktrng}ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>ɴᴏᴛ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ</code></b></blockquote>
"""
        else:
            await remove_from_vars(client.me.id, "BL_ID", chat_id)
            response = f"""
<blockquote><b>{grp}ɢʀᴏᴜᴘ:</b> {message.chat.title}
<b>{ktrng}ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ</code></b></blockquote>
"""

        return await msg.edit(response)
    except Exception as error:
        return await msg.edit(str(error))


@PY.UBOT("listbl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    brhsl = await EMO.BERHASIL(client)
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"
    mzg = await message.reply(_msg)

    blacklist = await get_list_from_vars(client.me.id, "BL_ID")
    total_blacklist = len(blacklist)

    list = f"{ktrng} <b>ᴅᴀғᴛᴀʀ ʙʟᴀᴄᴋʟɪsᴛ</b>\n"

    for chat_id in blacklist:
        try:
            chat = await client.get_chat(chat_id)
            list += f" <blockquote>├ {chat.title} | <code>{chat.id}</code></blockquote>\n"
        except:
            list += f" <blockquote>├ {chat_id}</blockquote>\n"

    list += f"{brhsl} <b>ᴛᴏᴛᴀʟ ʙʟᴀᴄᴋʟɪsᴛ</b> {total_blacklist}"
    return await mzg.edit(list)


@PY.UBOT("rallbl")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    blacklists = await get_list_from_vars(client.me.id, "BL_ID")

    if not blacklists:
        return await msg.edit(f"{ggl}<b>ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ ᴀɴᴅᴀ ᴋᴏsᴏɴɢ</b>")

    for chat_id in blacklists:
        await remove_from_vars(client.me.id, "BL_ID", chat_id)

    await msg.edit(f"{brhsl}<b>sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ʜɪᴛᴀᴍ ᴛᴇʟᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")


