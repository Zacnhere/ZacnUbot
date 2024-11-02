from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone


from PyroUbot import *



@PY.BOT("prem")
@PY.SELLER
async def _(client, message):
    
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply(f"<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if not user_id:
        return await msg.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
 <blockquote><b>INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</b> <code>sudah premium</code>
 <b>ᴇxᴘɪʀᴇᴅ: <code>{get_bulan}</code> ʙᴜʟᴀɴ</b></blockquote>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(client.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
 <blockquote><b>INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>premium</code></b>
 <b>ᴇxᴘɪʀᴇᴅ: <code>{get_bulan}</code> ʙᴜʟᴀɴ</b></blockquote>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"<b>🆔 ɪᴅ-sᴇʟʟᴇʀ: {message.from_user.id}\n\n🆔 ɪᴅ-ᴄᴜsᴛᴏᴍᴇʀ: {user_id}</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 sᴇʟʟᴇʀ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "ᴄᴜsᴛᴏᴍᴇʀ ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unprem")
@PY.SELLER
async def _(client, message):
    
    msg = await message.reply(f"<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(client.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
 <blockquote><b>INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>tidak dalam daftar</code></b></blockquote>
"""
        )
    try:
        await remove_from_vars(bot.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
 <blockquote><b>INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>unpremium</code></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.BOT("getprem")
@PY.SELLER
async def _(client, message):
    prem = await get_list_from_vars(client.me.id, "PREM_USERS")
    prem_users = []

    for user_id in prem:
        try:
            user = await client.get_users(user_id)
            prem_users.append(
                f"<b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></b>"
            )
        except Exception as error:
            return await message.reply(str(error))

    total_prem_users = len(prem_users)
    if prem_users:
        prem_list_text = "\n".join(prem_users)
        return await message.reply(
            f"<b>📋 ᴅᴀғᴛᴀʀ ᴘʀᴇᴍɪᴜᴍ:\n\n{prem_list_text}\n\n⚜️ ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ: {total_prem_users}</b>"
        )
    else:
        return await message.reply("<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ᴘʀᴇᴍɪᴜᴍ sᴀᴀᴛ ɪɴɪ</b>")


@PY.BOT("addseles")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
 <blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>sudah seller</code></b></blockquote>
"""
        )

    try:
        await add_to_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
 <blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>seller</code></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unseles")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
<blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>tidak dalam daftar</code></b></blockquote>
"""
        )

    try:
        await remove_from_vars(client.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>unseller</code></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getseles")
@PY.ADMIN
async def _(client, message):
    
    Sh = await message.reply(f"<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    seles_users = await get_list_from_vars(client.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit(f"<b>ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ ᴋᴏsᴏɴɢ</b>")

    seles_list = []
    for user_id in seles_users:
        try:
            user = await client.get_users(int(user_id))
            seles_list.append(
                f"<b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></b>"
            )
        except:
            continue

    if seles_list:
        response = (
            f"<b> ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ:</b>\n\n"
            + "\n".join(seles_list)
            + f"\n\n<b> ᴛᴏᴛᴀʟ sᴇʟʟᴇʀ:</b> <code>{len(seles_list)}</code>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ</b>")


@PY.BOT("set_time")
@PY.SELLER
async def _(client, message):
    
    Tm = await message.reply(f"<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"<b>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ /set_time ᴜsᴇʀ_ɪᴅ ʜᴀʀɪ</b>")
    user_id = int(bajingan[1])
    get_day = int(bajingan[2])
    print(user_id , get_day)
    try:
        get_id = (await client.get_users(user_id)).id
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"""
 <blockquote><b> INFORMATION</b>
 <b>ɴᴀᴍᴇ: {user.mention}</b>
 <b>ɪᴅ: {get_id}</b>
 <b>ᴀᴋᴛɪғᴋᴀɴ_sᴇʟᴀᴍᴀ: {get_day} ʜᴀʀɪ</b></blockquote>
"""
    )

# async def _(client, message):
    # Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    # user_id, get_day = await extract_user_and_reason(message)
    # if not user_id:
        # return await Tm.edit(f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʜᴀʀɪ</b>")
    # try:
        # get_id = (await client.get_users(user_id)).id
        # user = await client.get_users(user_id)
    # except Exception as error:
        # return await Tm.edit(error)
    # if not get_day:
        # get_day = 30
    # now = datetime.now(timezone("Asia/Jakarta"))
    # expire_date = now + timedelta(days=int(get_day))
    # await set_expired_date(user_id, expire_date)
    # await Tm.edit(f"""
# <b>💬 INFORMATION</b>
 # <b>ɴᴀᴍᴇ: {user.mention}</b>
 # <b>ɪᴅ: {get_id}</b>
 # <b>ᴀᴋᴛɪғᴋᴀɴ_sᴇʟᴀᴍᴀ: {get_day} ʜᴀʀɪ</b>
# """
    # )


@PY.BOT("cek")
@PY.SELLER
async def _(client, message):
    Sh = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.ediit(error)
    if get_exp is None:
        await Sh.edit(f"{user_id} ʙᴇʟᴜᴍ ᴅɪᴀᴋᴛɪғᴋᴀɴ.")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        await Sh.edit(f"""
 <blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ: {sh.mention}</b>
 <b>ɪᴅ: {user_id}</b>
 <b>ᴘʀᴇғɪx: {' '.join(SH)}</b>
 <b>ᴀᴋᴛɪғ_ʜɪɴɢɢᴀ: {exp}</b></blockquote>
"""
        )


@PY.BOT("addadmin")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>sudah dalam daftar</code></b>
"""
        )

    try:
        await add_to_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>admin</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("unadmin")
@PY.OWNER
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>tidak daam daftar</code></b>
"""
        )

    try:
        await remove_from_vars(client.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>unadmin</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.BOT("getadmin")
@PY.OWNER
async def _(client, message):
    Sh = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if not admin_users:
        return await Sh.edit("<s>ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ ᴋᴏsᴏɴɢ</s>")

    admin_list = []
    for user_id in admin_users:
        try:
            user = await client.get_users(int(user_id))
            admin_list.append(
                f"<b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code></b>"
            )
        except:
            continue

    if admin_list:
        response = (
            "<b>📋 ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ:</b>\n\n"
            + "\n".join(admin_list)
            + f"\n\n<b>⚜️ ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴ:</b> <code>{len(admin_list)}</code>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ</b>")

