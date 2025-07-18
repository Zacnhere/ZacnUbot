import os
import wget
from pyrogram import filters
from pyrogram.types import Message
from random import choice
import re
from gc import get_objects
from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent)

from PyroUbot import *


@PY.UBOT("autoreply")
async def toggle_autoreply(client, message: Message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.text.split()[0]}</code> <b>[on/off]</b>"
        )

    toggle_option = message.command[1].lower()
    toggle_options = {"on": True, "off": False}

    if toggle_option not in toggle_options:
        return await message.reply(f"{ggl}Opsi tidak valid. Gunakan 'on' atau 'off'.")

    try:
        await set_vars(client.me.id, "AUTOREPLY_STATUS", toggle_options[toggle_option])
        status_text = "diaktifkan" if toggle_options[toggle_option] else "dinonaktifkan"
        return await message.reply(f"{brhsl}Auto Reply berhasil {status_text}.")
    except Exception as e:
        return await message.reply(f"{ggl}Gagal mengatur status: {str(e)}")


def load_responses_from_txt(filepath="respon.txt"):
    responses = {}
    current_pattern = None

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            elif not line.startswith("-"):
                current_pattern = line
                responses[current_pattern] = []
            else:
                responses[current_pattern].append(line[1:].strip())
    return responses

DIR_PATH = os.path.dirname(__file__)
RESPONSES = load_responses_from_txt(os.path.join(DIR_PATH, "respon.txt"))

@AUTO_REPLAY("AUTOREPLY", ubot)
async def auto_reply_handler(client, message: Message):
    status = await get_vars(client.me.id, "AUTOREPLY_STATUS")
    if not status:
        return

    text = message.text.lower() if message.text else ""
    text = text.replace("\n", " ").strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)

    for pattern, replies in RESPONSES.items():
        try:
            if re.search(pattern, text, re.IGNORECASE):
                await message.reply(choice(replies))
                break
        except re.error:
            continue     
