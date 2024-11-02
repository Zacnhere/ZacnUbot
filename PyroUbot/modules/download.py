import asyncio

from pyrogram.raw.functions.messages import DeleteHistory

from PyroUbot import *


__MODULE__ = "downloader"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}down</code>
   <i>mendownload video tiktok</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}song</code>
   <i>mendownload music yang di inginkan</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}vsong</code>
   <i>mendownload video yang di inginkan</i>
   </blockquote>

"""


@PY.UBOT("down")
async def sosmed_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<code>{message.text}</code> ʟɪɴᴋ ᴛɪᴋᴛᴏᴋ"
        )
    else:
        bot = "TIKTOKDOWNLOADROBOT"
        link = message.text.split()[1]
        await client.unblock_user(bot)
        Tm = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ . . .</b>")
        xnxx = await client.send_message(bot, link)
        await asyncio.sleep(10)
        try:
            sosmed = await client.get_messages(bot, xnxx.id + 2)
            await sosmed.copy(message.chat.id, reply_to_message_id=message.id)
            await Tm.delete()
        except Exception:
            await Tm.edit(
                "<b>ᴠɪᴅᴇᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ sɪʟᴀʜᴋᴀɴ ᴜʟᴀɴɢɪ ʙᴇʙᴇʀᴀᴘᴀ sᴀᴀᴛ ʟᴀɢɪ</b>"
            )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))

