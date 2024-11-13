from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

API_KEY = "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"

__MODULE__ = "Ai"
__HELP__ = """
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ask</code>
      <i>buat pertanyaan</i>
      <b>ᴄᴏɴᴛᴏʜ:</b> <code>{0}ask</code> <i>dimana letak Antartika</i>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}photo</code>
      <i>buat foto dengan ai</i>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stt</code>
      <i>merubah audio filter</i>
      </blockquote>
"""


@PY.UBOT("ask")
async def chat_gpt(client, message):
    prs = await EMO.PROSES(client)
    xbot = await EMO.UBOT(client)
    ggl = await EMO.GAGAL(client)
   
    try:
        # Show typing action to let the user know the bot is processing
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Check if the command includes a question
        if len(message.command) < 2:
            await message.reply_text(
                f"<blockquote>{ggl}<b>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ :</b> <code>ask bagaimana membuat donat?</code></blockquote>"
            )
            return

        # Processing message
        prs_msg = await message.reply_text(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ....</b>")
        
        # Extract the user's question
        question = message.text.split(' ', 1)[1]
        
        # OpenAI API request setup
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": question}]
        }

        try:
            # Send a request to the OpenAI API
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
            response.raise_for_status()  # Raises an HTTPError if the response code is 4xx or 5xx

            # Parse the response JSON
            json_response = response.json()
            if "choices" in json_response and json_response["choices"]:
                answer = json_response["choices"][0]["message"]["content"]
                await prs_msg.edit(
                    f"<blockquote>{answer}</blockquote>\n\n<blockquote>{xbot} **ᴅɪᴊᴀᴡᴀʙ ᴏʟᴇʜ** {client.me.mention}</blockquote>"
                )
            else:
                await prs_msg.edit("Error: Could not retrieve an answer from the API.")

        except requests.exceptions.RequestException as req_error:
            await prs_msg.edit(f"Request error: {req_error}")
        except ValueError:
            await prs_msg.edit("Error: Received an invalid JSON response from the API.")
            
    except Exception as e:
        await message.reply_text(f"An unexpected error occurred: {e}")


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
