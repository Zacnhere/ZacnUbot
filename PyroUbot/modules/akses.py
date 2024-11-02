from PyroUbot import *

@PY.UBOT("ultraprem")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    msg = await message.reply(f"<b>{prs}ᴘʀᴏᴄᴇssɪɴɢ...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl} <code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ]</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    akses_users = await get_list_from_vars(client.me.id, "AKSES_USERS")

    if user.id in akses_users:
        return await msg.edit(
            f"{ggl}[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) <b>sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀᴋsᴇs</b>"
        )

    try:
        await add_to_vars(client.me.id, "AKSES_USERS", user.id)
        return await msg.edit(
            f"{brhsl}[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) <b>ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ᴀᴋsᴇs</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("delultra")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    msg = await message.reply(f"<b>{prs}ᴘʀᴏᴄᴇssɪɴɢ...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl} <code>{message.text.split()[0]}</code> <b>[ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ]</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    akses_users = await get_list_from_vars(client.me.id, "AKSES_USERS")

    if user.id not in akses_users:
        return await msg.edit(
            f"{ggl}[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) <b>ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀᴋsᴇs</b>"
        )

    try:
        await remove_from_vars(client.me.id, "AKSES_USERS", user.id)
        return await msg.edit(
            f"{brhsl}[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) <b>ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴀᴋsᴇs</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getultraprem")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    Sh = await message.reply("<b>{prs}ᴘʀᴏᴄᴇssɪɴɢ...</b>")
    akses_users = await get_list_from_vars(client.me.id, "AKSES_USERS")

    if not akses_users:
        return await Sh.edit(f"{ggl}<b>ᴅᴀғᴛᴀʀ ᴀᴋsᴇs ᴋᴏsᴏɴɢ</b>")

    akses_list = []
    for user_id in akses_users:
        try:
            user = await client.get_users(int(user_id))
            akses_list.append(
                f"├ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}"
            )
        except:
            continue

    if akses_list:
        response = (
            f"{brhsl} <b>ᴅᴀғᴛᴀʀ ᴀᴋsᴇs:</b>\n"
            + "\n".join(akses_list)
            + f"\n{ktrng} <b>ᴛᴏᴛᴀʟ ᴀᴋsᴇs:</b> {len(akses_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ ᴀᴋsᴇs sᴀᴀᴛ ɪɴɪ</b>")
