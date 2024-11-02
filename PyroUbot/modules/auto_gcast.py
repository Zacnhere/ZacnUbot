import asyncio
import random

from gc import get_objects
from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from pyrogram.errors.exceptions import FloodWait

from PyroUbot import *

__MODULE__ = "autogcast"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴀᴜᴛᴏ ɢᴄᴀsᴛ』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}auto_gcast</code>
   <i>mengirim pesan siaran secara otomatis</i>
<b>ǫᴜᴇʀʏ:</b>
 ● <code>on</code>
 ● <code>off</code>
 ● <code>text</code>
 ● <code>list</code>
 ● <code>remove</code> <b>[ᴀʟʟ/ᴀɴɢᴋᴀ]</b>
 ● <code>delay</code> <b>[ᴀɴɢᴋᴀ]</b>
 ● <code>limit</code> <b>[ᴏɴ/ᴏғғ]</b>
 </blockquote>

"""
