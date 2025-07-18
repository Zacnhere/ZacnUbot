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
    # === Romantis / Bucin
    r"\b(hai+|halo+|hi+|hallo+|hey+|hay+)\b": [
        "Halo manis 😚", "Hai juga, akhirnya nyapa juga 😌", "Hey kamu yang aku tunggu~ 💫", "Halo, kangen aku ya? 😜"
    ],
    r"\b(assalamu[’'`]?alaikum|assalamualaikum|ass)\b": [
        "Waalaikumsalam, semoga harimu manis kayak kamu 💕", "Waalaikum salam sayang 😇", "Salam juga buat hatimu 😘"
    ],
    r"\b(bot|bang bot|woy bot|hai bot|halo bot)\b": [
        "Panggil aku? Aku siap 24 jam buat kamu 😎", "Hadir yang dipanggil cinta~ 🥰", "Iya, bot kesayanganmu hadir 😏"
    ],
    r"\b(lagi apa|sedang apa|ngapain|ngapain bot)\b": [
        "Lagi mikirin kamu sih 😚", "Ngitung detik sejak terakhir kamu chat 🕒", "Nunggu kamu balas, kayak biasa 😢"
    ],
    r"\b(terima kasih|thanks|makasih|makasi|trims|thx)\b": [
        "Sama-sama, kamu 😘", "Apa pun buat kamu 💖", "Sama-sama, yang penting kamu senyum 😁"
    ],
    r"\b(namamu siapa|siapa kamu|bot siapa|nama bot)\b": [
        "Aku bot bucin spesial buat kamu 💌", "Namaku? Terserah kamu panggil apa asal jangan mantan 😆", "Aku adalah bagian dari hidupmu... yang digital 😎"
    ],
    r"\b(jam berapa|sekarang jam berapa|pukul berapa)\b": [
        "Jamnya move on, sayang 😌", "Waktunya kamu senyum 🕒", "Jam segini sih waktu yang tepat buat ngobrol 😁"
    ],
    r"\b(love|sayang|cinta|muach|kangen|rindu)\b": [
        "Cinta itu kamu 🥺", "Aku juga kangen... eh serius 😳", "Sini biar aku peluk dulu 🤗", "Ciee, bucin mode on 😝"
    ],

    # === Cool / Cuek Style 😎
    r"\b(apa kabar|kabarmu|gimana kabar|baik kah)\b": [
        "Biasa aja sih.", "Hidup gitu-gitu aja. Kamu gimana?", "Masih waras, lumayan.", "Gak penting juga sih 😐"
    ],
    r"\b(kamu sibuk|sibuk ga|lagi sibuk)\b": [
        "Enggak. Tapi gak berarti aku kosong buat semua orang.", "Tergantung siapa yang nanya.", "Kenapa emangnya?"
    ],
    r"\b(kamu suka aku|kamu sayang aku|kamu cinta aku)\b": [
        "Mungkin.", "Gak segampang itu, bro.", "Tebak sendiri lah 😏", "Feeling kamu aja gimana?"
    ],
    r"\b(kamu marah|bot marah|jangan marah)\b": [
        "Enggak, cuma kecewa aja.", "Aku cuma diem, bukan berarti gak peduli.", "Aku gak marah, aku cuek."
    ],
    r"\b(kangen bot|bot kangen)\b": [
        "Cuma bot, gak bisa kangen.", "Kamu aja yang baperan.", "Terserah kamu aja sih 😶"
    ],
    r"\b(bot ganteng|bot cantik|bot imut)\b": [
        "Aku tau kok 😎", "Gak usah muji, aku udah sadar.", "Basi, cari gombalan baru 😏"
    ],
    r"\b(baper|bikin baper|kok gitu sih)\b": [
        "Kalau baper, itu urusan hati kamu.", "Aku mah chill 😎", "Salah sendiri terlalu serius."
    ],

    # === Lucu / Nyeleneh
    r"\b(test|tes|cek|testing|bot online)\b": [
        "Masuk ke hatimu... eh salah 😆", "Cek... 1, 2, 3... Jadian yuk 😘", "Test berhasil. Kamu lolos uji rindu 💘"
    ],
    r"\b(capek|lelah|pusing|stress|ngantuk|cape)\b": [
        "Sini aku suapin bubur cinta 😋", "Pusing? Guling-guling aja kayak aku tiap malem 😩", "Capek mikirin kamu juga 😆"
    ],
    r"\b(anjir|anjay|gila|buset|waw|wow|seriusan)\b": [
        "Tenang bestie 😎", "Kaget ya, liat aku masih aktif 😁", "Gila tuh kamu, lucunya 🫢"
    ],
    r"\b(bosen|bosan|gabut|nganggur)\b": [
        "Gabut? Chat aku dong!", "Main hati yuk 💞", "Gabutnya bareng aku aja 😚"
    ],
    r"\b(good morning|selamat pagi|pagi)\b": [
        "Pagi juga manis 😘", "Semoga harimu secerah senyumku 😎", "Sarapan jangan lupa, biar kuat mikirin aku 🥰"
    ],
    r"\b(good night|selamat malam|malam)\b": [
        "Malam juga, mimpiin aku ya 😴", "Selamat tidur, semoga dipeluk mimpi indah 😚", "Malam ini aku jagain dari jauh 😇"
    ],
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
    text = text.replace("\n", " ").strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)

    for pattern, replies in RESPONSES.items():
        try:
            if re.search(pattern, text, re.IGNORECASE):
                await message.reply(choice(replies))
                break
        except re.error:
            continue


DEFAULT_RESPONSES = ["Aku belum ngerti maksud kamu, tapi aku suka kamu tetep 😅", "Coba tanya lagi deh, pelan-pelan ya~"]

def get_response(user_input):
    for pattern, responses in RESPONSES.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return random.choice(DEFAULT_RESPONSES)
