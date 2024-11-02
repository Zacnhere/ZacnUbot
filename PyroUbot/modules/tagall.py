import asyncio
import random
from random import shuffle


from PyroUbot import *



__MODULE__ = "tagall"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴛᴀɢᴀʟʟ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tagall</code>
   <i>melakukan tag ke seluruh anggota group</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}batal</code>
   <i>membatalkan perintah tagall</i>
   </blockquote>
  """



tagallgcid = []

emoji_categories = {
    "smileys": [
        "😀",
        "😃",
        "😄",
        "😁",
        "😆",
        "😅",
        "😂",
        "🤣",
        "😊",
        "😍",
        "🥰",
        "😘",
        "😎",
        "🥳",
        "😇",
        "🙃",
        "😋",
        "😛",
        "🤪",
    ],
    "animals": [
        "🐶",
        "🐱",
        "🐰",
        "🐻",
        "🐼",
        "🦁",
        "🐸",
        "🦊",
        "🦔",
        "🦄",
        "🐢",
        "🐠",
        "🐦",
        "🦜",
        "🦢",
        "🦚",
        "🦓",
        "🐅",
        "🦔",
    ],
    "food": [
        "🍎",
        "🍕",
        "🍔",
        "🍟",
        "🍩",
        "🍦",
        "🍓",
        "🥪",
        "🍣",
        "🍔",
        "🍕",
        "🍝",
        "🍤",
        "🥗",
        "🥐",
        "🍪",
        "🍰",
        "🍫",
        "🥤",
    ],
    "nature": [
        "🌲",
        "🌺",
        "🌞",
        "🌈",
        "🌊",
        "🌍",
        "🍁",
        "🌻",
        "🌸",
        "🌴",
        "🌵",
        "🍃",
        "🍂",
        "🌼",
        "🌱",
        "🌾",
        "🍄",
        "🌿",
        "🌳",
    ],
    "travel": [
        "✈️",
        "🚀",
        "🚲",
        "🚗",
        "⛵",
        "🏔️",
        "🚁",
        "🚂",
        "🏍️",
        "🚢",
        "🚆",
        "🛴",
        "🛸",
        "🛶",
        "🚟",
        "🚈",
        "🛵",
        "🛎️",
        "🚔",
    ],
    "sports": [
        "⚽",
        "🏀",
        "🎾",
        "🏈",
        "🎱",
        "🏓",
        "🥊",
        "⛳",
        "🏋️",
        "🏄",
        "🤸",
        "🏹",
        "🥋",
        "🛹",
        "🥏",
        "🎯",
        "🥇",
        "🏆",
        "🥅",
    ],
    "music": ["🎵", "🎶", "🎤", "🎧", "🎼", "🎸", "🥁", "🎷", "🎺", "🎻", "🪕", "🎹", "🔊"],
    "celebration": ["🎉", "🎊", "🥳", "🎈", "🎁", "🍰", "🧁", "🥂", "🍾", "🎆", "🎇"],
    "work": ["💼", "👔", "👓", "📚", "✏️", "📆", "🖥️", "🖊️", "📂", "📌", "📎"],
    "emotions": ["❤️", "💔", "😢", "😭", "😠", "😡", "😊", "😃", "🙄", "😳", "😇", "😍"],
}


def emoji_random():
    random_category = random.choice(tuple(emoji_categories.keys()))
    return random.choice(emoji_categories[random_category])


@PY.UBOT("tagall")
@PY.GROUP
async def _(client, message):
    if message.chat.id in tagallgcid:
        return
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
        f"<a href=tg://user?id={member.user.id}>{emoji_random()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await m.reply_text(
            f"<blockquote><b>{text}</b>\n\n{' '.join(output)}</blockquote>", quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(2)
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass


@PY.UBOT("batal")
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if message.chat.id not in tagallgcid:
        return await message.reply_text(
            f"<blockquote>{ggl}<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇʀɪɴᴛᴀʜ: <code>tagall</code> ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ</b></blockquote>"
        )
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text(f"<blockquote>{brhsl}<b>ᴛᴀɢᴀʟʟ ʙᴇʀʜᴀsɪʟ ᴅɪʙᴀᴛᴀʟᴋᴀɴ</b></blockquote>")
