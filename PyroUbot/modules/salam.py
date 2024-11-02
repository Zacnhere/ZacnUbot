from time import sleep
from PyroUbot import *

__MODULE__ = "salam"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀʟᴀᴍ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}pp</code> <b>ᴏʀ</b> <code>{0}hi</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}l</code> <b>ᴏʀ</b> <code>{0}ass</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}h</code> <b>ᴏʀ</b> <code>{0}j</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}b</code> <b>ᴏʀ</b> <code>{0}s</code>
              <i>coba aja sendiri</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}o</code> <b>ᴏʀ</b> <code>{0}d</code>
              <i>coba aja sendiri</i>
              </blockquote>
"""



@PY.UBOT("pp")
async def assalamualaikum_warohmatullahi_wabarokatuh(client, message):
    await client.send_message(
        message.chat.id,
        "**Assalamualaikum Warahmatullahi Wabarakatuh**",
        reply_to_message_id=(message.reply_to_message or message).id,
    )
    await message.delete()


@PY.UBOT("hi")
async def hai_salken(client, message):
    me = await client.get_me()
    reply_msg = await edit_or_reply(message, f"**Haii Salken Saya {me.first_name} {me.last_name or ''}**")
    sleep(3)
    await reply_msg.edit("**Assalamualaikum...**")


@PY.UBOT("l")
async def waalaikumsalam(client, message):
    await client.send_message(
        message.chat.id, "**Wa'alaikumsalam**", reply_to_message_id=(message.reply_to_message or message).id
    )
    await message.delete()


@PY.UBOT("a")
async def assalamualaikum(client, message):
    me = await client.get_me()
    reply_msg = await edit_or_reply(message, f"**siapasi paling ganteng kalo bukan {me.first_name} {me.last_name or ''}**")
    sleep(4)
    await reply_msg.edit("**ngapa lu gasuka!!??**")


@PY.UBOT("j")
async def jaka_sembung(client, message):
    reply_msg = await edit_or_reply(message, "**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await reply_msg.edit("**NIMBRUNG GOBLOKK!!!🔥**")


@PY.UBOT("h")
async def hallo_kimakk(client, message):
    me = await client.get_me()
    reply_msg = await edit_or_reply(message, f"**Hallo KIMAAKK SAYA {me.first_name} {me.last_name or ''}**")
    sleep(2)
    await reply_msg.edit("**LU SEMUA NGENTOT 🔥**")


@PY.UBOT("ass")
async def salam_dulu(client, message):
    reply_msg = await edit_or_reply(message, "**Salam Dulu Biar Sopan**")
    sleep(2)
    await reply_msg.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


@PY.UBOT("b")
async def beli_lego(client, message):
    reply_msg = await edit_or_reply(message, "**KE PASAR BELI LEGO**")
    sleep(3)
    await reply_msg.edit("**DASAR LU BEGO!!!🔥**")


@PY.UBOT("s")
async def beli_ketan(client, message):
    reply_msg = await edit_or_reply(message, "**KE PASAR BELI KETAN**")
    sleep(3)
    await reply_msg.edit("**DASAR ANAK SETAN!!!🔥**") 


@PY.UBOT("o")
async def obusetdah(client, message):
    reply_msg = await edit_or_reply(message, "**ADA KESET ADA WADAH**")
    sleep(3)
    await reply_msg.edit("**BUSETTTT DAH....!!!**")


@PY.UBOT("d")
async def duh_berteduh(client, message):
    reply_msg = await edit_or_reply(message, "**BERTEDUH BAWA KRESEK**")
    sleep(3)
    await reply_msg.edit("**DUHH...BRENGSEKK!!!**")


