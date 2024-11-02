from PyroUbot import *
from pyrogram import enums
from pyrogram.enums import ChatType

__MODULE__ = "archive"
__HELP__ = """
<blockquote>
<b> 『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʀᴄʜɪᴠᴇ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}arch</code>
    <i>meng archive kan group/chat/pribadi/bot/dan channel</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unarch</code>
    <i>meng unarchive kan group/chat/pribadi/bot/dan channel</i>

<b>➢ ᴛʏᴘᴇ: </b>
     ● <code>group</code>
     ● <code>private</code>
     ● <code>channel</code>
     ● <code>bot</code>
     </blockquote>

"""


async def get_data_id(client, query):
    chat_types = {
        "channel": [ChatType.CHANNEL],
        "bot": [ChatType.BOT],
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "private": [ChatType.PRIVATE],
    }
    return [dialog.chat.id async for dialog in client.get_dialogs() if dialog.chat.type in chat_types.get(query, [])]

@PY.UBOT("arch")
async def archive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) <2:
        return await message.reply(f"{ggl}ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴀʀᴄʜ ᴛʏᴘᴇ")
    anjai = await message.reply(f"{prs}ᴘʀᴏᴄᴄᴇsɪɴɢ...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.archive_chats(anu)
    
    await anjai.edit(f"{brhsl}ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀʀᴄʜɪᴠᴇᴋᴀɴ sᴇᴍᴜᴀ {anjir}")

@PY.UBOT("unarch")
async def unarchive_user(client, message):
    if len(message.command) <2:
        return await message.reply(f"{ggl}ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ᴜɴᴀʀᴄʜ ᴛʏᴘᴇ")
    anjai = await message.reply(f"{prs}ᴘʀᴏᴄᴄᴇsɪɴɢ...")
    anjir = message.command[1]
    xx = await get_data_id(client, anjir)
    for anu in xx:
        await client.unarchive_chats(anu)
    
    await anjai.edit(f"{brhsl}ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴜɴᴀʀᴄʜɪᴠᴇᴋᴀɴ sᴇᴍᴜᴀ {anjir}")
