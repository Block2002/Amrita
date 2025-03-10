# Don't Remove/Edit This Line 👇
# Created By - @ProBotts || @ZeoXpro


from JioSavaan import app
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from logging import getLogger
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from pyrogram import Client, filters
from JioSavaan.utils.database import add_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from JioSavaan.utils.database import get_assistant
import asyncio
from JioSavaan import app
import asyncio
import random
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from JioSavaan.utils.database import get_assistant, is_active_chat



random_photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]
# --------------------------------------------------------------------------------- #





LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None



def circle(pfp, size=(500, 500), brightness_factor=10):
    pfp = pfp.resize(size, Image.Resampling.LANCZOS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.Resampling.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname, brightness_factor=1.3):
    background = Image.open("JioSavaan/assets/20250120_214235.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor) 
    pfp = pfp.resize((512, 512))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('JioSavaan/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('JioSavaan/assets/font.ttf', size=61)
#Module Made By @ProBotts || Dev - @YasirAkhtar
    draw.text((490, 778), f'{user}', fill=(23, 156, 241), font=font)
    draw.text((315, 890), f'{id}', fill=(34, 34, 34), font=font)
    draw.text((700, 1010), f"@{uname}", fill=(34, 34, 34), font=font)

    #
    pfp_position = (162, 161)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"


@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "ᴜsᴀɢᴇ:\n⦿ /welcome [on|off]"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title}")
        elif state == "on":
            if not A:
                await message.reply_text("ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!")



@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    count = await app.get_chat_members_count(chat_id)
    A = await wlcm.find_one(chat_id)
    if A:
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    
    # Add the modified condition here
    if member.new_chat_member and not member.old_chat_member and member.new_chat_member.status != "kicked":
    
        try:
            pic = await app.download_media(
                user.photo.big_file_id, file_name=f"pp{user.id}.png"
            )
        except AttributeError:
            pic = "JioSavaan/assets/upic.png"
        if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
            try:
                await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
            except Exception as e:
                LOGGER.error(e)
        try:
            welcomeimg = welcomepic(
                pic, user.first_name, member.chat.title, user.id, user.username
            )
            button_text = "๏ ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ ๏"
            add_button_text = "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏"
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"
            temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
                member.chat.id,
                photo=welcomeimg,
                caption=f"""
◦•●◉✿ ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ ✿◉●•◦ 

▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰
➻ ɴᴀᴍᴇ » {user.mention}
➻ ᴜsᴇʀ ɪᴅ » {user.id}
➻ ᴜsᴇʀɴᴀᴍᴇ » @{user.username}
➻ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs » {count}
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰

◦•●◉✿✿◉●•◦●∘◦❀◦∘●◦•●◉✿✿◉●•◦
""",

                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
        except Exception as e:
            LOGGER.error(e)
# Don't Remove/Edit This Line 👇
# Created By - @ProBotts || @ZeoXpro
