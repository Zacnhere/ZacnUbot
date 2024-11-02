from PyroUbot import *

__MODULE__ = "sudo"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ sᴜᴅᴏ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addsudo</code>
   <i>menambahkan sudo user</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delsudo</code>
   <i>menghapus sudo user</i>
  
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}getsudo</code>
   <i>mendapatkan daftar sudo user</i>
   </blockquote> 
"""

@PY.UBOT("addsudo")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    msg = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl}<b><code>{message.text.split()[0]}</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ]</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id in sudo_users:
        return await msg.edit(
            f"{brhsl}<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>"
        )

    try:
        await add_to_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit(
            f"{brhsl}<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("delsudo")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    msg = await message.reply(f"<b>{prs}sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl}<b><code>{message.text.split()[0]}</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ]</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id not in sudo_users:
        return await msg.edit(
            f"{ggl}<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>"
        )

    try:
        await remove_from_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit(
            f"{brhsl}<b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ sᴜᴅᴏ</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getsudo")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    gcs = await EMO.BROADCAST(client)
    tion = await EMO.MENTION(client)
    Sh = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if not sudo_users:
        return await Sh.edit(f"{ggl}<b>ᴅᴀғᴛᴀʀ sᴜᴅᴏ ᴋᴏsᴏɴɢ</b>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(
                f"├ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>"
            )
        except:
            continue

    if sudo_list:
        response = (
            f"{gcs}<b> ᴅᴀғᴛᴀʀ sᴜᴅᴏ:</b>\n"
            + "\n".join(sudo_list)
            + f"\n{brhsl}<b> ᴛᴏᴛᴀʟ sᴜᴅᴏ:</b> <code>{len(sudo_list)}</code>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit(f"{ggl}<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ sᴜᴅᴏ sᴀᴀᴛ ɪɴɪ</b>")
