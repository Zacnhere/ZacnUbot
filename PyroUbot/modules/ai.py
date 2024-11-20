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
async def _(client, message):
    random_number = random.randint(1000000, 9999999)
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply(
                f"Give me a question fot chatgpt!"
            )
        else:
            prs = await message.reply(f"Processing...")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/openai-chat?text={a}&apikey=enakaja')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"{x}"
                    )
                else:
                    return await prs.edit("No 'results' key found in the response!")
            except KeyError:
                return await prs.edit("Error accessing the response!")
    except Exception as e:
        return await prs.edit(f"Error!\n{e}")


@PY.UBOT("photo")
async def _(client, message):
    random_number = random.randint(1000000, 9999999)  
    try:
        if len(message.command) < 2:
            return await message.reply(f"Give me a name for an image!")
        
        prs = await message.reply(f"Processing...")
        search_query = message.text.replace(" ", ",")
        async with aiohttp.ClientSession() as session:
            try:
                url = f'https://api.botcahx.eu.org/api/maker/text2img?text={search_query}&apikey=enakaja'
                async with session.get(url) as response:
                    if response.status == 200:
                        image_path = f"temp_image_{random_number}.png"
                        with open(image_path, 'wb') as f:
                            f.write(await response.read())

                        await prs.delete()
                        await message.reply_photo(image_path)
                        os.remove(image_path)
                    else:
                        await prs.edit(f"Error: Received non-200 response status {response.status}")
            except Exception as e:
                return await prs.edit(f"Error during API request!\n{e}")

    except Exception as e:
        return await prs.edit(f"Error!\n{e}")


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
