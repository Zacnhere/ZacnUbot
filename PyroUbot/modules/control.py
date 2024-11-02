from PyroUbot import *

__MODULE__ = "control"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ sᴇᴛᴘʀᴇғɪx 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setprefix</code>
   <i>untuk merubah prefix/handler perintah</i>
   </blockquote>       
"""


@PY.UBOT("creat")
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"<b><code>{message.text}</code> [ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ] [ɴᴀᴍᴇ/ᴛɪᴛʟᴇ]</b>")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("<b>ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜᴘ: [{group_name}]({link.invite_link})</b>",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: [{group_name}]({link.invite_link})</b>",
            disable_web_page_preview=True,
        )


@PY.UBOT("setprefix")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    Tm = await message.reply(f"<b>{brhsl}ᴍᴇᴍᴘʀᴏsᴇs...</b>", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"{ggl}<code>{message.text}</code> <b>[sɪᴍʙᴏʟ]</b>")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"<code>{prefix}</code>" for prefix in ub_prefix)
            return await Tm.edit(f"<blockquote><b>{brhsl}ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b></blockquote>")
        except Exception as error:
            return await Tm.edit(str(error))


@PY.UBOT("afk")
async def _(client, message):
    tion = await EMO.MENTION(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    msg_afk = (
        f"<blockquote><b>{tion}sᴇᴅᴀɴɢ ᴀғᴋ\n{ktrng}ᴀʟᴀsᴀɴ: {reason}</b></blockquote>"
        if reason
        else "<blockquote><b>sᴇᴅᴀɴɢ ᴀғᴋ</b></blockquote>"
      )
    await set_vars(client.me.id, "AFK", db_afk)
    return await message.reply(msg_afk)



@PY.NO_CMD_UBOT("AFK", ubot)
async def _(client, message):
    tion = await EMO.MENTION(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    mng = await EMO.MENUNGGU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = (
            f"<blockquote><b>{tion}sᴇᴅᴀɴɢ ᴀғᴋ\n{mng}ᴡᴀᴋᴛᴜ: {afk_runtime}\n{ktrng}ᴀʟᴀsᴀɴ: {afk_reason}</b></blockquote>"
            if afk_reason
            else f"<blockquote><b>sᴇᴅᴀɴɢ ᴀғᴋ\nᴡᴀᴋᴛᴜ: {afk_runtime}</b></blockquote>"
        )
        return await message.reply(afk_text)


@PY.UBOT("unafk")
async def _(client, message):
    tion = await EMO.MENTION(client)
    mng = await EMO.MENUNGGU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = f"<blockquote><b>{tion}ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n{mng}ᴀғᴋ sᴇʟᴀᴍᴀ: {afk_runtime}</b></blockquote>"
        await message.reply(afk_text)
        return await remove_vars(client.me.id, "AFK")


@PY.UBOT("setemoji")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    try:
        msg = await message.reply(f"<b>{prs}ᴍᴇᴍᴘʀᴏsᴇs...</b>", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                "<b>ᴜɴᴛᴜᴋ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀᴋᴜɴ ᴀɴᴅᴀ ʜᴀʀᴜs ᴘʀᴇᴍɪᴜᴍ ᴛᴇʀʟᴇʙɪʜ</b>"
            )

        if len(message.command) < 3:
            return await msg.edit(f"<b>{ggl}ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")

        query_mapping = {
          "pong": "EMOJI_PING",
          "mention": "EMOJI_MENTION",
          "ubot": "EMOJI_USERBOT",
          "proses": "EMOJI_PROSES",
          "gcast": "EMOJI_BROADCAST",
          "berhasil": "EMOJI_BERHASIL",
          "gagal": "EMOJI_GAGAL",
          "keterangan": "EMOJI_KETERANGAN",
          "group": "EMOJI_GROUP",
          "menunggu": "EMOJI_MENUNGGU",
        }
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"<blockquote><b>{brhsl}ᴇᴍᴏJɪ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ ᴋᴇ:</b> <emoji id={emoji_id}>{value}</emoji></blockquote>"
                )
            else:
                await msg.edit(f"<b>{ggl}ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ</b>")
        else:
            await msg.edit(f"<b>{ggl}ᴍᴀᴘᴘɪɴɢ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    except Exception as error:
        await msg.edit(str(error))

