"""
create:          Anonymousx888.t.me
"""

from PyroUbot import *

__MODULE__ = "filtergrup"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ғɪʟᴛᴇʀ ɢʀᴏᴜᴘs 』</b> </blockquote>
  <blockquote>
  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}filter</code> <b>ᴏɴ/ᴏғғ</b>
      <i>untuk mengaktifkan atau mengaktifkan filters</i>
    <b>ᴄᴀᴛᴀᴛᴀɴ:</b> <i>khusus grup</i>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addfilter</code> <b>ɴᴀᴍᴀ - ʀᴇᴘʟʏ_ᴍsɢ</b>
      <i>untuk menambahkan filters ke database</i>
    <b>ᴄᴀᴛᴀᴛᴀɴ:</b> <i>khusus grup</i>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delfilter</code> <b>ɴᴀᴍᴀ ғɪʟᴛᴇʀs</b>
      <i>untuk menghapus filters dari database</i>
    <b>ᴄᴀᴛᴀᴛᴀɴ:</b> <i>khusus grup</i>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listfilter</code>
      <i>untuk melihat semua daftar filters</i>
    <b>ᴄᴀᴛᴀᴛᴀɴ:</b> <i>khusus grup</i>
    </blockquote>
"""


@PY.NO_CMD_UBOT("FILTER_MSG", ubot)
async def _(client, message):
    try:
        chat_logs = bot.me.id
        all_filters = await all_vars(client.me.id, "FILTERS") or {}
        
        for key, value in all_filters.items():
            if key == message.text.split()[0]:
                msg = await client.get_messages(int(chat_logs), int(value))
                return await msg.copy(message.chat.id, reply_to_message_id=message.id)
    except BaseException:
        pass


@PY.UBOT("filter")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"<b>{ggl}ɢᴜɴᴀᴋᴀɴ ᴏɴ/ᴏғғ</b>")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "FILTER_ON_OFF", type)
    return await txt.edit(f"<b>{sks}ғɪʟᴛᴇʀs ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b>")


@PY.UBOT("addfilter")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    type, reply = extract_type_and_msg(message)

    if not type and message.reply_to_message:
        return await txt.edit(f"{ggl}<b>ʜᴀʀᴀᴘ ʙᴀʟᴀs ᴘᴇsᴀɴ ᴅᴀɴ ᴋᴀsɪʜ ɴᴀᴍᴀ</b>")

    logs = bot.me.id
    if bool(logs):
        try:
            msg = await reply.copy(int(logs))
            await set_vars(client.me.id, type, msg.id, "FILTERS")
            await txt.edit(f"{sks}<b>ғɪʟᴛᴇʀs</b> <code>{type}</code> <b>ʙᴇʀʜᴀsɪʟ ᴅɪ sɪᴍᴘᴀɴ</b>")
        except Exception as error:
            await txt.edit(error)
    else:
        return await txt.edit(f"{ggl}<b>ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ғɪʟᴛᴇʀs ʙᴀʀᴜ</b>")


@PY.UBOT("delfilter")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ..</b>")
    arg = get_arg(message)

    if not arg:
        return await txt.edit(f"{ggl}<code>{message.text.split()[0]}</code> <b>ɴᴀᴍᴀ ғɪʟᴛᴇʀ</b>")

    logs = bot.me.id
    all = await all_vars(client.me.id, "FILTERS")

    if arg not in all:
        return await txt.edit(f"{ggl}<b>ғɪʟᴛᴇʀ</b> <code>{arg}</code> <b>ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ!</b>")

    await remove_vars(client.me.id, arg, "FILTERS")
    await client.delete_messages(logs, all[arg])
    return await txt.edit(f"<b>ғɪʟᴛᴇʀ</b> <code>{arg}</code> <b>ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs{sks}</b>")


@PY.UBOT("listfilter")
@PY.ULTRA
@PY.GROUP
async def _(client, message):
    vars = await all_vars(client.me.id, "FILTERS")
    if vars:
        msg = "<b>📝 ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs</b>\n"
        for x in vars.keys():
            msg += f"<b> ├ <code>{x}</code></b>\n"
        msg += f"<b> ╰ ᴛᴏᴛᴀʟ ғɪʟᴛᴇʀs: {len(vars)}</b>"
    else:
        msg = "<b>❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ғɪʟᴛᴇʀs ʏᴀɴɢ ᴛᴇʀsɪᴍᴘᴀɴ</b>"

    return await message.reply(msg, quote=True)
