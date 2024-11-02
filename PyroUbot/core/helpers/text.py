from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, get_expired_date, get_two_factor, ubot


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>🔴 ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>ɪᴅ:</b> <code>{X.me.id}</code>
<b>ʀᴇᴀsᴏɴ:</b> <code>ᴜꜱᴇʀʙᴏᴛ ᴛᴇʟᴀʜ ʜᴀʙɪs</code></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

💬 @{bot.me.username} ᴀᴅᴀʟᴀʜ ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ʙɪsᴀ ᴋᴀʟɪᴀɴ ʙᴜᴀᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ

👉🏻 sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ / ᴍᴇᴍʙᴇʟɪ ᴜsᴇʀʙᴏᴛ</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴏʀᴅᴇʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b> 

<b>✅ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ</b></blockquote>
"""

    async def UBOT(count):
        code = await get_two_factor(ubot._ubot[int(count)].me.id)
        return f"""
<b>🤖 ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>👤 ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b>📍 ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b>📱 ɴᴏᴍᴇʀ ᴛᴇʟᴇᴘᴏɴ:</b> <code>{ubot._ubot[int(count)].me.phone_number}</code>
<b>🔐 ᴛᴡᴏ-ғᴀᴄᴛᴏʀ</b> <code>{code}</code>
"""

    def POLICY():
        return """
<blockquote><b>↪️ ᴋᴇʙɪᴊᴀᴋᴀɴ ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ

✅ sᴇᴛᴇʟᴀʜ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ, ᴊɪᴋᴀ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍᴘᴇʀᴏʟᴇʜ/
ᴍᴇɴᴇʀɪᴍᴀ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ ᴘᴇᴍʙᴇʟɪᴀɴ, 
ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʜᴀᴋ ᴘᴇɴɢɢᴀɴᴛɪᴀɴ ᴅᴀʟᴀᴍ ᴡᴀᴋᴛᴜ 2 ʜᴀʀɪ sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴇʟɪᴀɴ. ɴᴀᴍᴜɴ, ᴊɪᴋᴀ 
ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ/ᴍᴇɴᴇʀɪᴍᴀ sᴀʟᴀʜ sᴀᴛᴜ ᴍᴀɴꜰᴀᴀᴛ ᴅᴀʀɪ 
ᴘᴇᴍʙᴇʟɪᴀɴ, ᴛᴇʀᴍᴀsᴜᴋ ᴀᴋsᴇs ᴋᴇ ꜰɪᴛᴜʀ ᴘᴇᴍʙᴜᴀᴛᴀɴ ᴜsᴇʀʙᴏᴛ, ᴍᴀᴋᴀ 
ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʟᴀɢɪ ʙᴇʀʜᴀᴋ ᴀᴛᴀs ᴘᴇɴɢᴇᴍʙᴀʟɪᴀɴ ᴅᴀɴᴀ.

🆘 ᴅᴜᴋᴜɴɢᴀɴ
ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴜᴋᴜɴɢᴀɴ, ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ:
• ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴅɪʙᴀᴡᴀʜ ɪɴɪ
• sᴜᴘᴘᴏʀᴛ @ZacnBoys ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ

👉🏻 ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴʏᴀᴛᴀᴋᴀɴ ʙᴀʜᴡᴀ ᴀɴᴅᴀ ᴛᴇʟᴀʜ 
ᴍᴇᴍʙᴀᴄᴀ ᴅᴀɴ ᴍᴇɴᴇʀɪᴍᴀ ᴋᴇᴛᴇɴᴛᴜᴀɴ ɪɴɪ ᴅᴀɴ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ 
ᴘᴇᴍʙᴇʟɪᴀɴ. ᴊɪᴋᴀ ᴛɪᴅᴀᴋ, ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴀᴛᴀʟᴋᴀɴ.</b></blockquote>
"""
