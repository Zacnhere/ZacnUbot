from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone
from PyroUbot.config import OWNER_ID
from PyroUbot import *



@PY.UBOT("rasacoklat")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    brhsl = await EMO.BERHASIL(client)
    user = message.from_user
    seller_id = await get_list_from_vars(bot.me.id, "SELER_USERS")
    if user.id not in seller_id:
        return
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply(f"{prs}<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if not user_id:
        return await msg.edit(f"{ggl}<b><code>{message.text}</code> ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(bot.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
 <blockquote><b>{ktrng} INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</b> <i>sudah premium{brhsl}</i>
 <b>ᴇxᴘɪʀᴇᴅ: <code>{get_bulan}</code> ʙᴜʟᴀɴ</b></blockquote>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(bot.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
 <blockquote><b>{ktrng} INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴇxᴘɪʀᴇᴅ: <code>{get_bulan}</code> ʙᴜʟᴀɴ</b>
 <b>ʙᴜᴀᴛ @{bot.me.username} </b></blockquote>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"<b>🆔 id-seller: {message.from_user.id}\n\n🆔 id-customer: {user_id}</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔱 seller",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "customer ⚜️", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unprem")
async def _(client, message):
    msg = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<b><code>{message.text}</code> ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(bot.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
 <blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>TIDAK ADA DALAM DAFTAR</code></b></blockquote>
"""
        )
    try:
        await remove_from_vars(bot.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
 <blockquote><b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>UNPREMIUM</code></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.UBOT("getprem")
async def _(client, message):
    user = message.from_user
    seller_id = await get_list_from_vars(bot.me.id, "SELER_USERS")
    if user.id not in seller_id:
        return
    prem = await get_list_from_vars(bot.me.id, "PREM_USERS")
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
            f"<b>📋 daftar premium:\n\n{prem_list_text}\n\n⚜️ total premium: {total_prem_users}</b>"
        )
    else:
        return await message.reply("<b>tidak ada pengguna premium saat ini</b>")


@PY.UBOT("addseles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    sudo_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>SUDAH SELLER</code></b>
"""
        )

    try:
        await add_to_vars(bot.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>SELLER</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unseles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>TIDAK DALAM DAFTAR SELLER</code></b>
"""
        )

    try:
        await remove_from_vars(bot.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
 <b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
 <b>ɪᴅ:</b> {user.id}
 <b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>UNSELLER</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getseles")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    brhsl = await EMO.BERHASIL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit(f"{ggl}<b>ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ ᴋᴏsᴏɴɢ</b>")

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
            f"<b>{ktrng} ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ:</b>\n\n"
            + "\n".join(seles_list)
            + f"\n\n<b>{brhsl} ᴛᴏᴛᴀʟ sᴇʟʟᴇʀ:</b> <code>{len(seles_list)}</code>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit(f"{ggl}<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀғᴛᴀʀ sᴇʟʟᴇʀ</b>")


@PY.UBOT("set_time")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Tm = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"{ggl}<b>ɢᴜɴᴀᴋᴀɴ <code>/set_time</code> ᴜsᴇʀ_ɪᴅ ʜᴀʀɪ</b>")
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
 <blockquote><b>{ktrng} INFORMATION</b>
 <b>ɴᴀᴍᴇ: {user.mention}</b>
 <b>ɪᴅ: {get_id}</b>
 <b>ᴀᴋᴛɪғᴋᴀɴ_sᴇʟᴀᴍᴀ: {get_day} ʜᴀʀɪ</b></blockquote>
"""
    )


@PY.UBOT("cek")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    brhsl = await EMO.BERHASIL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit(f"{ggl}<b>ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.ediit(error)
    if get_exp is None:
        await Sh.edit(f"{ggl}{user_id} <b>ʙᴇʟᴜᴍ ᴅɪᴀᴋᴛɪғᴋᴀɴ.</b>")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        await Sh.edit(f"""
 <blockquote><b>{ktrng} INFORMATION</b>
 <b>ɴᴀᴍᴇ: {sh.mention}</b>
 <b>ɪᴅ: {user_id}</b>
 <b>ᴘʀᴇғɪx: {' '.join(SH)}</b>
 <b>ᴀᴋᴛɪғ_ʜɪɴɢɢᴀ: {exp}</b></blockquote>
"""
        )


@PY.UBOT("addadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>SUDAH DALAM DAFTAR ADMIN</code></b>
"""
        )

    try:
        await add_to_vars(bot.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>ADMIN</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
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

    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>TIDAK DALAM DAFTAR ADMIN</code></b>
"""
        )

    try:
        await remove_from_vars(bot.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
<b>💬 INFORMATION</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: <code>UNADMIN</code></b>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply("<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if not admin_users:
        return await Sh.edit("<s>DAFTAR ADMIN KOSONG</s>")

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
        return await Sh.edit("<b>TIDAK DAPAT MENGAMBIL DAFTAR ADMIN</b>")

@PY.UBOT("addultra")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return await message.reply_text(f"{ggl}ᴍᴀᴜ ɴɢᴀᴘᴀɪɴ ᴋᴀᴍᴜ ?")
    msg = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl}<code>{message.text}</code> <b>ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")

    if user.id in ultra_users:
        return await msg.edit(f"""
<blockquote><b>{ktrng}💬 ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</b> {ggl}<b>sᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴜʟᴛʀᴀᴘʀᴇᴍ</b></blockquote>
"""
        )

    try:
        await add_to_vars(bot.me.id, "ULTRA_PREM", user.id)
        return await msg.edit(f"""
<blockquote><b>{ktrng}💬 ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</b> {brhsl}<b>ᴜʟᴛʀᴀᴘʀᴇᴍ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)

@PY.UBOT("rmultra")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    brhsl = await EMO.BERHASIL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return await message.reply_text(f"{ggl}ᴍᴀᴜ ɴɢᴀᴘᴀɪɴ ᴋᴀᴍᴜ ?")
    msg = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"{ggl}<b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")

    if user.id not in ultra_users:
        return await msg.edit(f"""
<blockquote><b>{ktrng} ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</b> {ggl}<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴜʟᴛʀᴀᴘʀᴇᴍ</b></blockquote>
"""
        )

    try:
        await remove_from_vars(bot.me.id, "ULTRA_PREM", user.id)
        return await msg.edit(f"""
<blockquote><b>{ktrng} ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>
<b>ɴᴀᴍᴇ:</b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
<b>ɪᴅ:</b> {user.id}
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ:</b> {brhsl}<b>ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴜʟᴛʀᴀᴘʀᴇᴍɪᴜᴍ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
