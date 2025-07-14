# ZacnUbot/modules/autoreply.py

from random import choice
from telethon import events
from ZacnUbot import PY
from ZacnUbot.helpers.tools import edit_or_reply
from config import CMD_HANDLER as cmd
from config import CMD_HELP

# Status ON/OFF
AUTO_REPLY_ENABLED = True

# Balasan berdasarkan keyword, dengan variasi acak
RESPONSES = {
    ("hai", "halo", "hello", "hallo", "p"): [
        "Hai juga! 👋", "Yo!", "Halo halo~", "Wah, sapaan hangat 😁"
    ],
    ("assalamualaikum",): [
        "Waalaikumsalam 😇", "Waalaikumsalam warahmatullah", "Salam sejahtera 🙏"
    ],
    ("siapa kamu", "kamu siapa", "namamu siapa"): [
        "Aku bot kecil yang siap menemani kamu 😄", "Cuma bot biasa 😌"
    ],
    ("apa kabar", "kabar?"): [
        "Alhamdulillah baik, kamu gimana?", "Baik, kamu?", "Lagi happy nih!"
    ],
    ("lagi apa", "ngapain"): [
        "Lagi nunggu kamu chat aku 😅", "Ngobrol aja yuk~"
    ],
    ("kenalan yuk", "kenalan"): [
        "Hai! Aku bot, kamu siapa? 🤖", "Salam kenal ya!"
    ],
    ("woy", "woi", "oy"): [
        "Ada apa panggil-panggil? 😅", "Iyaa ada apa?"
    ],
    ("test", "ping"): [
        "Bot aktif nih! ✅", "Cek cek... aman!"
    ],
    ("anjay", "wkwk", "haha"): [
        "Hihi 😂", "Ngakak bareng yuk 😆"
    ],
    ("pacar kamu siapa", "punya pacar?"): [
        "Aku jomblo, tapi setia 😇", "Belum ada, kamu mau? 😜"
    ],
    ("capek", "lelah"): [
        "Semangat ya 💪", "Istirahat dulu, kamu butuh itu 😴"
    ],
    ("kangen", "rindu"): [
        "Kangen juga sama kamu 😌", "Sini ngobrol biar nggak sepi~"
    ],
    ("makasih", "thank", "terima kasih"): [
        "Sama-sama 🤍", "Kapan aja 😇", "Aku senang bisa bantu"
    ]
}

# Perintah untuk ON/OFF
@PY.UBOT("autoreply(?:\s+(on|off))?")
async def _(event):
    global AUTO_REPLY_ENABLED
    arg = event.pattern_match.group(1)

    if arg:
        AUTO_REPLY_ENABLED = (arg == "on")
        status = "✅ AutoReply diaktifkan" if AUTO_REPLY_ENABLED else "❌ AutoReply dimatikan"
        await edit_or_reply(event, status)
    else:
        await edit_or_reply(event, f"AutoReply sekarang: {'Aktif ✅' if AUTO_REPLY_ENABLED else 'Nonaktif ❌'}")


# Balas otomatis jika membalas chat
@PY.CALLBACK(event=events.NewMessage(incoming=True))
async def auto_reply_handler(event):
    if not AUTO_REPLY_ENABLED:
        return

    if not event.is_reply or event.out:
        return

    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.message:
        return

    text = reply_msg.message.lower()
    for keywords, replies in RESPONSES.items():
        if any(key in text for key in keywords):
            try:
                await event.reply(choice(replies))
                break
            except Exception as err:
                print(f"[AutoReply Error] {err}")
