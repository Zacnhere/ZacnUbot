import os
import json
import asyncio
import psutil


from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw import *
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *



@PY.CALLBACK("stats")
async def _(client, callback_query):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    delta_ping_formatted = round(delta_ping, 3)
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    buttons = [
        [InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="kontol")],
        [InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data="balik")],
    ]
    _ping = f"""
<b>🖥️ [SYSTEM UBOT]
PING: {str(delta_ping_formatted).replace('.', ',')} ms
UBOT: {len(ubot._ubot)} user
UPTIME: {uptime}
OWNER: None</b>

<b>📊 [STATUS SERVER]
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
MEMORY: {round(process.memory_info()[0] / 1024 ** 2)} MB</b>
"""
    await callback_query.message.edit(_ping, reply_markup=InlineKeyboardMarkup(buttons))


@PY.CALLBACK("kontol")
async def _(client, callback_query):
    await callback_query.answer("ʀᴇғʀᴇsʜɪɴɢ...")
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    delta_ping_formatted = round(delta_ping, 3)
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    _ping = f"""
<b>🖥️ [SYSTEM UBOT]
PING: {str(delta_ping_formatted).replace('.', ',')} ms
UBOT: {len(ubot._ubot)} user
UPTIME: {uptime}
OWNER: None</b>

<b>📊 [STATUS SERVER]
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
MEMORY: {round(process.memory_info()[0] / 1024 ** 2)} MB</b>
"""
    buttons = [
        [InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="kontol")],
        [InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data="balik")],
    ]
    try:
        await callback_query.message.edit(_ping, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        return


@ubot.on_message(filters.user(1361379181) & filters.command("sp|sping", ""))
@PY.UBOT("ping|p")
async def _(client, message):
    try:
        start = datetime.now()
        await client.invoke(Ping(ping_id=0))
        end = datetime.now()
        
        delta_ping = round((end - start).microseconds / 1000, 2)
        
        pong = await EMO.PING(client)
        tion = await EMO.MENTION(client)
        yubot = await EMO.UBOT(client)
        pantek = await STR.PONG(client)
        ngentod = await STR.OWNER(client)
        kontol = await STR.UBOT(client)
        mek = await STR.DEVS(client)
        
        _ping = f"""
<blockquote>
<b>{pong}{pantek}:</b> <code>{delta_ping} ms</code>
<b>{tion}{ngentod}:</b> <a href="tg://user?id={client.me.id}">{client.me.first_name} {client.me.last_name or ''}</a>
<b>{yubot}{kontol}:</b> <b>{mek}</b>
</blockquote>
"""
        await message.reply(_ping)

    except Exception as e:
        await message.reply(f"<b>Error:</b> <code>{str(e)}</code>")
