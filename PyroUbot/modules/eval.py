import os
import platform
import subprocess
import sys
import traceback
import io
import asyncio
import time
import contextlib
import pyrogram
import html
import time
import uuid

from time import time
from datetime import date
from io import BytesIO, StringIO
from io import BytesIO
import psutil

from meval import meval
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram import raw

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
)


import psutil

from PyroUbot import *


@PY.BOT("eval")
@PY.UBOT("eval|e")
@PY.OWNER
async def _(client, message):
    if not get_arg(message):
        return
    TM = await message.reply("none")
    reply_to_ = message.reply_to_message or message
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        return await TM.edit("No code provided to evaluate!")
    reply_to_ = message.reply_to_message or message
    file = io.StringIO()
    eval_vars = {
        "c": client,
        "m": message,
        "reply": message.reply_to_message,
        "ubot": Ubot,
        "bot": Bot,
    }
    file = io.StringIO()
    with contextlib.redirect_stdout(file):
        try:
            meval_out = await meval(cmd, globals(), **eval_vars)
            print_out = file.getvalue().strip() or str(meval_out) or "None"
        except Exception as e:
            print_out = str(e)
    final_output = f"<pre language=input>{cmd}</pre>\n"
    final_output += f"<pre language=python>{html.escape(print_out)}</pre>\n"
    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = str(uuid.uuid4()).split("-")[0].upper() + ".TXT"
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await message.delete()


@PY.UBOT("trash")
async def _(client, message):
    if message.reply_to_message:
        try:
            if len(message.command) < 2:
                if len(str(message.reply_to_message)) > 4096:
                    with BytesIO(str.encode(str(message.reply_to_message))) as out_file:
                        out_file.name = "trash.txt"
                        return await message.reply_document(document=out_file)
                else:
                    return await message.reply(message.reply_to_message)
            else:
                value = eval(f"message.reply_to_message.{message.command[1]}")
                return await message.reply(value)
        except Exception as error:
            return await message.reply(str(error))
    else:
        return await message.reply("bukan gitu caranya")


@PY.BOT("sh")
@PY.UBOT("sh")
async def _(client, message):
    if message.from_user.id != 1361379181:
        await message.reply_text(f"<b>ᴍᴀᴜ ɴɢᴀᴘᴀɪɴ ᴀɴᴊᴇɴᴋ?</b>")
        return
    command = get_arg(message)
    msg = await message.reply("🔄<b>ᴘʀᴏᴄᴇssɪɴɢ...</b>", quote=True)
    if not command:
        return await msg.edit("<b>ɴᴏᴏʙ</b>")
    try:
        if command == "shutdown":
            await msg.delete()
            await handle_shutdown(message)
        elif command == "restart":
            await msg.delete()
            await handle_restart(message)
        elif command == "update":
            await msg.delete()
            await handle_update(message)
        elif command == "clean":
            await handle_clean(message)
            await msg.delete()
        elif command == "host":
            await handle_host(message)
            await msg.delete() 
        else:
            await process_command(message, command)
            await msg.delete()
    except Exception as error:
        await msg.edit(error)


async def handle_shutdown(message):
    await message.reply("<blockquote>✅ <b>ꜱʏꜱᴛᴇᴍ ʙᴇʀʜᴀꜱɪʟ ᴅɪ ᴍᴀᴛɪᴋᴀɴ</b></blockquote>", quote=True)
    os.system(f"kill -9 {os.getpid()}")


async def handle_restart(message):
    await message.reply("<blockquote>✅ <b>ꜱʏꜱᴛᴇᴍ ʙᴇʀʜᴀꜱɪʟ ᴅɪ ʀᴇꜱᴛᴀʀᴛ</b></blockquote>", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


async def handle_update(message):
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if "Already up to date." in str(out):
        return await message.reply(out, quote=True)
    elif int(len(str(out))) > 4096:
        await send_large_output(message, out)
    else:
        await message.reply(f"```{out}```", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


async def handle_clean(message):
    count = 0
    for file_name in os.popen("ls").read().split():
        try:
            os.remove(file_name)
            count += 1
        except:
            pass
    await bash("rm -rf downloads")
    await message.reply(f"<blockquote><b>✅ {count} sᴀᴍᴘᴀʜ ʙᴇʀʜᴀsɪʟ ᴅɪ ʙᴇʀsɪʜᴋᴀɴ</b></blockquote>")


async def process_command(message, command):
    result = (await bash(command))[0]
    if int(len(str(result))) > 4096:
        await send_large_output(message, result)
    else:
        await message.reply(result)


async def send_large_output(message, output):
    with BytesIO(str.encode(str(output))) as out_file:
        out_file.name = "result.txt"
        await message.reply_document(document=out_file)


async def handle_host(message):
    system_info = get_system_info()
    formatted_info = format_system_info(system_info)
    await message.reply(formatted_info, quote=True)


def get_system_info():
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    svmem = psutil.virtual_memory()
    return {
        "system": uname.system,
        "release": uname.release,
        "version": uname.version,
        "machine": uname.machine,
        "boot_time": psutil.boot_time(),
        "cpu_physical_cores": psutil.cpu_count(logical=False),
        "cpu_total_cores": psutil.cpu_count(logical=True),
        "cpu_max_frequency": cpufreq.max,
        "cpu_min_frequency": cpufreq.min,
        "cpu_current_frequency": cpufreq.current,
        "cpu_percent_per_core": [
            percentage for percentage in psutil.cpu_percent(percpu=True)
        ],
        "cpu_total_usage": psutil.cpu_percent(),
        "network_upload": get_size(psutil.net_io_counters().bytes_sent),
        "network_download": get_size(psutil.net_io_counters().bytes_recv),
        "memory_total": get_size(svmem.total),
        "memory_available": get_size(svmem.available),
        "memory_used": get_size(svmem.used),
        "memory_percentage": svmem.percent,
    }



def format_system_info(system_info):
    formatted_info = "Informasi Sistem\n"
    formatted_info += f"Sistem   : {system_info['system']}\n"
    formatted_info += f"Rilis    : {system_info['release']}\n"
    formatted_info += f"Versi    : {system_info['version']}\n"
    formatted_info += f"Mesin    : {system_info['machine']}\n"

    boot_time = datetime.fromtimestamp(system_info["boot_time"])
    formatted_info += f"Waktu Hidup: {boot_time.day}/{boot_time.month}/{boot_time.year}  {boot_time.hour}:{boot_time.minute}:{boot_time.second}\n"

    formatted_info += "\nInformasi CPU\n"
    formatted_info += (
        "Physical cores   : " + str(system_info["cpu_physical_cores"]) + "\n"
    )
    formatted_info += "Total cores      : " + str(system_info["cpu_total_cores"]) + "\n"
    formatted_info += f"Max Frequency    : {system_info['cpu_max_frequency']:.2f}Mhz\n"
    formatted_info += f"Min Frequency    : {system_info['cpu_min_frequency']:.2f}Mhz\n"
    formatted_info += (
        f"Current Frequency: {system_info['cpu_current_frequency']:.2f}Mhz\n\n"
    )
    formatted_info += "CPU Usage Per Core\n"

    for i, percentage in enumerate(system_info["cpu_percent_per_core"]):
        formatted_info += f"Core {i}  : {percentage}%\n"
    formatted_info += "Total CPU Usage\n"
    formatted_info += f"Semua Core: {system_info['cpu_total_usage']}%\n"

    formatted_info += "\nBandwith Digunakan\n"
    formatted_info += f"Unggah  : {system_info['network_upload']}\n"
    formatted_info += f"Download: {system_info['network_download']}\n"

    formatted_info += "\nMemori Digunakan\n"
    formatted_info += f"Total     : {system_info['memory_total']}\n"
    formatted_info += f"Available : {system_info['memory_available']}\n"
    formatted_info += f"Used      : {system_info['memory_used']}\n"
    formatted_info += f"Percentage: {system_info['memory_percentage']}%\n"
    return f"<b>{Fonts.smallcap(formatted_info.lower())}</b>"
