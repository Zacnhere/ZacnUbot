from pyrogram import Client
from pyrogram import errors
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate

from pyrogram import *
from PyroUbot import *

__MODULE__ = "joinleave"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴊᴏɪɴʟᴇᴀᴠᴇ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kickme</code>
    <i>keluar dari group</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}join</code>
    <i>join ke group melalui tautan atau username group</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leaveallmute</code>
    <i>keluar dari group yang di batasi</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leaveallgc</code>
    <i>keluar semua dari group</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leaveallch</code>
    <i>keluar semua dari channel</i>
    </blockquote>

"""


@PY.UBOT("kickme")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"<b>{prs}ᴘʀᴏꜱᴇꜱ...</b>")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(f"<b>{ktrng}ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ</b>")
    try:
        await xxnx.edit_text(f"{brhsl}{client.me.first_name} <b>ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ ɪɴɪ, ʙʏᴇ!!</b>")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")



@PY.UBOT("join")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(f"<b>{prs}ᴘʀᴏꜱᴇꜱ...</b>")
    try:
        await xxnx.edit(f"<b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴄʜᴀᴛ ɪᴅ: <code>{Man}</code></b>")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")


@PY.UBOT("leaveallgc")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    Man = await message.reply(f"<b>{prs}ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴏᴜᴘ...</b>")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"<b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ <code>{done}</code> ɢʀᴏᴜᴘ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ <code>{er}</code> ɢʀᴏᴜᴘ</b>"
    )


@PY.UBOT("leaveallch")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    Man = await message.reply(f"<b>{prs}ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ...</b>")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"<b>{brhsl}ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ <code>{done}</code> ᴄʜᴀɴɴᴇʟ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ <code>{er}</code> ᴄʜᴀɴɴᴇʟ</b>"
    )

@PY.UBOT("leaveallmute")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    done = 0
    Man = await message.reply(f"<b>{prs}ᴘʀᴏꜱᴇꜱ...</b>")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat)
                    done += 1
            except Exception:
                pass
    await Man.edit(f"<blockquote><i>{ktrng}**ʟᴇᴀᴠᴇᴀʟʟ ᴍᴜᴛᴇ ʙᴇʀʜᴀsɪʟ\n{brhsl}sᴜᴋsᴇs <code>{done}</code> ɢʀᴏᴜᴘ\n{ggl}ɢᴀɢᴀʟ <code>0</code> ɢʀᴏᴜᴘ**</i></blockquote>")
    
    

