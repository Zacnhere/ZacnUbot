import asyncio
import os
import requests

from asyncio import sleep
from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from bs4 import BeautifulSoup
from io import BytesIO

from telegraph import Telegraph, exceptions, upload_file

from PyroUbot import *

__MODULE__ = "misc"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴍɪꜱᴄ 』</b> </blockquote>
 <blockquote>
 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}carbon</code>
    <i>membuat text carbonara</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}qrGen</code>
    <i>merubah qrcode text menjadi gambar</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}qrRead</code>
    <i>merubah qrcode media menjadi text:</i>

 <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}tg</code>
    <i>mengapload media/text ke telegra.ph</i>
    </blockquote>  
"""

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@PY.UBOT("carbon")
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    carbon = await make_carbon(text)
    await ex.edit("<b><emoji id=6161365963204726449>⏳</emoji>ᴜᴘʟᴏᴀᴅɪɴɢ...</b>")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"<b><emoji id=4976558436708778794>✅</emoji>ᴄᴀʀʙᴏɴɪꜱᴇᴅ by :</b>{client.me.mention}",
        ),
    )
    carbon.close()


def qr_gen(content):
    return {
        "data": content,
        "config": {
            "body": "circle-zebra",
            "eye": "frame13",
            "eyeBall": "ball14",
            "erf1": [],
            "erf2": [],
            "erf3": [],
            "brf1": [],
            "brf2": [],
            "brf3": [],
            "bodyColor": "#000000",
            "bgColor": "#FFFFFF",
            "eye1Color": "#000000",
            "eye2Color": "#000000",
            "eye3Color": "#000000",
            "eyeBall1Color": "#000000",
            "eyeBall2Color": "#000000",
            "eyeBall3Color": "#000000",
            "gradientColor1": "",
            "gradientColor2": "",
            "gradientType": "linear",
            "gradientOnEyes": "true",
            "logo": "",
            "logoMode": "default",
        },
        "size": 1000,
        "download": "imageUrl",
        "file": "png",
    }


@PY.UBOT("qrgen")
async def _(client, message):
    ID = message.reply_to_message or message
    if message.reply_to_message:
        data = qr_gen(message.reply_to_message.text)
    else:
        if len(message.command) < 2:
            return await message.delete()
        else:
            data = qr_gen(message.text.split(None, 1)[1])
    Tm = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ʙᴜᴀᴛ ǫʀᴄᴏᴅᴇ....</b>")
    try:
        QRcode = (
            requests.post(
                "https://api.qrcode-monkey.com//qr/custom",
                json=data,
            )
            .json()["imageUrl"]
            .replace("//api", "https://api")
        )
        await client.send_photo(message.chat.id, QRcode, reply_to_message_id=ID.id)
        await Tm.delete()
    except Exception as error:
        await Tm.edit(error)



@PY.UBOT("qrread")
async def _(client, message):
    replied = message.reply_to_message
    if not (replied and replied.media and (replied.photo or replied.sticker)):
        await message.reply("<b><emoji id=5021905410089550576>✅</emoji>ʙᴀʟᴀs ᴋᴏᴅᴇ ǫʀ ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ...</b>")
        return
    if not os.path.isdir("premiumQR/"):
        os.makedirs("premiumQR/")
    AM = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇɴɢᴜɴᴅᴜʜ ᴍᴇᴅɪᴀ...</b>")
    down_load = await client.download_media(message=replied, file_name="premiumQR/")
    await AM.edit("<b><emoji id=6161365963204726449>⏳</emoji>ᴍᴇᴍᴘʀᴏsᴇs ᴋᴏᴅᴇ ǫʀ ᴀɴᴅᴀ...</b>")
    cmd = [
        "curl",
        "-X",
        "POST",
        "-F",
        "f=@" + down_load + "",
        "https://zxing.org/w/decode",
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    out_response = stdout.decode().strip()
    err_response = stderr.decode().strip()
    os.remove(down_load)
    if not (out_response or err_response):
        await AM.edit("<b><emoji id=6161479118413106534>❌</emoji>ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀᴛᴀ ᴋᴏᴅᴇ ǫʀ ɪɴɪ...</b>")
        return
    try:
        soup = BeautifulSoup(out_response, "html.parser")
        qr_contents = soup.find_all("pre")[0].text
    except IndexError:
        await AM.edit("<b><emoji id=6161479118413106534>❌</emoji>ɪɴᴅᴇᴋs ᴅᴀꜰᴛᴀʀ ᴅɪ ʟᴜᴀʀ ᴊᴀɴɢᴋᴀᴜᴀɴ</b>")
        return
    await AM.edit(f"<b><emoji id=4976558436708778794>✅</emoji>ᴅᴀᴛᴀ ǫʀᴄᴏᴅᴇ:</b>\n<code>{qr_contents}</code>")


@PY.UBOT("tg")
async def _(client, message):
    XD = await message.reply("<b><emoji id=6161365963204726449>⏳</emoji>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs . . .</b>")
    if not message.reply_to_message:
        return await XD.edit(
            "<b><emoji id=6161479118413106534>❌</emoji>ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ, ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʟɪɴᴋ ᴅᴀʀɪ ᴛᴇʟᴇɢʀᴀᴘʜ.</b>"
        )
    telegraph = Telegraph()
    if message.reply_to_message.media:
        m_d = await dl_pic(client, message.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        U_done = f"<emoji id=4976558436708778794>✅</emoji><b>ʙᴇʀʜᴀsɪʟ ᴅɪᴜᴘʟᴏᴀᴅ ᴋᴇ</b> <a href='https://telegra.ph/{media_url[0]}'>ᴛᴇʟᴇɢʀᴀᴘʜ</a>"
        await XD.edit(U_done)
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        wow_graph = f"<emoji id=4976558436708778794>✅</emoji><b>ʙᴇʀʜᴀsɪʟ ᴅɪᴜᴘʟᴏᴀᴅ ᴋᴇ</b> <a href='https://telegra.ph/{response['path']}'>ᴛᴇʟᴇɢʀᴀᴘʜ</a>"
        await XD.edit(wow_graph)

  
@PY.UBOT("font")
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    
    if message.reply_to_message:
        if message.reply_to_message.text:
            query = id(message)
        else:
            return await message.reply("<b>{ggl}ʜᴀʀᴀᴘ ʀᴇᴘʟʏ ᴋᴇ ᴛᴇxᴛ</b>")
    else:
        if len(message.command) < 2:
            return await message.reply(f"{ggl}<b><code>{message.text}</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]</b>")
        else:
            query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"get_font {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(error)


@PY.INLINE("^get_font")
async def _(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for X in query_fonts[0]:
        keyboard.append(
            InlineKeyboardButton(X, callback_data=f"get {get_id} {query_fonts[0][X]}")
        )
    buttons.add(*keyboard)
    buttons.row(InlineKeyboardButton("►", callback_data=f"next {get_id}"))
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get font!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        "<blockquote><b>👇ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ғᴏɴᴛ👇</b></blockquote>"
                    ),
                )
            )
        ],
    )


@PY.CALLBACK("^get")
async def _(client, callback_query):
    try:
        q = int(callback_query.data.split()[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        new = str(callback_query.data.split()[2])
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = m.text.split(None, 1)[1]
        get_new_font = gens_font(new, text)
        return await callback_query.edit_message_text(get_new_font)
    except Exception as error:
        return await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("^next")
async def _(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[1]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[1][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("◄", callback_data=f"prev {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("^prev")
async def _(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[0]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[0][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("►", callback_data=f"next {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"❌ Error: {error}", True)
