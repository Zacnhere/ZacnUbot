import random
from pyrogram.enums import MessagesFilter
from PyroUbot import *

__MODULE__ = "asupan"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ  ᴀsᴜᴘᴀɴ 』</b> </blockquote>
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}asupan</code>
      <i>mengirim video asupan random</i> 

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cewek</code>
      <i>mengirim photo cewe random</i>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cowok</code>
      <i>mengirim photo cowo random</i>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}bokep</code>
      <i>mengirim video bokep random</i>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}bokep2</code>
      <i>mengirim video bokep2 random</i>
      </blockquote>

"""


@PY.UBOT("asupan")
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<b>{prs}ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ...</b>")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("cewek")
async def photo_cewek(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<b>{prs}ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("cowok")
async def photo_cowok(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<b>{prs}ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@Ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)

@PY.UBOT("bokep")
async def video_bokep(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<b>{prs}ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ...</b>")
    try:
        await client.join_chat("https://t.me/+kJJqN5kUQbs1NTVl")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1001867672427)

@PY.UBOT("bokep2")
async def video_bokep2(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<b>{prs}ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ2...</b>")
    try:
        await client.join_chat("https://t.me/+wqQ9MzJriwVjYTM9")
    except:
        pass
    try:
        bokep2nya = []
        async for bokep2 in client.search_messages(
            -1002143221100, filter=MessagesFilter.VIDEO
        ):
            bokep2nya.append(bokep2)
        video = random.choice(bokep2nya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1002143221100)
