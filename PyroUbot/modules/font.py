import asyncio
import os
import requests

from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from bs4 import BeautifulSoup
from io import BytesIO

from telegraph import Telegraph, exceptions, upload_file

from PyroUbot import *



__MODULE__ = "font"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ғᴏɴᴛ 』</b> </blockquote>
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}font</code>
     <i>merubah text menjadi berbeda</i>
     </blockquote>

   """
