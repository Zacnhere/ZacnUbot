from PyroUbot import *
from pyrogram.enums import ParseMode
__MODULE__ = "customtext"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ  ᴄᴏsᴛᴜᴍ ᴛᴇxᴛ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}set</code>
      <i>untuk merubah text pada tampilan 
         ping/mention/ubot</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}set devs</code> <b>[ᴋᴀᴛᴀ/ɴᴏɴᴇ]</b>
      <i>untuk merubah text pada tampilan
         devs ubot</i>
      
 <b>ᴄᴏɴᴛᴏʜ:</b>
     → <code>{0}set pong</code> <b>[ᴋᴀᴛᴀ/ɴᴏɴᴇ]</b>
     → <code>{0}set mention</code> <b>[ᴋᴀᴛᴀ/ɴᴏɴᴇ]</b>
     → <code>{0}set ubot</code> <b>[ᴋᴀᴛᴀ/ɴᴏᴍᴇ]</b>

 <b>ǫᴜᴇʀʏ:</b>
     ● <code>pong</code> 
     ● <code>mention</code> 
     ● <code>ubot</code> 

 <b>ᴄᴀᴛᴀᴛᴀɴ:</b>
   • <code>{0}set</code> <b>[query]</b> <code>none</code>
      <i>untuk merubah tampilan semula</i>
      </blockquote>      
"""

@PY.UBOT("set")
@PY.ULTRA
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        msg = await message.reply(f"{prs}<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>", quote=True)

        if len(message.command) < 3:
            return await msg.edit(f"{ggl}<b>ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴜᴇɴʏᴀ</b>")

        query_mapping = {
            "pong": "STRING_PONG",
            "mention": "STRING_OWNER",
            "ubot": "STRING_UBOT",
            "devs": "STRING_DEVS",
        }

        command = message.command[0]
        mapping = message.command[1]
        value = " ".join(message.command[2:])

        if mapping.lower() in query_mapping:
            if value.lower() == "none":
                value = False
            query_var = query_mapping[mapping.lower()]
            await set_vars(client.me.id, query_var, value)
            await msg.edit(
                f"{brhsl}<b>ᴛᴇxᴛ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ ᴋᴇ</b> : {value}"
            )
        else:
            await msg.edit(f"{ggl}<b>ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    except Exception as error:
        await msg.edit(str(error))
