from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import *

from PyroUbot import *


def detect_url_links(text):
    link_pattern = (
        r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?"
    )
    link_found = re.findall(link_pattern, text)
    return link_found


def detect_button_and_text(text):
    button_matches = re.findall(r"\| ([^|]+) - ([^|]+) \|", text)
    text_matches = (
        re.search(r"(.*?) \|", text, re.DOTALL).group(1) if "|" in text else text
    )
    return button_matches, text_matches


def create_inline_keyboard(text, user_id=False, is_back=False):
    keyboard = []
    button_matches, text_matches = detect_button_and_text(text)

    prev_button_data = None
    for button_text, button_data in button_matches:
        data = (
            button_data.split(";same")[0]
            if detect_url_links(button_data.split(";same")[0])
            else f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]} {button_data.split(';same')[0]}"
        )
        cb_data = data if user_id else button_data.split(";same")[0]
        if ";same" in button_data:
            if prev_button_data:
                if detect_url_links(cb_data):
                    keyboard[-1].append(InlineKeyboardButton(button_text, url=cb_data))
                else:
                    keyboard[-1].append(
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    )
            else:
                if detect_url_links(cb_data):
                    button_row = [InlineKeyboardButton(button_text, url=cb_data)]
                else:
                    button_row = [
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    ]
                keyboard.append(button_row)
        else:
            if button_data.startswith("http"):
                button_row = [InlineKeyboardButton(button_text, url=cb_data)]
            else:
                button_row = [InlineKeyboardButton(button_text, callback_data=cb_data)]
            keyboard.append(button_row)

        prev_button_data = button_data

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if user_id and is_back:
        markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    "ᴋᴇᴍʙᴀʟɪ",
                    f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]}",
                )
            ]
        )

    return markup, text_matches


class BTN:
    def ALIVE(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def BOT_HELP(message):
        button = [
            [InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ", callback_data="reboot")],
            [InlineKeyboardButton("sᴛᴀᴛs", callback_data="stats")],
            [InlineKeyboardButton("ᴜʙᴏᴛ", callback_data="getubot")],
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", callback_data="update")],
            [InlineKeyboardButton("sʜᴜᴛᴅᴏᴡɴ", callback_data="shutdown")],
        ]
        return button

    def ADD_EXP(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} ʙᴜʟᴀɴ",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "👤 ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏꜰɪʟ 👤", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "❌ ᴛᴏʟᴀᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ❌", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def EXP_UBOT():
        button = [
            [InlineKeyboardButton("💵 ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ 💵", callback_data="bahan")],
        ]
        return button

    def START(message):
        button = [
            [InlineKeyboardButton("💵 ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ 💵", callback_data="bahan"),
            InlineKeyboardButton("💬 ʟɪᴠᴇ ᴄʜᴀᴛ 💬", callback_data="support")],
            [
                InlineKeyboardButton(
                    "🤖 sᴛᴀᴛᴜs ᴀᴋᴜɴ", callback_data="status"
                ),
                InlineKeyboardButton(
                    "ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ⚒️", callback_data="buat_ubot"
                ),
            ],
            [
                InlineKeyboardButton(
                    "👥 ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ", url="https://t.me/ZacnnSupport"
                ),
                InlineKeyboardButton(
                    "💠 ᴍᴏᴅᴜʟᴇ", callback_data="help_back"
                ),
            ],
        ]
        return button

    def PLUS_MINUS(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("✅ ᴋᴏɴꜰɪʀᴍᴀsɪ", callback_data="confirm")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {user_id}")],
        ]
        return button

    def UBOT(user_id, count):
        button = [
            [InlineKeyboardButton("📁 ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ 📁", callback_data=f"del_ubot {int(user_id)}")],
            [InlineKeyboardButton("⏳ ᴄᴇᴋ ᴋᴀᴅᴀʟᴜᴀʀꜱᴀ ⏳", callback_data=f"cek_masa_aktif {int(user_id)}")],
            [InlineKeyboardButton("🔑 ᴄᴇᴋ ᴏᴛᴘ 🔑", callback_data=f"get_otp {int(count)}")],
            [InlineKeyboardButton("☠ ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ ☠", callback_data=f"ub_deak {int(count)}")],
            [
                InlineKeyboardButton("⬅️", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"n_ub {int(count)}"),
            ],
            [InlineKeyboardButton("ᴋᴇᴍʙᴀʟɪ", callback_data="balik")],
        ]
        return button

    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "🔙 ᴋᴇᴍʙᴀʟɪ",
                    callback_data=f"p_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "sᴇᴛᴜJᴜɪ ✅", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button
