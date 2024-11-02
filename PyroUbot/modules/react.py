__MODULE__ = "reaction"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ʀᴇᴀᴄᴛɪᴏɴ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}react</code> [ᴜꜱᴇʀɴᴀᴍᴇ] [ᴇᴍᴏᴛ]
   <i>memberikan reaction pengguna</i>
<b>ᴛʏᴘᴇ:</b> <b>ᴄʜᴀɴɴᴇʟ | ᴄʜᴀᴛ ᴜsᴇʀs</b>
   
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopreact</code>
   <i>membatalkan proses reaction</i>
   </blockquote>  
"""

from PyroUbot import *
from pyrogram import Client, idle, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatMember
from pyrogram.errors.exceptions import UserNotParticipant

reaction_progress = False

@PY.UBOT("react")
async def _(c, m):
    global reaction_progress
    reaction_progress = True
    try:
        if len(m.command) != 3:
            await m.reply("<b><emoji id=6161479118413106534>❌</emoji>ꜰᴏʀᴍᴀᴛ [ᴜsᴇʀɴᴀᴍᴇ-ᴇᴍᴏᴊɪ]</b>")
            return

        chat_id = m.command[1]
    except IndexError:
        await m.reply("<b><emoji id=6161479118413106534>❌</emoji>ꜰᴏʀᴍᴀᴛ [ᴜsᴇʀɴᴀᴍᴇ-ᴇᴍᴏᴊɪ]</b>")
        return

    rach = await m.reply("<b><emoji id=5974326532670230199>⏳</emoji>ᴘʀᴏᴄᴄᴇꜱɪɴɢ..</b>")
    async for message in c.get_chat_history(chat_id):
        await asyncio.sleep(0.5)
        chat_id = message.chat.id
        message_id = message.id
        try:
            if not reaction_progress:
                break
            await asyncio.sleep(0.5)
            await c.send_reaction(chat_id=chat_id, message_id=message_id, emoji=m.command[2])
        except Exception:
            pass
    
    await rach.edit(f"<b><emoji id=4976558436708778794>⭐</emoji>ʀᴇᴀᴄᴛɪᴏɴ ʙᴇʀʜᴀꜱɪʟ</b>")


@PY.UBOT("stopreact")
async def _(client, message):
    global reaction_progress
    reaction_progress = False
    await message.reply("<b><emoji id=5021905410089550576>✅</emoji>ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ʀᴇᴀᴄᴛɪᴏɴ</b>")
