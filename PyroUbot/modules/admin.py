import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    ChatNotModified,
)

from PyroUbot import *


__MODULE__ = "admin"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴀᴅᴍɪɴ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kick</code>
   <i>menendang anggota dari group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}|mute |unmute</code>
   <i>membisukan dan melepas pembisuan anggota group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}|ban |unban</code>
   <i>memblokir dan melepas blokiran anggota group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}zombies</code>
   <i>mengeluarkan akun terhapus dari group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}|pin |unpin</code>
<i>memasang dan melepas sematan pesan di group/chat</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}|lock |unlock</code>
   <i>mengunci dan membuka izin group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}locks</code>
   <i>melihat izin pada group saat ini</i>

  <b>ᴛʏᴘᴇ:</b>
   <code>|msg |media |stickers |polls |info</code>
   <code>|invite |webprev |pin</code>
   </blockquote>
"""


data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}


async def current_chat_permissions(client, chat_id):
    perms = []
    perm = (await client.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_other_messages:
        perms.append("can_send_other_messages")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")
    return perms


async def tg_lock(
    client,
    message,
    parameter,
    permissions: list,
    perm: str,
    lock: bool,
):
    if lock:
        if perm not in permissions:
            return await message.reply(f"<emoji id=5021905410089550576>✅</emoji>`{parameter}` <b>ꜱᴜᴅᴀʜ ᴛᴇʀᴋᴜɴᴄɪ</b>")
        permissions.remove(perm)
    else:
        if perm in permissions:
            return await message.reply(f"<emoji id=5021905410089550576>✅</emoji>`{parameter}` <b>ꜱᴜᴅᴀʜ ᴛᴇʀʙᴜᴋᴀ</b>")
        permissions.append(perm)
    permissions = {perm: True for perm in set(permissions)}
    try:
        await client.set_chat_permissions(
            message.chat.id, ChatPermissions(**permissions)
        )
    except ChatNotModified:
        return await message.reply(
            f"<emoji id=5021905410089550576>✅</emoji><code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ]</b>"
        )
    except ChatAdminRequired:
        return await message.reply("<b><emoji id=6161479118413106534>❌</emoji>ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ɪᴢɪɴ</b>")
    await message.reply(
        (
            f"<b><emoji id=5021905410089550576>✅</emoji>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ: <code>{parameter}</code>\nɢʀᴜᴘ: {message.chat.title}</b>"
            if lock
            else f"<b><emoji id=5021905410089550576>✅</emoji>ᴛᴇʀʙᴜᴋᴀ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\nᴛɪᴘᴇ: <code>{parameter}</code>\nɢʀᴜᴘ: {message.chat.title}</b>"
        )
    )


@PY.UBOT("lock|unlock")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    grp = await EMO.BL_GROUP(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    if len(message.command) != 2:
        return await message.reply(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ]</b>")
    chat_id = message.chat.id
    parameter = message.text.strip().split(None, 1)[1].lower()
    state = message.command[0].lower()
    if parameter not in data and parameter != "all":
        return await message.reply(incorrect_parameters)
    permissions = await current_chat_permissions(client, chat_id)
    if parameter in data:
        await tg_lock(
            client,
            message,
            parameter,
            permissions,
            data[parameter],
            bool(state == "lock"),
        )
    elif parameter == "all" and state == "lock":
        try:
            await client.set_chat_permissions(chat_id, ChatPermissions())
            await message.reply(
                f"<blockquote>{brhsl}<b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\n{ktrng}ᴛɪᴘᴇ: <code>{parameter}</code>\n{grp}ɢʀᴜᴘ: {message.chat.title}</b></blockquote>"
            )
        except ChatAdminRequired:
            return await message.reply(f"<blockquote>{ggl}<b>ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ɪᴢɪɴ</b></blockquote>")
        except ChatNotModified:
            return await message.reply(
                f"<blockquote>{brhsl}<b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\n{ktrng}ᴛɪᴘᴇ: <code>{parameter}</code>\n{grp}ɢʀᴜᴘ: {message.chat.title}</b></blockquote>"
            )
    elif parameter == "all" and state == "unlock":
        try:
            await client.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False,
                ),
            )
        except ChatAdminRequired:
            return await message.reply(f"<blockquote>{ggl}<b>ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴜɴʏᴀɪ ɪᴢɪɴ</b></blockquote>")
        await message.reply(
            f"<blockquote>{brhsl}<b>ᴛᴇʀʙᴜᴋᴀ ᴜɴᴛᴜᴋ ɴᴏɴ-ᴀᴅᴍɪɴ!\n{ktrng}ᴛɪᴘᴇ: <code>{parameter}</code>\n{grp}ɢʀᴜᴘ: {message.chat.title}</b></blockquote>"
        )


@PY.UBOT("locks")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    permissions = await current_chat_permissions(client, message.chat.id)
    if not permissions:
        return await message.reply(f"<blockquote>{brhsl}<b>ᴛᴇʀᴋᴜɴᴄɪ ᴜɴᴛᴜᴋ ꜱᴇᴍᴜᴀ</b></blockquote>")

    perms = " -> __**" + "\n -> __**".join(permissions) + "**__"
    await message.reply(perms)


@PY.UBOT("pin|unpin")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if not message.reply_to_message:
        return await message.edit(f"<blockquote><b>{ggl}ʀᴇᴘʟʏ ᴛᴇxᴛ</b></blockquote>")
    r = message.reply_to_message
    await message.edit(f"{prs}<b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b>")
    if message.command[0][0] == "u":
        await r.unpin()
        return await message.edit(
            f"<blockquote><b>{brhsl}ᴜɴᴘɪɴɴᴇᴅ</b> [ᴛʜɪꜱ]({r.link}) <b>ᴍᴇꜱꜱᴀɢᴇ</b></blockquote>",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await message.edit(
            f"<blockquote><b>{brhsl}ᴘɪɴɴᴇᴅ</b> [ᴛʜɪꜱ]({r.link}) <b>ᴍᴇꜱꜱᴀɢᴇ</b></blockquote>",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        await message.edit(f"<blockquote><b>{ggl}ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ɢʀᴏᴜᴘ ɪɴɪ!</b></blockquote>")
        await message.delete()


@PY.UBOT("kick|ban|mute|unmute|unban")
@PY.GROUP
async def _(client, message):
    tion = await EMO.MENTION(client)
    ggl = await EMO.GAGAL(client)
    grp = await EMO.BL_GROUP(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    brhsl = await EMO.BERHASIL(client)
    if message.command[0] == "kick":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text(f"<blockquote>{ggl}<code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>")
        if user_id == OWNER_ID:
            return await message.reply_text(f"<blockquote><b>{ggl}ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ</b></blockquote>")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                f"<blockquote><b>{ggl}sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ</b></blockquote>"
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg_kick = f"""
<blockquote><b>{ggl}ᴡᴀʀɴɪɴɢ:</b> {mention}
<b>{tion}ᴀᴅᴍɪɴ:</b> {message.from_user.mention}
<b>{ktrng}ᴀʟᴀsᴀɴ:</b> {reason}</blockquote>
            """
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg_kick)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "ban":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text(f"<blockquote>{ggl}<code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>")
        if user_id == OWNER_ID:
            return await message.reply_text(f"<blockquote><b>{ggl}ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ</b></blockquote>")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                f"<blockquote>{ggl}<b>sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ</b></blockquote>"
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg_ban = f"""
<blockquote><b>{ggl}ᴡᴀʀɴɪɴɢ:</b> {mention}
<b>{tion}ᴀᴅᴍɪɴ:</b> {message.from_user.mention}
<b>{ktrng}ᴀʟᴀsᴀɴ:</b> {reason}</blockquote>
            """
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg_ban)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "mute":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text(f"<blockquote>{ggl}<code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>")
        if user_id == OWNER_ID:
            return await message.reply_text(f"<blockquote>{ggl}<b>ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ</b></blockquote>")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                f"<blockquote>{ggl}<b>sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀᴅᴍɪɴ</b></blockquote>"
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg_mute = f"""
<blockquote><b>{ggl}ᴡᴀʀɴɪɴɢ:</b> {mention}
<b>{tion}ᴀᴅᴍɪɴ:</b> {message.from_user.mention}
<b>{ktrng}ᴀʟᴀsᴀɴ:</b> {reason}</blockquote>
            """
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
            await message.reply(msg_mute)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unmute":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text(f"<blockquote>{ggl}<code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<blockquote>{brhsl}{mention} <b>sᴜᴅᴀʜ ʙɪsᴀ ᴄʜᴀᴛ ʟᴀɢɪ</b></blockquote>")
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unban":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text(f"<blockquote>{ggl}<code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<blockquote>{brhsl}{mention} <b>sᴜᴅᴀʜ ʙɪsᴀ ᴊᴏɪɴ ʟᴀɢɪ</b></blockquote>")
        except Exception as error:
            await message.reply(error)


@PY.UBOT("zombies")
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    chat_id = message.chat.id
    deleted_users = []
    banned_users = 0
    Tm = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴇʀɪᴋsᴀ</b>")
    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                banned_users += 1
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
        await Tm.edit(f"<blockquote>{brhsl}<b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴇʟᴜᴀʀᴋᴀɴ {banned_users} ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs</b></blockquote>")
    else:
        await Tm.edit(f"<blockquote>{ggl}<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ</b></blockquote>")
