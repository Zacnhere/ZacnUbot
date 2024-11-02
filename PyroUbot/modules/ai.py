from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

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
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                f"<blockquote>{ggl}<b>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ :</b> <code>ask bagaimana membuat donat?</code></blockquote>"
            )
        else:
            prs = await message.reply_text(f"{prs}<b>ᴘʀᴏᴄᴄᴇsɪɴɢ....</b>")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                if "answer" in response.json():
                    x = response.json()["answer"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>\n\n<blockquote>{xbot} **ᴅɪᴊᴀᴡᴀʙ ᴏʟᴇʜ** {bot.me.mention}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
      
