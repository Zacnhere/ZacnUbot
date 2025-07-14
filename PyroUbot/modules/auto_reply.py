from pyrogram.types import Message
from pyrogram import filters
from random import choice

from PyroUbot import PY
from PyroUbot.helpers.tools import get_vars, set_vars
from PyroUbot.helpers.basic import edit_or_reply
from PyroUbot.helpers.types import EMO


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


@PY.on_message(filters.incoming & filters.reply)
async def auto_reply_handler(client, message: Message):
    status = await get_vars(client.me.id, "AUTOREPLY_STATUS")

    # Tidak aktif → keluar
    if not status:
        return

    if not message.reply_to_message or not message.reply_to_message.text:
        return

    text = message.reply_to_message.text.lower()

    for keywords, replies in RESPONSES.items():
        if any(key in text for key in keywords):
            await message.reply(choice(replies))
            break
        
