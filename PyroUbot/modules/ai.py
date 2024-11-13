from PyroUbot import *
import os
import io
import random
import requests
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
async def chat_gpt(client, message):
    prs = await EMO.PROSES(client)
    xbot = await EMO.UBOT(client)
    ggl = await EMO.GAGAL(client)
   
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                f"<blockquote>{ggl}<b>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ :</b> <code>ask bagaimana membuat donat?</code></blockquote>"
            )
        else:
            prs = await message.reply_text(f"{prs}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ....</b>")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/openai-chat?text={a}&apikey=enakaja')

            try:
                if "answer" in response.json():
                    x = response.json()["answer"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>\n\n<blockquote>{xbot} ᴅɪᴊᴀᴡᴀʙ ᴏʟᴇʜ {bot.me.mention}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")


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
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏsᴇs...</code>")
    reply = message.reply_to_message
    if reply:
        if reply.voice or reply.audio or reply.video:
            file = await client.download_media(
                message=message.reply_to_message,
                file_name=f"sst_{message.reply_to_message.id}",
            )
            audio_file = f"{file}.mp3"
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {audio_file}"
            await run_cmd(cmd)
            os.remove(file)
            try:
                response = await OpenAi.SpeechToText(audio_file)
            except Exception as error:
                await message.reply(error)
                return await Tm.delete()
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
        else:
            return await Tm.edit(
                f"<b><code>{message.text}</code> [ʀᴇᴘʟʏ ᴠᴏɪᴄᴇ_ᴄʜᴀᴛ/ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ]</b>"
            )



@PY.UBOT("stt")
async def voice_tools(client, message):
    TM = await message.reply("<b>Sedang memproses audio...</b>")

    if not message.reply_to_message or not message.reply_to_message.voice:
        return await TM.edit("<b>Reply vnya</b>")

recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(voice_file) as source:
            audio = recognizer.record(source)  
            text = recognizer.recognize_google(audio)  
            await TM.edit(f"{text}")
    except sr.UnknownValueError:
        await TM.edit("-")
    except sr.RequestError:
        await TM.edit("-")
    except Exception as e:
        await TM.edit(f"Error: {str(e)}")
    
    try:
        os.remove(voice_file)
    except FileNotFoundError:
        pass

voice_file = await client.download_media(message.reply_to_message.voice)

recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(voice_file) as source:
            audio = recognizer.record(source)  
            text = recognizer.recognize_google(audio)  
            await TM.edit(f"{text}")
    except sr.UnknownValueError:
        await TM.edit("-")
    except sr.RequestError:
        await TM.edit("-")
    except Exception as e:
        await TM.edit(f"Error: {str(e)}")
    
    try:
        os.remove(voice_file)
    except FileNotFoundError:
        pass
