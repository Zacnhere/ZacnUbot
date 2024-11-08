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
        # Show typing action
        
   
await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Check if the command includes a question
        if len(message.command) < 2:
            
          
await message.reply_text(
                
           

    
f"<blockquote>{ggl}<b>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ :</b> <code>ask bagaimana membuat donat?</code></blockquote>"
            )
            
            )
        
return

        # Processing message
        prs_msg = 
   
await message.reply_text(f"{prs}<b>ᴘʀᴏᴄᴇssɪɴɢ....</b>")
        
        
        
# Extract question from the message
        question = message.text.split(
        question = mess
' ', 1)[1]
        
        
   
# Make the API request
        try:
            response = requests.get(
            response = r
f'https://chatgpt.apinepdev.workers.dev/?question={question}')
            response.raise_for_status()  
     
# Raises an HTTPError for non-200 responses
            
            
   
# Parse the response JSON
            json_response = response.json()
            
            json_response = response.json()
if "answer" in json_response:
                answer = json_response[
               
"answer"]
                await prs_msg.edit(
                    
      
f"<blockquote>{answer}</blockquote>\n\n<blockquote>{xbot} **ᴅɪᴊᴀᴡᴀʙ ᴏʟᴇʜ** {client.me.mention}</blockquote>"
                )
            
                )
 
else:
                await prs_msg.edit("Error: No 'answer' key found in the API response.")

        except requests.exceptions.RequestException as req_error:
            await prs_msg.edit(f"Request error: {req_error}")
        
        exc
except ValueError:
            await prs_msg.edit("Error: Received an invalid JSON response from the API.")
            
    
        
except Exception as e:
        await message.reply_text(f"An unexpected error occurred: {e}")
