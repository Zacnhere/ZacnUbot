import asyncio
import os

from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from PyroUbot import *

__MODULE__ = "convert"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴄᴏɴᴠᴇʀᴛ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toanime</code>
   <i>untuk merubah photo/sticker/gif menjadi gambar anime</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toimg</code>
   <i>untuk merubah sticker/gif menjadi photo</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tosticker</code>
   <i>untuk merubah foto menjadi sticker</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}togif</code>
   <i>untuk merubah sticker menjadi gif</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}toaudio</code>
   <i>untuk merubah video menjadi audio mp3</i>
   </blockquote>  
"""



@PY.UBOT("toanime")
async def _(client, message):
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>")
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                file = "foto"
                get_photo = message.reply_to_message.photo.file_id
            elif message.reply_to_message.sticker:
                file = "sticker"
                get_photo = await dl_pic(client, message.reply_to_message)
            elif message.reply_to_message.animation:
                file = "gift"
                get_photo = await dl_pic(client, message.reply_to_message)
            else:
                return await Tm.edit(
                    "<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ <code>ᴘʜᴏᴛᴏ/sᴛʀɪᴋᴇʀ/ɢɪᴛ</code></b>"
                )
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                file = "foto profil"
                get = await client.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await dl_pic(client, photo)
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                "<b>ʙᴀʟᴀs ᴋᴇ ꜰᴏᴛᴏ ᴅᴀɴ sᴀʏᴀ ᴀᴋᴀɴ ᴍᴇʀᴜʙᴀʜ ꜰᴏᴛᴏ ᴀɴᴅᴀ ᴍᴇɴᴊᴀᴅɪ ᴀɴɪᴍᴇ</b>"
            )
        else:
            try:
                file = "foto"
                get = await client.get_chat(message.command[1])
                photo = get.photo.big_file_id
                get_photo = await dl_pic(client, photo)
            except Exception as error:
                return await Tm.edit(error)
    await Tm.edit("<b>sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs...</b>")
    await client.unblock_user("@qq_neural_anime_bot")
    send_photo = await client.send_photo("@qq_neural_anime_bot", get_photo)
    await asyncio.sleep(30)
    await send_photo.delete()
    await Tm.delete()
    info = await client.resolve_peer("@qq_neural_anime_bot")
    anime_photo = []
    async for anime in client.search_messages(
        "@qq_neural_anime_bot", filter=MessagesFilter.PHOTO
    ):
        anime_photo.append(
            InputMediaPhoto(
                anime.photo.file_id, caption=f"<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ: {bot.me.mention}</b>"
            )
        )
    if anime_photo:
        await client.send_media_group(
            message.chat.id,
            anime_photo,
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))

    else:
        await client.send_message(
            message.chat.id,
            f"<b>ɢᴀɢᴀʟ ᴍᴇʀᴜʙᴀʜ {file} ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ</b>",
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))


@PY.UBOT("toimg")
async def _(client, message):
    _msg = "<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>"
    Tm = await message.reply(_msg)
  
    try:
        file_io = await dl_pic(client, message.reply_to_message)
        file_io.name = "sticker.png"
        await client.send_photo(
            message.chat.id,
            file_io,
            reply_to_message_id=message.id,
        )
        await Tm.delete()
    except Exception as e:
        await Tm.delete()
        return await client.send_message(
            message.chat.id,
            e,
            reply_to_message_id=message.id,
        )


@PY.UBOT("tosticker")
async def _(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            return await message.reply_text("<b>ʀᴇᴘʟʏ ᴋᴇ ꜰᴏᴛᴏ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴋᴇ sᴛɪᴄᴋᴇʀ</b>")
        sticker = await client.download_media(
            message.reply_to_message.photo.file_id,
            f"sticker_{message.from_user.id}.webp",
        )
        await message.reply_sticker(sticker)
        os.remove(sticker)
    except Exception as e:
        await message.reply_text(str(e))


@PY.UBOT("togif")
async def _(client, message):
    TM = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if not message.reply_to_message.sticker:
        return await TM.edit("<b>ʙᴀʟᴀs ᴋᴇ sᴛɪᴋᴇʀ...</b>")
    await TM.edit("<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ sᴛɪᴄᴋᴇʀ. . .</b>")
    file = await client.download_media(
        message.reply_to_message,
        f"Gift_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await TM.delete()
    except Exception as error:
        await TM.edit(error)


@PY.UBOT("toaudio")
async def _(client, message):
    replied = message.reply_to_message
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
    if not replied:
        return await Tm.edit("<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴠɪᴅᴇᴏ</b>")
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit("<b>ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴠɪᴅᴇᴏ . . ..</b>")
        file = await client.download_media(
            message=replied,
            file_name=f"toaudio_{replied.id}",
        )
        out_file = f"{file}.mp3"
        try:
            await Tm.edit("<b>ᴍᴇɴᴄᴏʙᴀ ᴇᴋsᴛʀᴀᴋ ᴀᴜᴅɪᴏ. ..</b>")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await Tm.edit("<b>ᴜᴘʟᴏᴀᴅɪɴɢ ᴀᴜᴅɪᴏ . . .</b>")
            await client.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            os.remove(file)
            await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        return await Tm.edit("<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴠɪᴅᴇᴏ</b>")


@PY.UBOT("colong")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    dia = message.reply_to_message
    if not dia:
        return await message.reply(f"{ggl}<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴍᴇᴅɪᴀ</b>")
    anjing = dia.caption or ""
    Tm = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ...</b>")
    if dia.photo:
        if message.reply_to_message.photo.file_size > 10000000:
            return await Tm.edit(f"{ggl}<b>ꜰɪʟᴇ ᴅɪ ᴀᴛᴀs 10ᴍʙ ᴛɪᴅᴀᴋ ᴅɪ ɪᴢɪɴᴋᴀɴ</b>")
        anu = await client.download_media(dia)
        await client.send_photo(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.video:
        if message.reply_to_message.video.file_size > 10000000:
            return await Tm.edit(f"{ggl}<b>ꜰɪʟᴇ ᴅɪ ᴀᴛᴀs 10ᴍʙ ᴛɪᴅᴀᴋ ᴅɪ ɪᴢɪɴᴋᴀɴ</b>")
        anu = await client.download_media(dia)
        await client.send_video(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.audio:
        if message.reply_to_message.audio.file_size > 10000000:
            return await Tm.edit(f"{ggl}<b>ꜰɪʟᴇ ᴅɪ ᴀᴛᴀs 10ᴍʙ ᴛɪᴅᴀᴋ ᴅɪ ɪᴢɪɴᴋᴀɴ</b>")
        anu = await client.download_media(dia)
        await client.send_audio(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.voice:
        if message.reply_to_message.voice.file_size > 10000000:
            return await Tm.edit(f"{ggl}<b>ꜰɪʟᴇ ᴅɪ ᴀᴛᴀs 10ᴍʙ ᴛɪᴅᴀᴋ ᴅɪ ɪᴢɪɴᴋᴀɴ</b>")
        anu = await client.download_media(dia)
        await client.send_voice(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.document:
        if message.reply_to_message.document.file_size > 10000000:
            return await Tm.edit(f"{ggl}<b>ꜰɪʟᴇ ᴅɪ ᴀᴛᴀs 10ᴍʙ ᴛɪᴅᴀᴋ ᴅɪ ɪᴢɪɴᴋᴀɴ</b>")
        anu = await client.download_media(dia)
        await client.send_document(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    else:
        return await Tm.reply(f"{ggl}<b>sᴇᴘᴇʀᴛɪɴʏᴀ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ</b>")


@PY.UBOT("ambil")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    dia = message.reply_to_message
    if not dia:
        return await message.reply(f"{ggl}<b>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴍᴇᴅɪᴀ</b>")
    anjing = dia.caption or ""
    Tm = await message.reply(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ...</b>")

    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()

    else:
        return await Tm.reply(f"{ggl}<b>sᴇᴘᴇʀᴛɪɴʏᴀ ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ</b>")


@PY.UBOT("ambilsekali")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    dia = message.reply_to_message
    if not dia:
        return await message.reply(f"{ggl}<b>ʙᴀʟᴀs ᴋᴇ ᴘᴇꜱᴀɴ ᴍᴇᴅɪᴀ ꜱᴇᴋᴀʟɪ ʟɪʜᴀᴛ</b>")
    Tm = await message.reply(f"{prs}<b>ᴍᴇɴʏɪᴍᴘᴀɴ ᴋᴏɴᴛᴇɴ ꜱᴇᴋᴀʟɪ ʟɪʜᴀᴛ...</b>")
    try:
        file = await client.download_media(dia)
        if dia.photo:
            await client.send_photo("me", file, caption="Disimpan dari view-once")
        elif dia.video:
            await client.send_video("me", file, caption="Disimpan dari view-once")
        else:
            await client.send_document("me", file, caption="Disimpan dari view-once")
        os.remove(file)
        await message.delete()
        await Tm.delete()
    except Exception as e:
        return await Tm.edit(f"{ggl}<b>ɢᴀɢᴀʟ ᴍᴇɴʏɪᴍᴘᴀɴ: {e}</b>")
