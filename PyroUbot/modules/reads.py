from pyrogram import *
from pyrogram.types import *
from pyrogram.raw.functions.messages import *
from pyrogram.errors import FloodWait

from PyroUbot import *


__MODULE__ = "reads"
__HELP__ = """
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}read</code>
   <i>membaca pesan dengan instant</i>

 <b>ᴛʏᴘᴇ:</b>
   ● <code>all</code>
   ● <code>group</code>
   ● <code>users</code>
   ● <code>channel</code>
   ● <code>reaction</code>
   ● <code>bot</code>
   ● <code>mention</code>
   </blockquote>
"""



async def read_count(client, message_type):
    total_unread = 0
  
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        chat_id = dialog.chat.id

        try:
            if message_type == "mention" and chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                peer = await client.resolve_peer(chat_id)
                total_unread += dialog.unread_mentions_count
                await client.invoke(ReadMentions(peer=peer))
            
            elif message_type == "reaction" and chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                peer = await client.resolve_peer(chat_id)
                total_unread += dialog.unread_reactions_count
                await client.invoke(ReadReactions(peer=peer))

            elif message_type == "users" and chat_type == enums.ChatType.PRIVATE:
                total_unread += dialog.unread_messages_count
                await client.read_chat_history(chat_id)

            elif message_type == "bot" and chat_type == enums.ChatType.BOT:
                total_unread += dialog.unread_messages_count
                await client.read_chat_history(chat_id)

            elif message_type == "channel" and chat_type == enums.ChatType.CHANNEL:
                total_unread += dialog.unread_messages_count
                await client.read_chat_history(chat_id)

            elif message_type == "group" and chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
                total_unread += dialog.unread_messages_count
                await client.read_chat_history(chat_id)
            
            elif message_type == "all" and chat_type in [enums.ChatType.PRIVATE, enums.ChatType.GROUP, enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL, enums.ChatType.BOT]:
                total_unread += dialog.unread_messages_count
                await client.read_chat_history(chat_id)

        except Exception as e:
            print(f"ᴘʀᴏsᴇs ɢᴀɢᴀʟ {chat_id}: {e}")

    return total_unread


@PY.UBOT("read")
async def _(client, message):
    command = message.command[1].lower() if len(message.command) > 1 else None
    
    Tm = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")

    valid_commands = ["mention", "reaction", "all", "group", "users", "channel", "bot"]
    if command not in valid_commands:
        return await Tm.edit("<b>ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ</b>")

    if command == "mention":
        total_read = await read_count(client, "mention")
    else:
        total_read = await read_count(client, command)

    return await Tm.edit(f"{total_read} <b>ᴘᴇsᴀɴ ᴛᴇʟᴀʜ ᴅɪʙᴀᴄᴀ\n ᴛʏᴘᴇ {command}</b>")

  
