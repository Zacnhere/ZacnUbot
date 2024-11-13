from PyroUbot import *
import os
import io
import random
import requests
from OpenAi import OpenAi
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message


__MODULE__ = "Ai"
__HELP__ = """
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ask</code>
      <i>buat pertanyaan</i>
      <b>ᴄᴏɴᴛᴏʜ:</b> <code>{0}ask</code> <i>dimana letak Antartika</i>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}photo</code>
      <i>buat foto dengan ai</i>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stt</code>
      <i>merubah text menjadi pesan suara</i>
      </blockquote>
"""


@PY.UBOT("ask")
async def _(client, message):
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs...</code>")
    args = get_text(message)
    if not args:
        return await Tm.edit(f"<b><code>{message.text}</code> [ᴘᴇʀᴛᴀɴʏᴀᴀɴ]</b>")
    try:
        response = await OpenAi.ChatGPT(args)
        if int(len(str(response))) > 4096:
            with io.BytesIO(str.encode(str(response))) as out_file:
                out_file.name = "openAi.txt"
                await message.reply_document(
                    document=out_file,
                )
                return await Tm.delete()
        else:
            msg = message.reply_to_message or message
            await client.send_message(
                message.chat.id, response, reply_to_message_id=msg.id
            )
            return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()


@PY.UBOT("photo")
async def _(client, message):
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs...</code>")
    if len(message.command) < 2:
        return await Tm.edit(f"<b><code>{message.text}</code> [ǫᴜᴇʀʏ]</b>")
    try:
        response = await OpenAi.ImageDalle(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await client.send_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await Tm.delete()
    except Exception as error:
        await message.reply(error)
        return await Tm.delete()


@PY.UBOT("stt")
async def _(client, message):
    # Memberi notifikasi bahwa proses sedang berjalan
    Tm = await message.reply("<code>Memproses...</code>")
    reply = message.reply_to_message
    
    # Periksa apakah ada pesan yang di-reply dan apakah berisi media
    if reply and (reply.voice or reply.audio or reply.video):
        # Unduh file media yang di-reply
        file = await client.download_media(
            message=reply,
            file_name=f"sst_{reply.id}",
        )
        
        # Tentukan nama file audio yang akan diubah ke format mp3
        audio_file = f"{file}.mp3"
        
        # Konversi ke format mp3 jika file bukan mp3 (misalnya dari pesan suara atau video)
        if not file.endswith(".mp3"):
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {audio_file}"
            await run_cmd(cmd)
            os.remove(file)  # Hapus file asli setelah konversi
        else:
            audio_file = file  # Jika sudah mp3, langsung gunakan file tersebut
        
        # Proses transkripsi menggunakan Whisper
        try:
            response = await OpenAi.SpeechToText(audio_file)
        except Exception as error:
            # Jika terjadi error, kirim pesan error
            await message.reply(f"Error: {str(error)}")
            return await Tm.delete()
        finally:
            # Bersihkan file audio setelah selesai
            os.remove(audio_file)
        
        # Kirim hasil transkripsi, atau sebagai dokumen jika terlalu panjang
        if len(response) > 4096:
            with io.BytesIO(response.encode()) as out_file:
                out_file.name = "transcription.txt"
                await message.reply_document(document=out_file)
        else:
            msg = reply or message
            await client.send_message(
                message.chat.id, response, reply_to_message_id=msg.id
            )
        
        # Hapus pesan notifikasi setelah selesai
        return await Tm.delete()
    
    # Jika tidak ada balasan yang berisi media, beri informasi ke pengguna
    return await Tm.edit(
        f"<b>Gunakan perintah ini sebagai balasan pada pesan suara, audio, atau video</b>"
      )
  
