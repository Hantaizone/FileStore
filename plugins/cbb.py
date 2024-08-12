#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href=https://t.me/CheaterKiMaakabhosda'>sᴀᴠɪᴛᴀʀ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/hiutffh'>ʜᴇɴᴛᴀɪ ɴᴀᴛɪᴏɴ</a>\n○ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : <a href='https://t.me/+z-K6wvsuO8Q0YjA1'>ʜ*ɴᴛᴀɪ ɴᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ ᴢᴏɴᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('⛩️ ʜᴏᴍᴇ ⛩️ ', url='https://t.me/h3ntai_nation')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
