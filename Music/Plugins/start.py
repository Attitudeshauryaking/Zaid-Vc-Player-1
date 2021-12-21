import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import UPDATES_CHANNEL, ZAID_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""**A Telegram Moti music bot.
 Add Me To Ur Chat For and Help and And Support Click On Buttons  ...
💞  These Features A.I Based 
Powered By [𝔸𝕥𝕥𝕚𝕥𝕦𝕕𝕖 ℕ𝕖𝕥𝕨𝕠𝕣𝕜](Https://t.me/Attitude_Network) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝔸𝔻𝔻 𝕄𝔼 𝕋𝕆 𝕐𝕆𝕌ℝ 𝔾ℝ𝕆𝕌ℙ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "★𝕆𝕎ℕ𝔼ℝ★", url=f"Https://t.me/ItsAttitudeking"
                    ),
                    InlineKeyboardButton(
                        "ཧᜰ꙰ꦿ➢𝐎𝐀𝐍༒☛", url="https://github.com/ItsAttitudeking"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡𝕌ℙ𝔻𝔸𝕋𝔼𝕊⚡", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "🥂𝕊𝕌ℙℙ𝕆ℝ𝕋🥂", url=f"https://t.me/{ZAID_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️ © @Attitude_Network""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝕁𝕆𝕀ℕ ℍ𝔼ℝ𝔼", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨ © @Attitude_Network""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/ItsAttitudeking")
                ]
            ]
        ),
    )
