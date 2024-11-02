__MODULE__ = "absen"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʙꜱᴇɴ 』</b> </blockquote>
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}absen</code></code>
         <i>untuk membuat list absen.</i>
  
  
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delabsen</code></code>
         <i>untuk menghapus list absen.</i>
         </blockquote>
  """



from PyroUbot import *

@PY.UBOT("absen")
async def _(client, message):
    await absen_command(client, message)
    
    
@PY.UBOT("delabsen")
async def _(client, message):
    await clear_absen_command(client, message)


@PY.INLINE("^absen_in")
async def _(client, inline_query):
    await absen_query(client, inline_query)

@PY.CALLBACK("absen_hadir")
async def _(client, callback_query):
        await hadir_callback(client, callback_query)


from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,                            InputTextMessageContent, InlineKeyboardButton)
from datetime import datetime
import pytz

from PyroUbot import *

hadir_list = []

def get_hadir_list():
    return "\n".join([f"👤 {user['mention']} - {user['jam']}" for user in hadir_list])
    
async def absen_command(c, m):
    ggl = await EMO.GAGAL(c)
    sks = await EMO.BERHASIL(c)
    prs = await EMO.PROSES(c)
    user_id = m.from_user.id
    mention = m.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")

    hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list()
    try:
        x = await c.get_inline_bot_results(bot.me.username, "absen_in")
        if x.results:
            await m.reply_inline_bot_result(x.query_id, x.results[0].id)
        else:
            await m.reply(f"{ggl}<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ʜᴀsɪʟ ɪɴʟɪɴᴇ ʙᴏᴛ</b>")
    except asyncio.TimeoutError:
        await m.reply(f"{ggl}<code>ᴡᴀᴋᴛᴜ ʜᴀʙɪs ᴅᴀʟᴀᴍ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʜᴀsɪʟ ɪɴʟɪɴᴇ ʙᴏᴛ</code>")
    except Exception as e:
        await m.reply(f"{ggl}<b>ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ</b>: <code>{e}</b>")
        
        
async def clear_absen_command(c, m):
    hadir_list.clear()
    ggl = await EMO.GAGAL(c)
    sks = await EMO.BERHASIL(c)
    prs = await EMO.PROSES(c)
    await m.reply(f"{sks}<b>sᴇᴍᴜᴀ ᴀʙsᴇɴ ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs</b>")
        
        
async def absen_query(c, iq):
    user_id = iq.from_user.id
    mention = iq.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list()

    text = f"**ᴀʙsᴇɴ ᴛᴀɴɢɢᴀʟ:**\n{timestamp}\n\n**ʟɪsᴛ ᴀʙsᴇɴ:**\n{hadir_text}\n\n"
    buttons = [[InlineKeyboardButton("ʜᴀᴅɪʀ", callback_data="absen_hadir")]]
    keyboard = InlineKeyboardMarkup(buttons)
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="💬",
                    input_message_content=InputTextMessageContent(text),
                    reply_markup=keyboard
                )
            )
        ],
    )
    
async def hadir_callback(c, cq):
    user_id = cq.from_user.id
    mention = cq.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    if any(user['user_id'] == user_id for user in hadir_list):
        await cq.answer("ᴀɴᴅᴀ sᴜᴅᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴀʙsᴇɴ sᴇʙᴇʟᴜᴍɴʏᴀ", show_alert=True)
    else:
        hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
        hadir_text = get_hadir_list()
        text = f"<b>ᴀʙsᴇɴ ᴛᴀɴɢɢᴀʟ:</b>\n{timestamp}\n\n<b>ʟɪsᴛ ᴀʙsᴇɴ:</b>\n{hadir_text}\n\n"
        buttons = [[InlineKeyboardButton("ʜᴀᴅɪʀ", callback_data="absen_hadir")]]
        keyboard = InlineKeyboardMarkup(buttons)
        await cq.edit_message_text(text, reply_markup=keyboard)
