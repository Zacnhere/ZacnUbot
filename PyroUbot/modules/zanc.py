from PyroUbot import *
from pyrogram.errors.exceptions import FloodWait

@PY.MECHA()
async def _(client, message):
    try:
        await message.delete()
    except FloodWait as Haku:
        await asyncio.sleep(Haku.value)
        await message.delete()
    except:
        pass