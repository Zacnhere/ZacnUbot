import asyncio
import random

from pyrogram import *
from pyrogram import types
from asyncio import sleep

from PyroUbot import *

__MODULE__ = "antiuser"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀɴᴛɪᴜsᴇʀ 』</b> </blockquote>
<blockquote>
<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}antiuser</code> <b>ᴏɴ/ᴏғғ</b>
   <i>untuk menhidupkan dan mematikan</i>
   
<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}dor</code>
   <i>tambahkan pengguna dalam blacklist</i>
   
<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}undor</code>
   <i>hapus pengguna dalam blacklist</i>

<b>➢ ᴘᴇʀɪɴᴛᴀʜ : </b><code>{0}getuser</code>
   <i>melihat daftar blacklist</i>
   
<b>➢ ɴᴏᴛᴇs:</b> 
   <i>pengguna yang di tambahkan tidak bisa
     mengirim pesan di group yang anda admin</i>
     </blockquote>
"""

import asyncio
import random

from pyrogram import *
from pyrogram import types
from asyncio import sleep
from PyroUbot.config import OWNER_ID
from PyroUbot import *
from pyrogram.errors.exceptions import FloodWait

@PY.UBOT("antiuser")
@PY.ULTRA
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    txt = await message.reply(f"{prs}<b>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"<blockquote><b>{ggl}ɢᴜɴᴀᴋᴀɴ ᴏɴ/ᴏғғ</b></blockquote>")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "ON_OFF_ANTI_USER", type)
    return await txt.edit(f"<blockquote><b>{sks}ᴀɴᴛɪᴜsᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢs ᴋᴇ {type}</b></blockquote>")


@PY.UBOT("dor")
@PY.ULTRA
async def add_user_to_blacklist(c, m):
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)

    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"<blockquote>{ggl}<b>ғᴏʀᴍᴀᴛ [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ]</b></blockquote>", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])
    if user_id == OWNER_ID:
        return await m.reply(f"<blockquote>{ggl}<b>ɢᴜᴀ ʏᴀɴɢ ᴘᴜɴʏᴀ ʙᴏᴛ ᴛᴏᴅ!</b></blockquote>")
    user_ids = await get_user_ids(c.me.id)
    if user_id not in user_ids:
        user_ids.append(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"<blockquote>{brhsl}<b>ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴᴛɪᴜsᴇʀ!!</b></blockquote>", quote=True)
    else:
        await m.reply_text(f"<blockquote>{ggl}<b>sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ᴀɴᴛɪᴜsᴇʀ!!</b></blockquote>", quote=True)

@PY.UBOT("undor")
@PY.ULTRA
async def remove_user_from_blacklist(c, m):
    brhsl = await EMO.BERHASIL(c)
    ggl = await EMO.GAGAL(c)

    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"<blockquote>{ggl}<b>ғᴏʀᴍᴀᴛ [ʀᴇᴘʟʏ_ᴘᴇꜱᴀɴ]</b></blockquote>", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    user_ids = await get_user_ids(c.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"<blockquote><b>ᴜsᴇʀ</b> : `{user_id}` \n<b>{brhsl}ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</b></blockquote>", quote=True)
    else:
        await m.reply_text(f"<blockquote>{ggl}<b>ᴜsᴇʀ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ</b></blockquote>", quote=True)

@PY.UBOT("getuser")
@PY.ULTRA
@PY.TOP_CMD
async def display_blacklist(client, message):
    sks = await EMO.BERHASIL(client)
    try:
        daftar = await get_user_ids(client.me.id)
        pesan = "\n".join(f"<blockquote><b>{sks}ᴅᴀғᴛᴀʀ ᴀɴᴛɪᴜsᴇʀ</b>\n\n ⌦ <code>`{x}`</code></blockquote>" for x in daftar)
        await message.reply(pesan)
    except Exception as r:
        await message.reply(r)




from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Daftar ID pengguna yang diblacklist (misalnya, disimpan dalam list atau database)
blacklisted_users = set()  # Menggunakan set untuk menyimpan ID unik
bot_status = True  # Status untuk menyalakan/mematikan penghapusan pesan

# Fungsi untuk menghapus pesan dalam chat pribadi
def delete_private_messages(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id  # ID chat pengguna yang mengirim pesan
    user_id = update.message.from_user.id  # ID pengguna yang mengirim pesan
    
    # Mengecek apakah penghapusan pesan diaktifkan dan pengguna ada dalam daftar blacklist
    if bot_status and user_id in blacklisted_users:
        # Menghapus pesan dari pengguna yang diblacklist
        context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
        update.message.reply_text("Pesan Anda telah dihapus karena Anda berada dalam daftar blacklist.")
        logger.info(f"Pesan dari pengguna {user_id} dihapus karena mereka diblacklist.")
    elif not bot_status:
        update.message.reply_text("Penghapusan pesan saat ini dinonaktifkan.")
    else:
        update.message.reply_text("Anda tidak diblacklist, pesan Anda tetap ada.")

# Fungsi untuk menambah pengguna ke blacklist
def add_to_blacklist(update: Update, context: CallbackContext):
    if len(context.args) == 1:
        user_id = int(context.args[0])
        blacklisted_users.add(user_id)
        update.message.reply_text(f"Pengguna dengan ID {user_id} telah ditambahkan ke blacklist.")
        logger.info(f"Pengguna {user_id} ditambahkan ke blacklist.")
    else:
        update.message.reply_text("Format perintah salah. Gunakan /add_blacklist <user_id>.")

# Fungsi untuk menghapus pengguna dari blacklist
def remove_from_blacklist(update: Update, context: CallbackContext):
    if len(context.args) == 1:
        user_id = int(context.args[0])
        if user_id in blacklisted_users:
            blacklisted_users.remove(user_id)
            update.message.reply_text(f"Pengguna dengan ID {user_id} telah dihapus dari blacklist.")
            logger.info(f"Pengguna {user_id} dihapus dari blacklist.")
        else:
            update.message.reply_text(f"Pengguna dengan ID {user_id} tidak ditemukan di blacklist.")
    else:
        update.message.reply_text("Format perintah salah. Gunakan /remove_blacklist <user_id>.")

# Fungsi untuk menampilkan daftar pengguna dalam blacklist
def list_blacklist(update: Update, context: CallbackContext):
    if blacklisted_users:
        user_list = "\n".join([str(user_id) for user_id in blacklisted_users])
        update.message.reply_text(f"Daftar pengguna yang diblacklist:\n{user_list}")
    else:
        update.message.reply_text("Tidak ada pengguna dalam daftar blacklist.")

# Fungsi untuk mengubah status on/off penghapusan pesan
def toggle_bot_status(update: Update, context: CallbackContext):
    global bot_status
    
    if len(context.args) == 1:
        if context.args[0].lower() == 'on':
            bot_status = True
            update.message.reply_text("Penghapusan pesan diaktifkan.")
            logger.info("Penghapusan pesan diaktifkan.")
        elif context.args[0].lower() == 'off':
            bot_status = False
            update.message.reply_text("Penghapusan pesan dinonaktifkan.")
            logger.info("Penghapusan pesan dinonaktifkan.")
        else:
            update.message.reply_text("Gunakan 'on' atau 'off' untuk mengubah status.")
    else:
        update.message.reply_text("Gunakan perintah: /set_status <on/off>")

def main():
    # Masukkan token bot Anda di sini
    TOKEN = "YOUR_BOT_TOKEN"
    
    # Membuat updater dan dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Menambahkan handler untuk perintah
    dp.add_handler(CommandHandler("delete_private", delete_private_messages))
    dp.add_handler(CommandHandler("add_blacklist", add_to_blacklist))
    dp.add_handler(CommandHandler("remove_blacklist", remove_from_blacklist))
    dp.add_handler(CommandHandler("list_blacklist", list_blacklist))
    dp.add_handler(CommandHandler("set_status", toggle_bot_status))

    # Memulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

