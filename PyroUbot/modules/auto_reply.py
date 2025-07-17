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
    ("hai", "halo", "hallo", "hi"): ["Hai juga!", "Halo!", "Ada yang bisa dibantu?", "Hai, kamu siapa?"],
    ("assalamualaikum",): ["Waalaikumsalam!", "Waalaikumsalam warahmatullahi wabarakatuh."],
    ("bot",): ["Aku bot yang ramah ✨", "Ya, ada apa?", "Dipanggil? 😊"],
    ("lagi apa", "sedang apa"): ["Lagi nunggu kamu nih 😁", "Lagi bantu yang lain juga"],
    ("terima kasih", "thanks"): ["Sama-sama 😄", "You're welcome!", "Kapan-kapan lagi ya"],
    ("namamu siapa", "siapa kamu"): ["Aku bot buatan tuan ku 😎", "Rahasia dong 😏"],
    ("jam berapa",): ["Aku gak punya jam, tapi kayaknya kamu udah lama nungguin aku 😅"],
    ("love", "sayang", "cinta"): ["Aku juga sayang kamu ❤️", "Ciee cinta-cintaan~"],
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


@PY.AUTO_REPLAY("AUTOREPLAY", ubot)
async def auto_reply_handler(client, message: Message):
    status = await get_vars(client.me.id, "AUTOREPLY_STATUS")
    if not status:
        return

    text = message.text.lower() if message.text else None
    if not text:
        return

    for keywords, replies in RESPONSES.items():
        # Cocokkan menggunakan regex agar lebih akurat (cocok utuh per kata)
        if any(re.search(rf"\b{re.escape(key)}\b", text) for key in keywords):
            await message.reply(choice(replies))
            break
