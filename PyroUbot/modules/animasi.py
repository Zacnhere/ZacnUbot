import asyncio
import random

import requests
from pyrogram import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *

from PyroUbot import *

DEFAULTUSER = "Nay"


NOBLE = [
    "╲╲╲┏━━┓╭━━━╮╱╱╱\n╲╲╲┗┓┏┛┃╭━╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏━╯╱╱\n╱╱┏┻━┳┳┻━┫┗┓╱╱╱\n╱╱╰━┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗━╮╲╲\n╱╱╱╱╰━━━╯╰━━┛╲╲",
    "┏━╮\n┃▔┃▂▂┏━━┓┏━┳━━━┓\n┃▂┣━━┻━╮┃┃▂┃▂┏━╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗━┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗━━━╮┃▔▔▔┃▔┏━╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗━╮\n┗━━━━━┻━━━━┻━━━┛",
    "┏┓┏━┳━┳━┳━┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗━┻━┛┗━┛┗━┛\n────­­­­­­­­­YOU────",
    "╦──╔╗─╗╔─╔ ─\n║──║║─║║─╠ ─\n╚═─╚╝─╚╝─╚ ─\n╦─╦─╔╗─╦╦   \n╚╦╝─║║─║║ \n─╩──╚╝─╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\\../') \n╔╝╚╗..( •.• ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭━╱▔▔▔▔╲━╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰━━╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭━╮▔▏┊┊▕▔╭━╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰━━━━╲╱━━━━╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­─────­­­­­­­­­YOU─────",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳━━┳━╮╭━┳━━╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰━━┻━━╯╰━━╯╰━━━╯",
    "┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊ \n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮ \n╭━╋━╋━╯┣╯┃┊┃╰╋━╯ \n╰━╯┊╰━━╯┊╰━┛┊╰━━",
]


__MODULE__ = "animasi"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴀɴɪᴍᴀꜱɪ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}loveyou</code> <b>ᴏʀ</b> <code>{0}dino</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ange</code> <b>ᴏʀ</b> <code>{0}kocok</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}kntl</code> <b>ᴏʀ</b> <code>{0}penis</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}heli</code> <b>ᴏʀ</b> <code>{0}tembak</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}bundir</code> <b>ᴏʀ</b> <code>{0}awk</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}y</code> <b>ᴏʀ</b> <code>{0}tank</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gabut</code> <b>ᴏʀ</b> <code>{0}terkadang</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ahh</code> <b>ᴏʀ</b> <code>{0}wlc</code>
            <i>coba aja sendiri</i>
              </blockquote>

"""


@PY.UBOT("loveyou")
async def lopeyo(client, message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    e = await message.edit(reply_text)


@PY.UBOT("hmm")
async def hmmm(client, message):
    e = await message.edit(
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭━━━━╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )


@PY.UBOT("kntl")
async def kntl(client, message):
    emoji = get_text(message)
    kontol = MEMES.GAMBAR_KONTOL
    if emoji:
        kontol = kontol.replace("⡀", emoji)
    e = await message.reply(kontol)


@PY.UBOT("penis")
async def pns(client, message):
    emoji = get_text(message)
    titid = MEMES.GAMBAR_TITIT
    if emoji:
        titid = titid.replace("😋", emoji)
    e = await message.edit(titid)


@PY.UBOT("heli")
async def helikopter(client, message):
    e = await message.edit(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


@PY.UBOT("tembak")
async def dornembak(client, message):
    e = await message.edit(
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n<b>Mau Jadi Pacarku Gak?!</b>",
    )


@PY.UBOT("bundir")
async def ngebundir(client, message):
    e = await message.edit(
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@PY.UBOT("awk")
async def awikwok(client, message):
    e = await message.edit(
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`",
    )


@PY.UBOT("y")
async def ysaja(client, message):
    e = await message.edit(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


@PY.UBOT("tank")
async def tank(client, message):
    e = await message.edit(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


@PY.UBOT("babi")
async def babi(client, message):
    e = await message.edit(
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@PY.UBOT("ange")
async def piciieess(client, message):
    e = await message.edit("<b>Ayanggg 😖</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Aku Ange 😫</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Ayuukk Picies Yang 🤤</b>")


@PY.UBOT("lipkol")
async def lipkoll(client, message):
    e = await message.edit("<b>Ayanggg 😖</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Kangeeen 👉👈</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Pingiinn Slipkool Yaaang 🥺👉👈</b>")


@PY.UBOT("nakal")
async def nakall(client, message):
    e = await message.edit("<b>Ayanggg ih🥺</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Nakal Banget Dah Ayang 🥺</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Aku Gak Like Ayang 😠</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Pokoknya Aku Gak Like Ih 😠</b>")


@PY.UBOT("piss")
async def peace(client: Client, message: Message):
    e = await message.edit(
        "┈┈┈┈PEACE MAN┈┈┈┈\n"
        "┈┈┈┈┈┈╭╮╭╮┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┗┛┣┳╮┈┈┈┈\n"
        "┈┈┈┈┈╭┻━━┓┃┃┈┈┈┈\n"
        "┈┈┈┈┈┃╲┏━╯┻┫┈┈┈┈\n"
        "┈┈┈┈┈╰╮╯┊┊╭╯┈┈┈┈\n",
    )


@PY.UBOT("spongebob")
async def spongebobss(client: Client, message: Message):
    e = await message.edit(
        "╲┏━┳━━━━━━━━┓╲╲\n"
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲\n"
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲\n"
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲\n"
        "╲┃◯┃╭╮╰╯┏━━━┳╯╲\n"
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲\n"
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲\n",
    )



@PY.UBOT("kocok")
async def kocokk(client, message):
    e = await message.edit("**KOCOKINNNN SAYANGG🥵**")
    await asyncio.sleep(0.6)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("**AH AH AH🥵**")
    await asyncio.sleep(0.5)
    await e.edit("**AH ENAK SAYANG😖**")
    await asyncio.sleep(0.5)
    await e.edit("**KOCOKIN LAGI SAYANG😣**")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("**MAU CROT SAYANG😫**")
    await asyncio.sleep(0.5)
    await e.edit("**AH AH AH😫**")
    await asyncio.sleep(0.5)
    await e.edit("**AKU CROTIN YA SAYANG😖**")
    await asyncio.sleep(0.5)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("🥵")
    await asyncio.sleep(0.5)
    await e.edit("8===✊D💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT**")
    await asyncio.sleep(0.5)
    await e.edit("**CROOTTTT AAAHHH.....**")
    await asyncio.sleep(0.5)
    await e.edit("**AHHH ENAKKKKK SAYANGGGG🥵🥵**")


@PY.UBOT("dino")
async def adadino(client: Client, message: Message):
    typew = await message.edit("`DIN DINNN.....`")
    await asyncio.sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    await asyncio.sleep(1)
    await typew.edit("`🧎🦖`")
    await asyncio.sleep(2)
    await typew.edit("`-TAMAT-`")


@PY.UBOT("ajg")
async def anjg(client, message):
    e = await message.edit(
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )


@PY.UBOT("nangis")
async def nangishua(client, message):
    e = await message.edit("**Kamu Jahat**")
    await asyncio.sleep(0.6)
    await e.edit("**Jahat Banget**")
    await asyncio.sleep(0.6)
    await e.edit("أ‿أ")
    await asyncio.sleep(0.4)
    await e.edit("╥﹏╥")
    await asyncio.sleep(0.4)
    await e.edit("(;﹏;)")
    await asyncio.sleep(0.4)
    await e.edit("(ToT)")
    await asyncio.sleep(0.4)
    await e.edit("(┳Д┳)")
    await asyncio.sleep(0.4)
    await e.edit("(ಥ﹏ಥ)")
    await asyncio.sleep(0.4)
    await e.edit("（；へ：）")
    await asyncio.sleep(0.4)
    await e.edit("(T＿T)")
    await asyncio.sleep(0.4)
    await e.edit("（πーπ）")
    await asyncio.sleep(0.4)
    await e.edit("(Ｔ▽Ｔ)")
    await asyncio.sleep(0.4)
    await e.edit("(⋟﹏⋞)")
    await asyncio.sleep(0.4)
    await e.edit("（ｉДｉ）")
    await asyncio.sleep(0.4)
    await e.edit("(´Д⊂ヽ")
    await asyncio.sleep(0.4)
    await e.edit("(;Д;)")
    await asyncio.sleep(0.4)
    await e.edit("（>﹏<）")
    await asyncio.sleep(0.4)
    await e.edit("(TдT)")
    await asyncio.sleep(0.4)
    await e.edit("(つ﹏⊂)")
    await asyncio.sleep(0.4)
    await e.edit("༼☯﹏☯༽")
    await asyncio.sleep(0.4)
    await e.edit("(ノ﹏ヽ)")
    await asyncio.sleep(0.4)
    await e.edit("(ノAヽ)")
    await asyncio.sleep(0.4)
    await e.edit("(╥_╥)")
    await asyncio.sleep(0.4)
    await e.edit("(T⌓T)")
    await asyncio.sleep(0.4)
    await e.edit("(༎ຶ⌑༎ຶ)")
    await asyncio.sleep(0.4)
    await e.edit("(☍﹏⁰)｡")
    await asyncio.sleep(0.4)
    await e.edit("(ಥ_ʖಥ)")
    await asyncio.sleep(0.4)
    await e.edit("(つд⊂)")
    await asyncio.sleep(0.4)
    await e.edit("(≖͞_≖̥)")
    await asyncio.sleep(0.4)
    await e.edit("(இ﹏இ`｡)")
    await asyncio.sleep(0.4)
    await e.edit("༼ಢ_ಢ༽")
    await asyncio.sleep(0.4)
    await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")
    await asyncio.sleep(0.4)
    await e.edit("**Jahat Jahat Jahat**")

@PY.UBOT("ayang")
async def payang(client, message):
    e = await message.edit("<b>I LOVE YOU SAYANG💗💕</b>")
    await asyncio.sleep(1)
    await e.edit("<b>❤🧡💛💚</b>")
    await asyncio.sleep(1)
    await e.edit("<b>🧡💛💚💙</b>")
    await asyncio.sleep(1)
    await e.edit("<b>💛💚💙💜</b>")
    await asyncio.sleep(1)
    await e.edit("<b>💚💙💜🤎</b>")
    await asyncio.sleep(1)
    await e.edit("<b>💙💜🤎🖤</b>")
    await asyncio.sleep(1)
    await e.edit("<b>💜🤎🖤🤍</b>")
    await asyncio.sleep(1)
    await e.edit("<b>SAYANG KAMU💗💗💗</b>")
    await asyncio.sleep(1)
    await e.edit("<b>CINTA KAMU💝💝💝</b>")
    await asyncio.sleep(1)
    await e.edit("<b>SAYANG</b>")
    await asyncio.sleep(1)
    await e.edit("<b>KAMU</b>")
    await asyncio.sleep(1)
    await e.edit("<b>SELAMANYA</b>")
    await asyncio.sleep(1)
    await e.edit("<b>MUAHHH</b>")
    await asyncio.sleep(1)
    await e.edit("<b>😚😚😚</b>")
    await asyncio.sleep(1)
    await e.edit("<b>HEHE</b>")
    await asyncio.sleep(1)
    await e.edit("<b>🥰🥰🥰</b>")
    await asyncio.sleep(1)
    await e.edit("<b>💕💓💗</b>")
    await asyncio.sleep(1)
    await e.edit("<b>💖💗💓</b>")
    await asyncio.sleep(1)
    await e.edit("<b>LOVE YOU💝</b>")

@PY.UBOT("fucek")
async def pucek(client, message):
    e = await message.edit(
                           "░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░\n"
                           "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                           "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                           "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                           "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
                           "██████▄███▄████░░███▄░░░░░░░\n"
                           "▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░\n"
                           "▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░\n"
                           "▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░\n"
                           "▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░\n"
                           "▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░\n"
                           "▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░\n")
        

@PY.UBOT("wlc")
async def ywelcom(client, message):
    e = await message.edit("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
                         "───█▒▒░░░░░░░░░▒▒█───\n"
                         "────█░░█░░░░░█░░█────\n"
                         "─▄▄──█░░░▀█▀░░░█──▄▄─\n"
                         "█░░█─▀▄░░░░░░░▄▀─█░░█\n"
                         "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                         "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
                         "█░░║║║╠─║─║─║║║║║╠─░░█\n"
                         "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
                         "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
        

@PY.UBOT("gabut")
async def gabut(_, m: Message):
    e = await edit_or_reply(
        m, "`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🚶                                 🐢")
    await e.edit("`AHHH MANTAP`")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("😂")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("`GABUT`")



@PY.UBOT("terkadang")
async def terkadang(client, message):
    e = await message.edit("**Terkadang**")
    sleep(3)
    await e.edit("**Mencintai Seseorang**")
    sleep(3)
    await e.edit("**Hanya Akan Membuang Waktumu**")
    sleep(3)
    await e.edit("**Ketika Waktumu Habis**")
    sleep(3)
    await e.edit("**Tambah Aja 5000**")
    sleep(3)
    await e.edit("**Bercanda**")


#@PY.UBOT("ayang")
#async def payang(client, message):
    #e = await message.edit("<blockquote><b>I LOVE YOU SAYANG💗💕</b</blockquote>>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>❤🧡💛💚</b></blockquote>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>🧡💛💚💙</b></blockquote>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>💛💚💙💜</b></blockquote>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>💚💙💜🤎</b></blockquote>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>💙💜🤎🖤</b></blockquote>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>💜🤎🖤🤍</b></blockquote>")
    #await asyncio.sleep(1)
    #await e.edit("<blockquote><b>SAYANG KAMU💗💗💗</b></blockquote>")

@PY.UBOT("love")
async def love(client, message):
    e = await message.edit("<blockquote>`\n(\\_/)`" "`\n(●_●)`" "\n />❤️ **Ini Buat Kamu**</blockquote>")
    await asyncio.sleep(2)
    await e.edit("<blockquote>`\n(\\_/)`" "\n(●_●)" "\n/>💔  **Aku Ambil Lagi**</blockquote>")
    await asyncio.sleep(2)
    await e.edit("<blockquote>`\n(\\_/)`" "`\n(●_●)`" "\n💔<\\  **Terimakasih**</blockquote>")

@PY.UBOT("nih")
async def nahlove(client, message):
    e = await message.edit("<blockquote>`\n(\\_/)`" "`\n(●_●)`" "\n />🩷 **Ini Buat Kamu**</blockquote>")
    await asyncio.sleep(2)
    await e.edit("<blockquote>`\n(\\_/)`" "`\n(●_●)`" "\n🩷<\\  **Tapi Boong HeHeHe**</blockquote>")

@PY.UBOT("ahh")
async def nakall(client, message):
    e = await message.edit("<b>Ahhhh Yamete</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Nee Chann Yamete</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Yamete😣</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Yamete😩</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Yamete🥵</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Yamete Kudasai</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Baka Baka Baka</b>")

@PY.UBOT("deak")
async def nakall(client, message):
    e = await message.edit("<b>Menghapus Akun Busuk Mu</b>")
    await asyncio.sleep(1)
    await e.edit("<b>Memproses 10%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 11%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 12%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 13%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 14%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 15%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 16%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 17%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 18%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 19%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 20%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 21%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 22%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 23%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 24%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 25%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 26%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 27%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 28%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 29%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 30%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 31%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 32%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 33%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 34%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 35%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 36%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 37%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 38%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 39%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 40%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 41%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 42%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 43%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 44%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 45%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 46%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 47%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 48%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 49%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 50%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 51%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 52%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 53%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 54%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 55%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 56%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 57%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 58%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 59%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 60%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 61%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 62%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 63%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 64%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 65%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 66%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 67%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 68%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 69%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 70%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 71%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 72%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 73%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 74%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 75%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 76%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 77%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 78%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 79%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 80%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 81%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 82%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 83%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 84%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 85%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 86%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 87%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 88%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 89%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 90%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 91%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 92%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 93%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 94%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 95%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 96%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 97%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 98%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 99%</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Memproses 100%</b>")
    await asyncio.sleep(2)
    await e.edit("<b>Deak Akun Sukses</b>")


@PY.UBOT("Riport")
async def nakall(client, message):
    e = await message.edit("<b>Memproses Laporan Anda</b>")
    await asyncio.sleep(1)
    await e.edit("<b>Laporan terkirim</b>")
    await asyncio.sleep(0.2)
    await e.edit("<b>Trimakasih Telah Melaporkan\n Laporan Akan Segera Ditangani Pihak Telegram</b>")
