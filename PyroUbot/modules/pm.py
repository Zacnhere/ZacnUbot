import wget

from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent)

from PyroUbot import *


FLOOD = {}
MSG_ID = {}
PM_TEXT = """
<blockquote><b>🤖ʜᴀʟᴏ {mention} ᴀᴅᴀ ʏᴀɴɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ?

ᴘᴇʀᴋᴇɴᴀʟᴋᴀɴ sᴀʏᴀ ᴀᴅᴀʟᴀʜ ᴘᴍ-sᴇᴄᴜʀɪᴛʏ ᴅɪsɪɴɪ
sɪʟᴀʜᴋᴀɴ ᴛᴜɴɢɢᴜ ᴍᴀᴊɪᴋᴀɴ sᴀʏᴀ ᴍᴇᴍʙᴀʟᴀs ᴘᴇsᴀɴ ᴍᴜ ɪɴɪ ʏᴀ
ᴊᴀɴɢᴀɴ sᴘᴀᴍ ʏᴀ ᴀᴛᴀᴜ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴅɪ ʙʟᴏᴋɪʀ sᴇᴄᴀʀᴀ ᴏᴛᴏᴍᴀᴛɪs

⛔️ᴘᴇʀɪɴɢᴀᴛᴀɴ: {warn} ʜᴀᴛɪ-ʜᴀᴛɪ</b></blockquote>
"""


__MODULE__ = "pmpermit"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴘᴍ ᴘᴇʀᴍɪᴛ 』</b> </blockquote>  
 <blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}nopc</code>
    <i>menghapus pesan baru dari semua pengguna</i>
 
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pmpermit</code>
    <i>mengaktifkan atau menonaktifkan pm permit</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ok</code>
    <i>mengizinkan seseorang untuk pm anda</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}no</code>
    <i>menolak seseorang untuk pm anda</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setpm</code>
    <i>mengatur configuration pada pm_permit</i>

 <b>ǫᴜᴇʀʏ:</b>
   ● <code>pic</code>
   ● <code>text</code>
   ● <code>limit</code>
   </blockquote>
"""


@PY.NO_CMD_UBOT("PMPERMIT", ubot)
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
  
    user = message.from_user
    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if pm_on:
        if user.id in MSG_ID:
            await delete_old_message(message, MSG_ID.get(user.id, 0))
        check = await get_pm_id(client.me.id)
        if user.id not in check:
            if user.id in FLOOD:
                FLOOD[user.id] += 1
            else:
                FLOOD[user.id] = 1
            pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"
            try:
                if FLOOD[user.id] > int(pm_limit):
                    del FLOOD[user.id]
                    await message.reply(
                        "<b>sᴜᴅᴀʜ ᴅɪɪɴɢᴀᴛᴋᴀɴ ᴊᴀɴɢᴀɴ sᴘᴀᴍ, sᴇᴋᴀʀᴀɴɢ Aɴᴅᴀ ᴅɪʙʟᴏᴋɪʀ.</b>"
                    )
                    return await client.block_user(user.id)
            except ValueError:
                await set_vars(client.me.id, "PM_LIMIT", "5")
            pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT
            if "~>" in pm_msg:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"pm_pr {id(message)} {FLOOD[user.id]}"
                )
                msg = await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=message.id,
                )
                MSG_ID[user.id] = int(msg.updates[0].id)
            else:
                try:
                    pm_pic = await get_vars(client.me.id, "PM_PIC")
                    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
                    peringatan = f"{FLOOD[user.id]} / {pm_limit}"
                    if pm_pic:
                        try:
                            msg = await message.reply_photo(
                                pm_pic, caption=pm_msg.format(mention=rpk, warn=peringatan)
                            )
                        except ValueError:
                            await set_vars(client.me.id, "PM_PIC", False)
                    else:
                        msg = await message.reply(
                            pm_msg.format(mention=rpk, warn=peringatan)
                        )
                    MSG_ID[user.id] = msg.id
                except UnboundLocalError:
                    pass


@PY.UBOT("setpm")
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ǫᴜᴇʀʏ] [ᴠᴀʟᴜᴇ]</b>"
        )
    query = {"limit": "PM_LIMIT", "text": "PM_TEXT", "pic": "PM_PIC"}
    if message.command[1].lower() not in query:
        return await message.reply(f"{ggl}<b>ǫᴜᴇʀʏ ʏᴀɴɢ ᴅɪ ᴍᴀsᴜᴋᴋᴀɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ</b>")
    query_str, value_str = (
        message.text.split(None, 2)[1],
        message.text.split(None, 2)[2],
    )
    value = query[query_str]
    if value_str.lower() == "none":
        value_str = False
    await set_vars(client.me.id, value, value_str)
    return await message.reply(
        f"{brhsl}<b>ᴘᴍᴘᴇʀᴍɪᴛ ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ</b>"
    )


@PY.UBOT("pmpermit")
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴏɴ/ᴏғғ]</b>"
        )

    toggle_options = {"off": False, "on": True}
    toggle_option = message.command[1].lower()

    if toggle_option not in toggle_options:
        return await message.reply(f"{ggl}<b>ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. Hᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'.</b>")

    value = toggle_options[toggle_option]
    text = "ᴅɪᴀᴋᴛɪғᴋᴀɴ" if value else "ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ"

    await set_vars(client.me.id, "PMPERMIT", value)
    await message.reply(f"<b>{brhsl}ᴘᴍᴘᴇʀᴍɪᴛ ʙᴇʀʜᴀsɪʟ {text}</b>")


@PY.INLINE("pm_pr")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    m = [obj for obj in get_objects() if id(obj) == int(get_id[1])][0]
    pm_msg = await get_vars(m._client.me.id, "PM_TEXT") or PM_TEXT
    pm_limit = await get_vars(m._client.me.id, "PM_LIMIT") or 5
    pm_pic = await get_vars(m._client.me.id, "PM_PIC")
    rpk = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    peringatan = f"{int(get_id[2])} / {pm_limit}"
    buttons, text = await pmpermit_button(pm_msg)
    if pm_pic:
        photo_video = InlineQueryResultVideo if pm_pic.endswith(".mp4") else InlineQueryResultPhoto
        photo_video_url = {"video_url": pm_pic, "thumb_url": pm_pic} if pm_pic.endswith(".mp4") else {"photo_url": pm_pic}
        hasil = [
            photo_video(
                **photo_video_url,
                title="Dapatkan tombol!",
                caption=text.format(mention=rpk, warn=peringatan),
                reply_markup=buttons,
            )
        ]
    else:
        hasil = [
            (
                InlineQueryResultArticle(
                    title="Dapatkan tombol!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text.format(mention=rpk, warn=peringatan)),
                )
            )
        ]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=hasil,
    )


@PY.UBOT("ok|terima")
@PY.PRIVATE
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
  
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await add_pm_id(client.me.id, user.id)
        return await message.reply(f"<b>{brhsl}ʙᴀɪᴋʟᴀʜ, {rpk} ᴛᴇʟᴀʜ ᴅɪᴛᴇʀɪᴍᴀ</b>")
    else:
        return await message.reply(f"<b>{brhsl}{rpk} sᴜᴅᴀʜ ᴅɪᴛᴇʀɪᴍᴀ</b>")


@PY.UBOT("no|tolak")
@PY.PRIVATE
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await message.reply(f"<b>{ggl}🙏🏻 ᴍᴀᴀғ ⁣{rpk} ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪʙʟᴏᴋɪʀ</b>")
        return await client.block_user(user.id)
    else:
        await remove_pm_id(client.me.id, user.id)
        return await message.reply(
            f"<b>{ggl}🙏🏻 ᴍᴀᴀғ {rpk} ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪᴛᴏʟᴀᴋ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴋᴜɴ ɪɴɪ ʟᴀɢɪ</b>"
        )

async def pmpermit_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    for X in m.split("~>", 1)[1].split():
        X_parts = X.split(":", 1)
        keyboard.append(InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1]))
    buttons.add(*keyboard)
    text = m.split("~>", 1)[0]

    return buttons, text


async def delete_old_message(message, msg_id):
    try:
        await message._client.delete_messages(message.chat.id, msg_id)
    except:
        pass

@NO_PC("NOPC", ubot)
async def _(client, message):
    user = message.from_user
    nopm_on = await get_vars(client.me.id, "NOPM_STATUS")  # Ambil status NoPM dari database
    datanya = await get_list_from_vars(client.me.id, "BL_ID")
    if nopm_on:
          if user.id not in datanya:
              await client.delete_messages(message.chat.id, message.id)
              return


@PY.UBOT("nopc")
async def toggle_nopm(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    # Validate command length
    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴏɴ/ᴏғғ]</b>"
        )

    # Parse and validate toggle option
    toggle_options = {"off": False, "on": True}
    toggle_option = message.command[1].lower()

    if toggle_option not in toggle_options:
        return await message.reply(
            f"{ggl}ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'."
        )

    value = toggle_options[toggle_option]
    text = "ᴀᴋᴛɪғᴋᴀɴ" if value else "ɴᴏɴᴀᴋᴛɪғᴋᴀɴ"

    # Set NoPM status in database
    try:
        await set_vars(client.me.id, "NOPM_STATUS", value)
        await message.reply(f"<b>{brhsl}ᴀɴᴛɪ ᴘᴄ ᴅɪ{text}</b>")
    except Exception as e:
        return await message.reply(
            f"{ggl}Gagal menyimpan status NoPM: {str(e)}"
        )
