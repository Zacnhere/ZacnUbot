import asyncio

from pyrogram.enums import UserStatus

from PyroUbot import *

__MODULE__ = "invite"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ɪɴᴠɪᴛᴇ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}invite</code>
    <i>mengundang anggota ke group<i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}inviteall</code>
    <i>mengundang beberapa anggota dari group lain</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cancel</code>
    <i>membatalkan perintah inviteall</i>
    </blockquote>
   
"""


@PY.UBOT("invite")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    mg = await message.reply(f"<b>{prs}ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ!</b>")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            f"<b>{ggl}ʙᴇʀɪ sᴀʏᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜɴᴛᴜᴋ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!\nᴘᴇʀɪᴋsᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴꜰᴏ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ!</b>"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"<b>{brhsl}ʙᴇʀʜᴀsɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ {len(user_list)} ᴋᴇ ɢʀᴜᴘ ɪɴɪ</b>")



invite_id = []


@PY.UBOT("inviteall")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    Tm = await message.reply(f"<b>{prs}ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    if len(message.command) < 3:
        await message.delete()
        return await Tm.delete()
    try:
        chat = await client.get_chat(message.command[1])
    except Exception as error:
        return await Tm.edit(error)
    if message.chat.id in invite_id:
        return await Tm.edit_text(
            f"<b>{ggl}sᴇᴅᴀɴɢ ᴍᴇɴɢɪɴᴠɪᴛᴇ ᴍᴇᴍʙᴇʀ sɪʟᴀʜᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ɴᴀɴᴛɪ ᴀᴛᴀᴜ ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ: <code>cancel</code>"
        )
    else:
        done = 0
        failed = 0
        invite_id.append(message.chat.id)
        await Tm.edit_text(f"<b>{prs}ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ</b> {chat.title}")
        async for member in client.get_chat_members(chat.id):
            stats = [
                UserStatus.ONLINE,
                UserStatus.OFFLINE,
                UserStatus.RECENTLY,
                UserStatus.LAST_WEEK,
            ]
            if member.user.status in stats:
                try:
                    await client.add_chat_members(message.chat.id, member.user.id)
                    done = done + 1
                    await asyncio.sleep(int(message.command[2]))
                except Exception:
                    failed = failed + 1
                    await asyncio.sleep(int(message.command[2]))
        invite_id.remove(message.chat.id)
        await Tm.delete()
        return await message.reply(
            f"""
<b>{brhsl}<code>{done}</code> ᴀɴɢɢᴏᴛᴀ ʏᴀɴɢ ʙᴇʀʜᴀsɪʟ ᴅɪᴜɴᴅᴀɴɢ</b>
<b>{ggl}<code>{failed}</code> ᴀɴɢɢᴏᴛᴀ ʏᴀɴɢ ɢᴀɢᴀʟ ᴅɪᴜɴᴅᴀɴɢ</b>
"""
        )


@PY.UBOT("cancel")
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if message.chat.id not in invite_id:
        return await message.reply_text(
            f"<b>{ggl}sᴇᴅᴀɴɢ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇʀɪɴᴛᴀʜ: <code>inviteall</code></b>"
        )
    try:
        invite_id.remove(message.chat.id)
        await message.reply_text(f"<b>{brhsl}ᴘᴇʀɪɴᴛᴀʜ: <code>inviteall</code> ʙᴇʀʜᴀsɪʟ dibatalkan</b>")
    except Exception as e:
        await message.reply_text(e)
