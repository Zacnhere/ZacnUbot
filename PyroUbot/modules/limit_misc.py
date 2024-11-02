import asyncio
import os
import requests
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from PyroUbot import *

__MODULE__ = "limit"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ʟɪᴍɪᴛ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}limit</code>
    <i>mengecek status akun apakah terkena limit atau tidak</i>
    </blockquote>
"""

@PY.UBOT("limit")
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    tion = await EMO.MENTION(client)
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
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
    if status and hasattr(status, "text"):
        pjg = len(status.text)
        if pjg <= 100:
            text=status.text
            await client.send_message(message.chat.id, f"<blockquote><i><b>{tion}{text}</b></i></blockquote>", reply_to_message_id=message.id)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            text=status.text
            await client.send_message(message.chat.id, f"<blockquote><i><b>{tion}{text}</b></i></blockquote>", reply_to_message_id=message.id)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
