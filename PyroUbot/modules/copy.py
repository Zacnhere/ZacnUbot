import asyncio
import os
import logging
import re
from gc import get_objects
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from PyroUbot import *



__MODULE__ = "copy"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴄᴏᴘʏ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}copy</code> [ᴜʀʟ]
   <i>untuk mengambil konten channel publik</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cprivate</code> [ᴜʀʟ]
   <i>untuk mengambil konten channel private</i>
   <i>note : hanya untuk owner bot</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}colong</code> [ʀᴇᴘʟʏ]
   <i>untuk mengambil media timer dan menyimpan ke pesan tersimpan</i>

<b>ɴᴏᴛᴇ:</b>
<i>gunakan fitur ini dengan sebaik - baiknya\njangan di salah gunakan untuk hal negative</i>
</blockquote>   
"""


@PY.BOT("copy")
async def copy_bot_msg(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if message.from_user.id not in ubot._get_my_id:
        return
    Tm = await message.reply(f"<b>{prs}ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b>{ggl}<code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    msg_id = int(link.split("/")[-1])
    chat = str(link.split("/")[-2])
    try:
        get = await client.get_messages(chat, msg_id)
        await get.copy(message.chat.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(error)


COPY_ID = {}


async def download_media_copy(get, client, infomsg, message):
    msg = message.reply_to_message or message
    text = get.caption or ""
    if get.photo:
        media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴘʜᴏᴛᴏ",
                get.photo.file_id,
            ),
        )
        await client.send_photo(
            message.chat.id,
            media,
            caption=text,
            reply_to_message_id=msg.id,
        )
        await infomsg.delete()
        os.remove(media)

    elif get.animation:
         media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴɪᴍᴀᴛɪᴏɴ",
                get.animation.file_id,
            ),
         )
         await client.send_animation(
            message.chat.id,
            animation=media,
            caption=text,
            reply_to_message_id=msg.id,
         )
         await infomsg.delete()
         os.remove(media)

    elif get.voice:
         media = await client.download_media(
            get,
            progress=progress,
            progress_args=(infomsg, time(), "ᴅᴏᴡɴʟᴏᴀᴅ ᴠᴏɪᴄᴇ", get.voice.file_id),
         )
         await client.send_voice(
            message.chat.id,
            voice=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
         await infomsg.delete()
         os.remove(media)

    elif get.audio:
         media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ",
                get.audio.file_id,
            ),
         )
         thumbnail = await client.download_media(get.audio.thumbs[-1]) or None
         await client.send_audio(
            message.chat.id,
            audio=media,
            duration=get.audio.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
         )
         await infomsg.delete()
         os.remove(media)
         os.remove(thumbnail)

    elif get.document:
         media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴅᴏᴄᴜᴍᴇɴᴛ",
                get.document.file_id,
            ),
         )
         await client.send_document(
            message.chat.id,
            document=media,
            caption=text,
            reply_to_message_id=msg.id,
        )
         await infomsg.delete()
         os.remove(media)

    elif get.video:
         media = await client.download_media(
            get,
            progress=progress,
            progress_args=(
                infomsg,
                time(),
                "ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ",
                get.video.file_name,
            ),
         )
         thumbnail = await client.download_media(get.video.thumbs[-1]) or None
         await client.send_video(
            message.chat.id,
            video=media,
            duration=get.video.duration,
            caption=text,
            thumb=thumbnail,
            reply_to_message_id=msg.id,
         )
         await infomsg.delete()
         os.remove(media)
         os.remove(thumbnail)


@PY.UBOT("copy")
async def copy_ubot_msg(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    msg = message.reply_to_message or message
    infomsg = await message.reply(f"<b>{prs}ꜱᴇᴅᴀɴɢ ᴍᴇɴɢᴄᴏᴘʏ ᴍᴇᴅɪᴀ</b>")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b>{ggl}<code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
            try:
                get = await client.get_messages(chat, msg_id)
                try:
                    await get.copy(message.chat.id, reply_to_message_id=msg.id)
                    await infomsg.delete()
                except Exception:
                    await download_media_copy(get, client, infomsg, message)
            except Exception as e:
                await infomsg.edit(str(e))
        else:
            chat = str(link.split("/")[-2])
            try:
                get = await client.get_messages(chat, msg_id)
                await get.copy(message.chat.id, reply_to_message_id=msg.id)
                await infomsg.delete()
            except Exception:
                try:
                    text = f"get_msg {id(message)}"
                    x = await client.get_inline_bot_results(bot.me.username, text)
                    results = await client.send_inline_bot_result(
                        message.chat.id,
                        x.query_id,
                        x.results[0].id,
                        reply_to_message_id=msg.id,
                    )
                    COPY_ID[client.me.id] = int(results.updates[0].id)
                    await infomsg.delete()
                except Exception as error:
                    await infomsg.edit(f"{str(error)}")
    else:
        await infomsg.edit(f"<b>{ggl}ᴍᴀsᴜᴋᴋɪɴ ʟɪɴᴋ ʏᴀɴɢ ᴠᴀʟɪᴅ</b>")


@PY.INLINE("^get_msg")
async def copy_inline_msg(client, inline_query):
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get message!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="🔐 ʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ 🔐",
                                    callback_data=f"copymsg_{int(inline_query.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        "<b>🔒 ᴋᴏɴᴛᴇɴ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴀᴍʙɪʟ ʙᴇʀsɪꜰᴀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅ\n\n✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ</b>"
                    ),
                )
            )
        ],
    )


@PY.CALLBACK("^copymsg")
async def copy_callback_msg(client, callback_query):
    try:
        q = int(callback_query.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        await m._client.unblock_user(bot.me.username)
        await callback_query.edit_message_text("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
        copy = await m._client.send_message(
            bot.me.username, f"/copy {m.text.split()[1]}"
        )
        msg = m.reply_to_message or m
        await asyncio.sleep(1.5)
        await copy.delete()
        async for get in m._client.search_messages(bot.me.username, limit=1):
            await m._client.copy_message(
                m.chat.id, bot.me.username, get.id, reply_to_message_id=msg.id
            )
            await m._client.delete_messages(m.chat.id, COPY_ID[m._client.me.id])
            await get.delete()
    except Exception as error:
        await callback_query.edit_message_text(f"<code>{error}</code>")


@PY.UBOT("cprivate")
@PY.OWNER
async def copy_private_content(client: Client, message: Message):
    """Menyalin konten media (foto/video) dari channel atau grup private."""
    reply = message.reply_to_message
    if not reply or not reply.text:
        await message.reply_text("⚠️ Mohon reply ke pesan yang berisi link dari grup atau channel private.")
        return

    link = reply.text.strip()
    if not link.startswith("https://t.me/c/") and not link.startswith("https://t.me/"):
        await message.reply_text("⚠️ Link tidak valid. Harap gunakan link dari grup atau channel private.")
        return

    try:
        # Ekstrak chat_id & msg_id dari link
        parts = link.split("/")
        if len(parts) < 3:
            await message.reply_text("⚠️ Format link salah.")
            return

        chat_id = int("-100" + parts[-2])  # ID Channel atau Grup
        msg_id = int(parts[-1])  # ID Pesan

        await message.reply_text("⏳ Memproses, harap tunggu...")

        # Ambil pesan dari grup atau channel private
        get = await client.get_messages(chat_id, msg_id)

        if not get or not get.media:
            await message.reply_text("❌ Tidak ada media dalam pesan ini.")
            return

        # Jika ada banyak media dalam satu pesan
        if get.media_group_id:
            media_group = await client.get_media_group(chat_id, msg_id)

            files = []
            for media in media_group:
                file_path = await client.download_media(media)
                if file_path:
                    files.append(file_path)

            # Kirim ulang media ke pengguna
            for file in files:
                await client.send_document(
                    chat_id=message.chat.id,
                    document=file,
                    caption="✅ Berhasil menyalin konten private."
                )
                os.remove(file)  # Hapus file setelah dikirim

        else:
            # Jika hanya satu media
            media = await client.download_media(get)
            if not media:
                await message.reply_text("❌ Gagal mengunduh media.")
                return

            await client.send_document(
                chat_id=message.chat.id,
                document=media,
                caption="✅ Berhasil menyalin konten private."
            )

            os.remove(media)  # Hapus file setelah dikirim

    except Exception as e:
        await message.reply_text(f"❌ Gagal mengambil media: {str(e)}")
