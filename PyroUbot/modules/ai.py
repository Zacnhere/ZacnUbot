from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

API_KEY = "http://chat.openai.com"

__MODULE__ = "Ai"
__HELP__ = """
<blockquote>
<b>『 ᴄʜᴀᴛ ɢᴘᴛ 』</b> </blockquote>
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ask</code>
      <i>buat pertanyaan</i>
      <b>ᴄᴏɴᴛᴏʜ:</b> <code>{0}ask</code> <i>dimana letak Antartika</i>
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
