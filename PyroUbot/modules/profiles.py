import os
import asyncio
import random

from os import remove
from asyncio import sleep, gather

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.enums import ChatType

from PyroUbot import *


__MODULE__ = "profiles"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴘʀᴏꜰɪʟᴇ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setbio</code>
   <i>mengubah bio pada akun anda</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setname</code>
   <i>mengubah nama pada akun anda:</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}block</code>
   <i>memblokir pengguna</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unblock</code>
   <i>membuka pemblokiran pada pengguna</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}sg</code>
   <i>memeriksa histori name pengguna telegram</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}info</code>
   <i>melihat informasi data akun telegram</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cinfo</code>
   <i>melihat informasi data group/channel telegram</i>
   </blockquote> 
"""


@PY.UBOT("sg")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    get_user = await extract_user(message)
    lol = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not get_user:
        return await lol.edit(f"<b>{ggl}ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user_id = (await client.get_users(get_user)).id
    except Exception:
        try:
            user_id = int(message.command[1])
        except Exception as error:
            return await lol.edit(error)
    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)
    await client.unblock_user(getbot)
    txt = await client.send_message(getbot, user_id)
    await asyncio.sleep(4)
    await txt.delete()
    await lol.delete()
    async for name in client.search_messages(getbot, limit=2):
        if not name.text:
            await message.reply(
                f"{ggl}{getbot} <b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ ᴘᴇʀᴍɪɴᴛᴀᴀɴ</b>", quote=True
            )
        else:
            await message.reply(f"<blockquote>{name.text}</blockquote>", quote=True)
    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))


@PY.UBOT("info")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    user_id = await extract_user(message)
    Tm = await message.reply(f"<b>{prs}ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if not user_id:
        return await Tm.edit(
            f"<blockquote><b>{ggl}ʙᴇʀɪᴋᴀɴ ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʀsᴇʙᴜᴛ.</b></blockquote>"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
<blockquote><b><emoji id=5895665336220388986>📍</emoji>ᴜsᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ:</b>

🆔 <b>ᴜsᴇʀ ɪᴅ:</b> <code>{user.id}</code>
👤 <b>ꜰɪʀsᴛ ɴᴀᴍᴇ:</b> {first_name}
🗣️ <b>ʟᴀsᴛ ɴᴀᴍᴇ:</b> {last_name}
🌐 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> {username}
🏛️ <b>ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
🤖 <b>ɪs ʙᴏᴛ:</b> <code>{user.is_bot}</code>
🚷 <b>ɪs sᴄᴀᴍ:</b> <code>{user.is_scam}</code>
🚫 <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> <code>{user.is_restricted}</code>
✅ <b>ᴠᴇʀɪꜰɪᴇᴅ:</b> <code>{user.is_verified}</code>
⭐ <b>ᴘʀᴇᴍɪᴜᴍ:</b> <code>{user.is_premium}</code>
📝 <b>ᴜsᴇʀ ʙɪᴏ:</b> {bio}

👀 <b>sᴀᴍᴇ ɢʀᴏᴜᴘs sᴇᴇɴ:</b> {len(common)}
👁️ <b>ʟᴀsᴛ sᴇᴇɴ:</b> <code>{status}</code>
🔗 <b>ᴜsᴇʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ:</b> <a href=tg://user?id={user.id}>{fullname}</a></blockquote>
"""
        
        await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"ɪɴꜰᴏ: {e}")


@PY.UBOT("cinfo")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"<b>{prs}ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await Tm.edit(
                    f"<b>{ggl}ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪ ᴅᴀʟᴀᴍ ɢʀᴜᴘ ᴀᴛᴀᴜ ɢᴜɴᴀᴋᴀɴ <code>cinfo</code> [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ɪᴅ]</b>"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
<blockquote><b><emoji id=5895665336220388986>📍</emoji>ᴄʜᴀᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ:</b>

🆔 <b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat.id}</code>
👥 <b>ᴛɪᴛʟᴇ:</b> {chat.title}
👥 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> {username}
📩 <b>ᴛʏᴘᴇ:</b> <code>{type}</code>
🏛️ <b>ᴅᴄ ɪᴅ:</b> <code>{dc_id}</code>
🗣️ <b>ɪs sᴄᴀᴍ:</b> <code>{chat.is_scam}</code>
🎭 <b>ɪs ꜰᴀᴋᴇ:</b> <code>{chat.is_fake}</code>
✅ <b>ᴠᴇʀɪꜰɪᴇᴅ:</b> <code>{chat.is_verified}</code>
🚫 <b>ʀᴇsᴛʀɪᴄᴛᴇᴅ:</b> <code>{chat.is_restricted}</code>
🔰 <b>ᴘʀᴏᴛᴇᴄᴛᴇᴅ:</b> <code>{chat.has_protected_content}</code>

🚻 <b>ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs:</b> <code>{chat.members_count}</code>
📝 <b>ᴅᴇsᴄʀɪᴘᴛɪᴏɴ:</b> <code>{description}</code></blockquote>
"""
        
        await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"ɪɴꜰᴏ: `{e}`")


@PY.UBOT("id")
async def _(client, message):
    text = f"<blockquote><b><emoji id=5895665336220388986>📍</emoji>ᴍᴇssᴀɢᴇ ɪᴅ:</b> <code>{message.id}</code></blockquote>\n"

    if message.chat.type == ChatType.CHANNEL:
        text += f"<blockquote><b><emoji id=5895739888262713455>📍</emoji>ᴄʜᴀᴛ ɪᴅ:</b> <code>{message.sender_chat.id}</code></blockquote>\n"
    else:
        text += f"<blockquote><b><emoji id=5895739888262713455>📍</emoji>ʏᴏᴜʀ ɪᴅ:</b> <code>{message.from_user.id}</code></blockquote>\n\n"

        if len(message.command) > 1:
            try:
                user = await client.get_chat(message.text.split()[1])
                text += f"<blockquote><b><emoji id=5895739888262713455>📍</emoji>ᴜsᴇʀ ɪᴅ:</b> <code>{user.id}</code></blockquote>\n\n"
            except:
                return await message.reply("<blockquote><b><emoji id=6161479118413106534>❌</emoji>ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b></blockquote>")

        text += f"<blockquote><b><emoji id=5895739888262713455>📍</emoji>ᴄʜᴀᴛ ɪᴅ:</b> <code>{message.chat.id}</code></blockquote>\n\n"

    if message.reply_to_message:
        id_ = (
            message.reply_to_message.from_user.id
            if message.reply_to_message.from_user
            else message.reply_to_message.sender_chat.id
        )
        file_info = get_file_id(message.reply_to_message)
        if file_info:
            text += f"<blockquote><b><emoji id=5895665336220388986>📍</emoji>ᴍᴇᴅɪᴀ ɪᴅ:</b> <code>{file_info.file_id}</code></blockquote>\n\n"
        text += (
            f"<blockquote><b><emoji id=5895739888262713455>📍</emoji>ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:</b> <code>{message.reply_to_message.id}</code></blockquote>\n"
            f"<blockquote><b><emoji id=5895739888262713455>📍</emoji>ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:</b> <code>{id_}</code></blockquote>"
        )

    return await message.reply(text, disable_web_page_preview=True)


@PY.UBOT("setbio")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    tex = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    if len(message.command) == 1:
        return await tex.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴛᴇxᴛ]</b>")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴍᴇɴᴊᴀᴅɪ</b> <code>{bio}</code>")
        except Exception as e:
            await tex.edit(f"<b>{ggl}ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit(f"<b>{ggl}ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ</b>")


@PY.UBOT("setname")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    tex = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    if len(message.command) == 1:
        return await tex.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴛᴇxᴛ]</b>")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴍᴇɴᴊᴀᴅɪ</b> <code>{name}</code>"
            )
        except Exception as e:
            await tex.edit(f"<b>{ggl}ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit(f"<b>{ggl}ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ</b>")


@PY.UBOT("block")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
   
    user_id = await extract_user(message)
    tex = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    if not user_id:
        return await tex.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]</b>")
    if user_id == client.me.id:
        return await tex.edit(f"<blockquote><b>{brhsl}ᴏᴋ ᴅᴏɴᴇ</b></blockquote>")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<blockquote><b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴅɪʙʟᴏᴋɪʀ</b> {umention}</blockquote>")
  

@PY.UBOT("unblock")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
   
    user_id = await extract_user(message)
    tex = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    if not user_id:
        return await tex.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]</b>")
    if user_id == client.me.id:
        return await tex.edit(f"<blockquote><b>{brhsl}ᴏᴋ ᴅᴏɴᴇ.</b></blockquote>")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<blockquote><b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴅɪʙᴇʙᴀꜱᴋᴀɴ</b> {umention}</blockquote>")


