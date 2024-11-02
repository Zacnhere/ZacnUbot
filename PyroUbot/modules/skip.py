from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from PyroUbot import *
from pytgcalls.exceptions import NotInCallError

async def lanjut_current_song(client, chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            try:
                await client.call_py.leave_call(chat_id)
            except NotInCallError:
                pass
            clear_queue(chat_id)
            return 1
        else:
            try:
                songname = chat_queue[1][0]
                url = chat_queue[1][1]
                link = chat_queue[1][2]
                type = chat_queue[1][3]
                Q = chat_queue[1][4]
                if type == "Audio":
                    await client.call_py.play(
                        chat_id,
                        MediaStream(
                            url,
                            AudioQuality.STUDIO,
                        ),
                    )
                elif type == "Video":
                    await client.call_py.play(
                        chat_id,
                        MediaStream(
                            url,
                        ),
                    )
                pop_an_item(chat_id)
                return [songname, link, type]
            except:
                await client.call_py.leave_call(chat_id)
                clear_queue(chat_id)
                return 2
    else:
        return 0

@PY.HAKU("skip")
@PY.GROUP
async def skip(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await lanjut_current_song(client, chat_id)
        if op == 0:
            await m.reply(f"<blockquote>{ggl}<b>ɴᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ</b></blockquote>")
        elif op == 1:
            await m.reply(f"<blockquote>{ggl}<b>ǫᴜᴇᴜᴇ ɪs ᴇᴍᴘᴛʏ, ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...</b></blockquote>")
        elif op == 2:
            await m.reply(f"<blockquote>{ggl}<b>sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ</b> \n<b>ᴄʟᴇᴀʀɪɴɢ ᴛʜᴇ ǫᴜᴇᴜᴇs ᴀɴᴅ ʟᴇᴀᴠɪɴɢ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...</b></blockquote>")
        else:
            await m.reply(f"<blockquote>**<emoji id=6005994005148471369>⏩</emoji> sᴋɪᴘᴘᴇᴅ** \n**<emoji id=5895705279416241926>▶</emoji> ɴᴏᴡ ᴘʟᴀʏɪɴɢ** - [{op[0]}]({op[1]}) | `{op[2]}`</blockquote>", disable_web_page_preview=True)

    else:
        skip = m.text.split(None, 1)[1]
        OP = "<blockquote>**ʀᴇᴍᴏᴠᴇᴅ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ sᴏɴɢs ғʀᴏᴍ ǫᴜᴇᴜᴇ:-**</blockquote>"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)        

@PY.HAKU("end")
@PY.GROUP
async def stop(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await client.call_py.leave_call(chat_id)
            clear_queue(chat_id)
            await m.reply(f"<blockquote>{brhsl}<b>sᴛʀᴇᴀᴍɪɴɢ ᴇɴᴅᴇᴅ!</b></blockquote>")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply(f"<blockquote>{ggl}<b>ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ</b></blockquote>")
   
@PY.HAKU("pause")
@PY.GROUP
async def pause(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await client.call_py.pause_stream(chat_id)
            await m.reply("<blockquote><b><emoji id=6005824650293022970>⏸️</emoji> ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍɪɴɢ</b></blockquote>")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply(f"<blockquote>{ggl}<b>ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ</b></blockquote>")
      
@PY.HAKU("resume")
@PY.GROUP
async def resume(client, m: Message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await client.call_py.resume_stream(chat_id)
            await m.reply("<blockquote>**<emoji id=5895705279416241926>▶️</emoji> ʀᴇsᴜᴍᴇᴅ sᴛʀᴇᴀᴍɪɴɢ**</blockquote>")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply(f"<blockquote>{ggl}<b>ɴᴏᴛʜɪɴɢ ɪs sᴛʀᴇᴀᴍɪɴɢ</b></blockquote>")
