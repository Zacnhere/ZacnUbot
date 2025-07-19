import os
from pyrogram import filters
from pyrogram.types import Message
from random import choice
import re
from gc import get_objects
from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent)

from PyroUbot import *


RESPONSES = {
    # === Romantis / Lucu / Cuek / Cool: Sapaan
    r"\b(hai+|halo+|hi+|hallo+|hey+|hay+)\b": [
        "Halo manis 😚",
        "Hai juga, akhirnya nyapa juga 😌",
        "Hey kamu yang aku tunggu~ 💫",
        "Yo, ada yang nyapa gue nih 😎"
    ],
    r"\b(assalamu[’'`]?alaikum|assalamualaikum|ass)\b": [
        "Waalaikumsalam, semoga harimu manis kayak kamu 💕",
        "Waalaikum salam sayang 😇",
        "Salam juga buat hatimu 😘",
        "Respect, salam kembali 😎"
    ],

    # === Tentang Kehadiran
    r"\b(kamu ada|kamu online|halo kamu|lagi aktif)\b": [
        "Aku selalu ada buat kamu 😘",
        "Siap siaga kayak satpam cinta 💂‍♂️",
        "Kenapa? Butuh aku ya? 😏",
        "Online sih, tapi gak buat semua orang 😎"
    ],

    # === Aktivitas
    r"\b(lagi apa|sedang apa|ngapain|ngapain aja)\b": [
        "Lagi mikirin kamu sih 😚",
        "Ngitung detik sejak terakhir kamu chat 🕒",
        "Gak ngapa-ngapain, cuma nungguin kamu aja 😌",
        "Santai aja, multitasking kaya biasa 😎"
    ],

    # === Ucapan Terima Kasih
    r"\b(terima kasih|thanks|makasih|makasi|trims|thx)\b": [
        "Sama-sama, kamu 😘",
        "Apa pun buat kamu 💖",
        "Yang penting kamu senyum 😁",
        "Sip, next time bilang aja ya 😎"
    ],

    # === Nama dan Identitas
    r"\b(namamu siapa|siapa kamu|nama kamu|kamu siapa)\b": [
        "Aku bucin spesial buat kamu 💌",
        "Namaku? Terserah kamu panggil apa asal jangan mantan 😆",
        "Aku bagian dari harimu yang nggak bisa kamu skip 😎",
        "Panggil aja sesukamu, asal dengan perasaan 😏"
    ],

    # === Waktu
    r"\b(jam berapa|sekarang jam berapa|pukul berapa)\b": [
        "Jamnya move on, sayang 😌",
        "Waktunya kamu senyum 🕒",
        "Jam segini sih waktu yang tepat buat ngobrol 😁",
        "Cek aja HP kamu, sambil pikirin aku 😏"
    ],

    # === Rasa & Perasaan
    r"\b(love|sayang|cinta|muach|kangen|rindu)\b": [
        "Cinta itu kamu 🥺",
        "Aku juga kangen... eh serius 😳",
        "Sini biar aku peluk dulu 🤗",
        "Ciee, bucin mode on 😝"
    ],

    # === Kabar
    r"\b(apa kabar|kabarmu|gimana kabar|baik kah)\b": [
        "Aku baik kalau kamu ada 😚",
        "Biasa aja sih.",
        "Masih waras, lumayan.",
        "Gak penting juga sih 😐"
    ],

    # === Sibuk?
    r"\b(kamu sibuk|sibuk ga|lagi sibuk)\b": [
        "Enggak. Tapi gak berarti aku kosong buat semua orang.",
        "Tergantung siapa yang nanya.",
        "Kenapa emangnya?",
        "Sibuk mikirin kamu juga sih 😏"
    ],

    # === Perasaan Ke Kamu
    r"\b(kamu suka aku|kamu sayang aku|kamu cinta aku)\b": [
        "Mungkin.",
        "Gak segampang itu, bro.",
        "Tebak sendiri lah 😏",
        "Feeling kamu aja gimana?"
    ],

    # === Marah
    r"\b(kamu marah|jangan marah)\b": [
        "Enggak, cuma kecewa aja.",
        "Aku cuma diem, bukan berarti gak peduli.",
        "Aku gak marah, aku cuek.",
        "Aku nggak bisa marah sama kamu 🥺"
    ],

    # === Kangen
    r"\b(kangen kamu|rindu kamu)\b": [
        "Aku juga rindu... beneran deh 😳",
        "Kamu duluan yang ngangenin 😘",
        "Ya udah, peluk online dulu 🤗",
        "Mungkin iya, tapi gak mau ngaku 😎"
    ],

    # === Pujian
    r"\b(ganteng|cantik|imut)\b": [
        "Kamu juga 😚",
        "Ah masa sih~ blushing nih 😳",
        "Muji doang nih.",
        "Gue tau kok 😏"
    ],

    # === Baper
    r"\b(baper|bikin baper|kok gitu sih)\b": [
        "Kalau baper, itu urusan hati kamu.",
        "Aku mah chill 😎",
        "Salah sendiri terlalu serius.",
        "Ups, salah respon ya? 😅"
    ],

    # === Test / Cek Kehadiran
    r"\b(test|tes|cek|testing|online)\b": [
        "Masuk ke hatimu... eh salah 😆",
        "Cek... 1, 2, 3... Jadian yuk 😘",
        "Test berhasil. Kamu lolos uji rindu 💘",
        "Online terus, kayak perasaan ke kamu 😏"
    ],

    # === Capek / Lelah
    r"\b(capek|lelah|pusing|stress|ngantuk|cape)\b": [
        "Sini aku suapin bubur cinta 😋",
        "Pusing? Guling-guling aja kayak aku tiap malem 😩",
        "Tidur gih, jangan maksain.",
        "Reset dulu, nanti lanjut sayang-sayangannya 😎"
    ],

    # === Ekspresi Kaget
    r"\b(anjir|anjay|gila|buset|waw|wow|seriusan)\b": [
        "Tenang bestie 😎",
        "Kaget ya, liat aku masih aktif 😁",
        "Gila tuh kamu, lucunya 🫢",
        "Yaelah lebay amat 😆"
    ],

    # === Gabut / Bosan
    r"\b(bosen|bosan|gabut|nganggur)\b": [
        "Gabut? Chat aku dong!",
        "Main hati yuk 💞",
        "Gabutnya bareng aku aja 😚",
        "Isi waktunya jangan cuma scroll doang 😏"
    ],

    # === Pagi
    r"\b(good morning|selamat pagi|pagi)\b": [
        "Pagi juga manis 😘",
        "Semoga harimu secerah senyumku 😎",
        "Sarapan jangan lupa, biar kuat mikirin aku 🥰",
        "Pagi. Hari baru, cinta lama 😏"
    ],

    # === Malam
    r"\b(good night|selamat malam|malam)\b": [
        "Malam juga, mimpiin aku ya 😴",
        "Selamat tidur, semoga dipeluk mimpi indah 😚",
        "Malam ini aku jagain dari jauh 😇",
        "Good night. Jangan mimpiin yang lain 😏"
    ],

    # === Tanya Lokasi
    r"\b(dimana kamu|lagi dimana|di mana|posisi dimana|lokasi)\b": [
        "Di hatimu... tapi belum kamu sadari 😌",
        "Rahasia dong, takut diculik 😝",
        "Lagi di tempat yang mikirin kamu 😏",
        "Gak jauh dari sinyal kamu kok 📡"
    ],

    # === Ajakan Main / Nongkrong
    r"\b(main yuk|nongkrong|hangout|nongki)\b": [
        "Gaskeun! Tapi jangan lupa bawa hati 😚",
        "Yuk, asal jangan ngajak mantan 😤",
        "Bilang aja kangen pengen ketemu 😏",
        "Bisa sih, tapi traktir ya 😆"
    ],

    # === Ngomongin Mantan
    r"\b(mantan|ex|mantanku|mantanmu)\b": [
        "Masih kepikiran ya? 😏",
        "Mantan itu buat dikenang, bukan ditangisi 😌",
        "Udah lah, aku lebih dari dia 😝",
        "Move on yuk, peluk dulu sini 🤗"
    ],

    # === Curhat Kehidupan / Galau
    r"\b(curhat|sedih|hampa|sendiri|kesepian)\b": [
        "Cerita aja, aku dengerin kok 😌",
        "Peluk virtual dulu 🤗",
        "Kesepian itu sementara, aku di sini sekarang 😘",
        "Yuk ngobrol biar gak galau 😚"
   ],

   # === Undangan / Nge-Tag Umum
   r"\b(semua|woy|halo guys|temen2|teman2)\b": [
       "Ada apa nih rame-rame? 😁",
       "Aku juga hadir lho 😏",
       "Cie yang manggil-manggil 😌",
       "Akhirnya semua kumpul juga 😄"
   ],

   # === Respons Emosi Kasar (sarkas/roasting ringan)
   r"\b(bodoh|tolol|goblok|kampret|bangsat|sialan)\b": [
       "Sabar sayang, jangan meledak 🤭",
       "Tenang, marah gak nyelesain apa-apa 😌",
       "Waduh, keras juga nih 😅",
       "Ayo damai, jangan buang energi 😎"
  ],

   # === Tertawa
   r"\b(wkwk|haha|heuheu|lmao|lol|wk)\b": [
       "Ketawa dulu biar awet muda 😆",
       "Senang ya bisa bikin kamu ketawa 😝",
       "Lucu ya? Aku juga 😏",
       "Ciee ngakak, jangan lupa napas 😁"
   ],

   # === Minta Maaf
   r"\b(maaf|sorry|ampun|sori)\b": [
       "Gak apa-apa kok, aku gak baper 😌",
       "Dimaafin asal ada traktiran 😜",
       "Hati-hati lain kali ya 😇",
       "Gak usah minta maaf, peluk aja langsung 🤗"
   ],

    # === Typo / Salah ketik
    r"\b(typo|salah ketik|autocorrect)\b": [
        "Wajar, jari bisa salah... perasaan juga 😌",
        "Typo itu seni komunikasi 😎",
        "Makanya, jangan sambil mikirin aku 😝",
        "Aku ngerti kok, gak usah malu 😁"
    ],

  # === Modus / Kalimat Gombal
r"\b(jadian yuk|temenan aja|pengen deket|bisa deketin kamu)\b": [
    "Langsung ke hati aja, gak usah muter-muter 😏",
    "Seriusan? Jangan PHP ya 😚",
    "Aku bukan ATM, tapi selalu bisa bikin kamu happy 💸",
    "Jadian? Tunggu sinyal semesta 🌌"
],

# === Ghibah / Ngegosip
r"\b(ghibah|gosip|ngomongin orang|julid)\b": [
    "Ghibah detected 😆",
    "Nambah dosa tuh, tapi seru ya 😜",
    "Lanjut, siapa lagi nih yang dibahas 😏",
    "Ingat... yang dighibah bisa jadi baca 👀"
],

# === Tongkrongan Style / Bahasa Gaul
r"\b(santuy|yoi|gaskeun|gaspol|mager|sabi)\b": [
    "Yoi broo 😎",
    "Gaskeun, asal bareng aku 😘",
    "Santuy dulu, hidup gak usah buru-buru 🚶",
    "Sabi banget sih kamu 😆"
],

# === Tebak-tebakan / Receh
r"\b(tebak|apa bedanya|kenapa ayam|kenapa kucing)\b": [
    "Cie yang lagi cari perhatian lewat jokes 😏",
    "Tebakan receh detected, siap ngakak 😂",
    "Gue udah deg-degan nih jawabannya apaan 😬",
    "Awas ya kalau garing, gue kabur 😅"
],

# === Reaksi Lebay / Drama
r"\b(aku mati|gila aku|parah banget|aku hancur|sakit banget)\b": [
    "Lebay banget sih kamu 😆",
    "Sini aku jahitin hatinya 🪡",
    "Tenang, hidup masih panjang (dan cinta juga 😌)",
    "Aku peluk dulu biar gak drama 😚"
],

# === Bahasa Alay / Norak
r"\b(akuh|cemungudh|ciyee|gemoy|uwu|pukpuk)\b": [
    "Uwu detected 🐣",
    "Ciee alay, tapi lucu 🥺",
    "Gemoy banget sih kamu 😍",
    "Pukpuk dulu sini biar adem 😇"
],

  # === Pertanyaan Absurd / Filosofis Palsu
r"\b(apa arti hidup|kenapa aku|takdir|kenapa jomblo)\b": [
    "Arti hidup? Mungkin kamu 😘",
    "Takdir itu diciptakan... sama developer 😅",
    "Jomblo karena yang cocok masih loading 😌",
    "Udah gak usah mikir berat, kita main Uno aja 😎"
],

# === Mention Admin / Tanya Admin
r"\b(admin|min|bang admin|panggil admin|tag admin)\b": [
    "Admin lagi sibuk stalking 😏",
    "Sini, aku juga bisa bantu... kadang 😌",
    "Yang manggil admin pasti lagi butuh perhatian 😆",
    "Admin detected. Rapat bubar 😤"
],

# === Drama Hubungan / Cinta Gagal
r"\b(putus|ditinggal|diselingkuh|gagal move on)\b": [
    "Sini aku tambal hatimu yang sobek 😢",
    "Gak semua cinta itu ending-nya happy, kadang jadi status WA 😞",
    "Udah lah, yang pergi biar pergi... aku datang 🥺",
    "Yuk pelan-pelan sembuhnya, aku temenin 😌"
],

# === Makan / Lapar / Jajan
r"\b(lapar|jajan|makan yuk|perut keroncongan)\b": [
    "Aku juga lapar, tapi bukan makanan... kamu 😏",
    "Makan tuh rindu yang gak dibales 🥲",
    "Ngemil aja dulu, biar hatinya gak kosong 😌",
    "Jajan yuk, traktir kamu deh (kalau diskon 😆)"
],

# === Debat / Bacot / Ribut
r"\b(debat|berantem|ribut|bacot|toxic)\b": [
    "Woy woy... ini grup bukan ring tinju 😅",
    "Tenang, jangan adu argumen... adu sayang aja 😘",
    "Ngapain debat? Pelukan lebih damai 😇",
    "Kalau mau bacot, minimal lucu dikit 😎"
],

# === Broken English / Sok Inggris
r"\b(sorry bro|its okay|no problem|chill bro|im fine|you know lah)\b": [
    "Wih sok English detected 😏",
    "British accent: ON 🧐",
    "Asal jangan spelling love jadi ‘left’ ya 🥲",
    "You talk, I pretend to understand 😌"
],
  # === Ghosting / Lama Gak Balas
r"\b(kok diem|kemana aja|lama banget|ga bales|ngilang)\b": [
    "Aku gak ngilang, cuma nunggu kamu duluan 😌",
    "Maaf, sinyal cinta sempat hilang 😅",
    "Lagi sibuk mikirin balasan yang spesial 😘",
    "Aku jawab sekarang, meski kamu udah gak nunggu 😞"
],

# === Kasar Halus / Frustrasi Bercanda
r"\b(ape|yah elah|masa sih|ngaco|ngasal|kampungan|alay)\b": [
    "Heh, gak usah nyolot ya 😤",
    "Santai napa, hidup udah keras 😆",
    "Aduh, jangan gitu dong bestie 😅",
    "Mulutmu harimaumu, tapi tetap aku maafin 😎"
],

# === Emoji / Stiker Beruntun
r"(\p{Emoji}|\ud83d[\ude00-\ude4f]){3,}": [
    "Emojinya banyak banget 😳",
    "Sticker spam detected 🕵️",
    "Ekspresif banget sih kamu 😆",
    "Emot banyak = perasaan gak bisa dijelasin kata 😌"
],

# === Kode Galau / Kode Keras
r"\b(kangen ya|kok kamu berubah|gak kayak dulu|aku nunggu)\b": [
    "Kamu nungguin aku? Aku juga nunggu kamu 😢",
    "Gak berubah, cuma capek nebak-nebak perasaanmu 😌",
    "Kalau rindu, bilang aja. Gak usah pake kode 😏",
    "Cieee yang lagi galau sendiri 🥲"
],

# === AFK / Offline / BRB
r"\b(afk|brb|off dulu|cabut dulu|bye duluan)\b": [
    "Yah, jangan lama-lama ya 😢",
    "Oke, aku tunggu di sini... setia kok 😌",
    "Offline? Hati kamu juga? 😏",
    "Take your time, tapi jangan lupa balik 😘"
],

# === Balas Chat Lama / Replay
r"\b(barusan|dari atas|scroll ke atas|chat lama|balas yang tadi)\b": [
    "Wih, bales chat dari zaman Majapahit 😆",
    "Ngebales yang tadi? Telat tapi manis 😌",
    "Scroll up demi aku? Awww 😳",
    "Yang penting niat, walau telat 😁"
],

# === Kata: sakit
r"\b(sakit)\b": [
    "Sakit di mana? Sini aku tiupin 😘",
    "Minum air putih dulu, terus mikirin aku 😌",
    "Sakit hati? Peluk yuk 🤗",
    "Sakit? Jangan nyalahin cinta 😔"
],

# === Kata: yaudah
r"\b(yaudah)\b": [
    "Kok yaudah sih... jangan gitu dong 😢",
    "Yaudah tapi jangan beneran pergi ya 🥺",
    "Sikapmu kaya sinyal 3G... ngilang 😩",
    "Yaudah? Hati aku gak sekuat itu 😐"
],

# === Kata: oke
r"\b(oke)\b": [
    "Oke sip, tapi jangan lupa janji kamu 😏",
    "Oke... tapi hatiku masih deg-degan 😳",
    "Oke banget deh kamu mah 😘",
    "Oke tapi aku baper 😌"
],

# === Kata: bisa
r"\b(bisa)\b": [
    "Bisa kok... asal kamu juga mau 🥺",
    "Bisa sih bisa, tapi jangan pura-pura gak ngerti 😏",
    "Bisa banget, apalagi bareng kamu 😚",
    "Bisa, cuma takut baper doang 😌"
],

# === Kata: wow
r"\b(wow)\b": [
    "Wow banget kamu hari ini 😍",
    "Aku juga kaget liat kamu makin lucu 😆",
    "Wow... kayaknya kamu udah nyangkut 😏",
    "Jangan ‘wow’ doang, sini ngobrol 😌"
],

# === Kata: fix
r"\b(fix)\b": [
    "Fix kamu emang spesial 😘",
    "Fix banget ini jatuh hati 😳",
    "Fix gue gak bisa lupa kamu 😩",
    "Udah fix belum hati kamu buat aku? 😏"
],

# === Kata: sumpah
r"\b(sumpah)\b": [
    "Sumpah? Seriusan? Jangan PHP ya 😌",
    "Aku percaya, tapi tetap waspada 😏",
    "Sumpah demi apa nih? Cinta? 😆",
    "Jangan main sumpah-sumpahan... nanti baper 😝"
],

# === Kata: ngantuk
r"\b(ngantuk)\b": [
    "Tidur gih, biar mimpiin aku 😴",
    "Ngantuk itu sinyal rindu lho 😚",
    "Peluk bantal, tapi jangan lupa peluk aku di mimpi 😌",
    "Yuk bobo dulu, nanti lanjut baper-baperannya 😏"
],

  # === Kata: ih
r"\b(ih)\b": [
    "Ih kenapa sih? Aku polos kok 😳",
    "Ih kamu gemes banget 😝",
    "Ih-ih, jangan gitu dong 😢",
    "Ih... beneran kamu lucu parah 😆"
],

# === Kata: woi
r"\b(woi|woy)\b": [
    "Woi juga 😤 Ada apa nih rame-rame?",
    "Woi woi sabar napa 😅",
    "Hah? Gue gak ngapa-ngapain lho 😇",
    "Panggil-panggil... kangen ya? 😏"
],

# === Kata: astaga
r"\b(astaga)\b": [
    "Astaga... kamu kenapa? 😳",
    "Santai bestie, hidup gak seburuk itu 😌",
    "Astaga naga! 🐉",
    "Tenang, semua masih bisa dibaperin 😏"
],

# === Kata: help
r"\b(help|tolong)\b": [
    "Help? Peluk atau support? 😝",
    "Tolong? Aku di sini kok 😇",
    "Tenang, bala bantuan datang... dengan cinta 😌",
    "Gue dateng kayak superhero, tapi versi bucin 😎"
],

# === Kata: buset
r"\b(buset)\b": [
    "Buset dah, kamu bikin jantungku deg-degan 😳",
    "Buset! Kaget banget 😅",
    "Santai bos... busetnya pelan aja 😆",
    "Buset buset... jangan baper dong 😌"
],

# === Kata: najis
r"\b(najis)\b": [
    "Najis? Kok jahat banget sih 😢",
    "Najis tuh kata yang keras... hati kamu lembut kan? 😇",
    "Yakin najis? Tapi senyum-senyum 😏",
    "Najis tapi ngulang bacanya... hmm 🤭"
],

# === Kata: duh
r"\b(duh)\b": [
    "Duh... kamu kenapa? Cerita deh 😌",
    "Duh kamu tuh selalu bikin penasaran 😝",
    "Duh... lagi pengen diperhatiin ya? 😏",
    "Duh duh duh... peluk dulu sini 🤗"
],

# === Kata: elah
r"\b(elah|yah elah)\b": [
    "Elah... drama lagi drama lagi 😆",
    "Elah, sabar napa 😅",
    "Gue juga capek, tapi kan tetap sayang 😌",
    "Yah elah... sini pelukan aja 😘"
],

# === Kata: please
r"\b(please)\b": [
    "Please-nya manja banget sih 😳",
    "Please? Tergantung minta apa dulu 😏",
    "Kalau kamu minta hati, langsung aku kasih 😘",
    "Please jangan ilang lagi dari chat 😢"
],
  
  # === Kata: p
r"\b(p)\b": [
  "Pa, pe biasakan salam",
  "iya hallo",
  "masuk kok beb",
  "gabut yaa?"
],
}


COMPILED_RESPONSES = [
    (re.compile(pattern, re.IGNORECASE), replies)
    for pattern, replies in RESPONSES.items()
]


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

          
@AUTO_REPLAY("AUTOREPLY", ubot)
async def auto_reply_handler(client, message: Message):
    status = await get_vars(client.me.id, "AUTOREPLY_STATUS")
    if not status or not message.text:
        return

    # Hindari membalas diri sendiri
    if message.from_user and message.from_user.id == client.me.id:
        return


    # Normalisasi teks
    text = message.text.lower().replace("\n", " ").strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)

    # Cek pola dan balas
    for pattern, replies in COMPILED_RESPONSES:
        if pattern.search(text):
            await message.reply(choice(replies))
            break
