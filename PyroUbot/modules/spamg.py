import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from .. import *

__MODULE__ = "spamg"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ sᴘᴀᴍɢ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spam</code>
   <i>melakukan spam pesan</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spamg</code>
   <i>melakukan spam gcast ke seluruh group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setdelay</code>
   <i>mengatur delay setiap pesan yang di kirim</i>
   </blockquote>  
"""


async def SpamMsg(client, message, send):
    delay = await get_vars(client.me.id, "SPAM") or 0
    await asyncio.sleep(int(delay))
    if message.reply_to_message:
        await send.copy(message.chat.id)
    else:
        await client.send_message(message.chat.id, send)


async def SpamGcast(client, message, send):
    blacklist = await get_list_from_vars(client.me.id, "BL_ID")

    async def send_message(target_chat):
        await asyncio.sleep(0.1)
        if message.reply_to_message:
            await send.copy(target_chat)
        else:
            await client.send_message(target_chat, send)

    async def handle_flood_wait(exception, target_chat):
        await asyncio.sleep(exception.value)
        await send_message(target_chat)

    async for dialog in client.get_dialogs():
        if (
            dialog.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP}
            and dialog.chat.id not in blacklist
        ):
            try:
                await send_message(dialog.chat.id)
            except FloodWait as e:
                await handle_flood_wait(e, dialog.chat.id)
            except Exception:
                pass


@PY.UBOT("spam")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴊᴜᴍʟᴀʜ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ]</b>")

    if not msg:
        return await r.edit(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴊᴜᴍʟᴀʜ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ]</b>"
        )
    
    for _ in range(count):
        await SpamMsg(client, message, msg)
    
    await r.edit(f"<b>{brhsl}sᴘᴀᴍ ᴛᴇʟᴀʜ sᴇʟᴇsᴀɪ</b>")


@PY.UBOT("spamg")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴊᴜᴍʟᴀʜ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ]</b>")

    if not msg:
        return await r.edit(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴊᴜᴍʟᴀʜ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ]</b>"
        )

    async def run_spam():
        spam_gcast = [SpamGcast(client, message, msg) for _ in range(int(count))]
        await asyncio.gather(*spam_gcast)

    await run_spam()
    return await r.edit(f"<blockquote><b>{brhsl}SᴘᴀᴍG ᴛᴇʟᴀʜ sᴇʟᴇsᴀɪ ᴅɪʟᴀᴋᴜᴋᴀɴ</b></blockquote>")


@PY.UBOT("setdelay")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    _msg = f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>"

    r = await message.reply(_msg)
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await r.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴄᴏᴜɴᴛ]</b>")

    if not count:
        return await r.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>[ᴄᴏᴜɴᴛ]</b>")

    await set_vars(client.me.id, "SPAM", count)
    return await r.edit(f"<b>{brhsl}sᴘᴀᴍ ᴅᴇʟᴀʏ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ</b>")
