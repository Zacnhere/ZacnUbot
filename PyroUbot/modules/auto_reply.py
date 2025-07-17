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



# === Data balasan chatbot ===
RESPONSES = {
    r"\b(hai+|halo+|hi+|hallo+)\b": ["Hai juga!", "Halo!", "Ada yang bisa dibantu?", "Hai, kamu siapa?"],
    r"\b(assalamu[’']?alaikum)\b": ["Waalaikumsalam!", "Waalaikumsalam warahmatullahi wabarakatuh."],
    r"\b(bot)\b": ["Aku bot yang ramah ✨", "Ya, ada apa?", "Dipanggil? 😊"],
    r"\b(lagi apa|sedang apa)\b": ["Lagi nunggu kamu nih 😁", "Lagi bantu yang lain juga"],
    r"\b(terima kasih|thanks|makasih)\b": ["Sama-sama 😄", "You're welcome!", "Kapan-kapan lagi ya"],
    r"\b(namamu siapa|siapa kamu)\b": ["Aku bot buatan tuanku 😎", "Rahasia dong 😏"],
    r"\b(jam berapa)\b": ["Aku gak punya jam, tapi kayaknya kamu udah lama nungguin aku 😅"],
    r"\b(love|sayang|cinta)\b": ["Aku juga sayang kamu ❤️", "Ciee cinta-cintaan~"],
}


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


@AUTO_REPLAY("AUTOREPLAY", ubot)
async def auto_reply_handler(client, message: Message):
    status = await get_vars(client.me.id, "AUTOREPLY_STATUS")
    if not status:
        return

    text = message.text.lower() if message.text else ""
    for pattern, replies in RESPONSES.items():
        if re.search(pattern, text):
            await message.reply(choice(replies))
            break
