from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from config import OWNER_ID

Muntazer = "eo_u7"
@app.on_message(filters.private & filters.user(OWNER_ID))
async def must_join_channel(_, message):
    if "‹ قناة الاشتراك ›" in message.text:
        link = f"https://t.me/{Muntazer}"
        await message.reply(
            text=f"~ عزيزي المطور \n~ هذا هي قناة الاشتراك الاجباري @{Muntazer} .",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 🎧", url=f"https://t.me/SOURCELARIN")],
            ])
        )
        
