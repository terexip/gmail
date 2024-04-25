import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["فرعون","المبرمج فرعون","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e2120ef2b55fbd6e7b00e.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ᯓ 𓆩 ˹𝒑𝒓𝒐𝒈𝒓𝒂𝒎𝒎𝒆𝒓 𝒇𝒓𝒂𝒐𝒏˼《𝑆》™𝑃𝐹𓆪 𓆃˼](https://t.me/PV_FR3ON)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @PV_FR3ON ❫
◉ 𝙸𝙳      : ❪ 5490392130 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ ҒᎡ3ΌΝ", url=f"https://t.me/PV_FR3ON"), 
                 ],[
                   InlineKeyboardButton(
                        "☭ ՏΌႮᎡᏟᎬ  ҒᎡ3ΌΝ ☭", url=f"https://t.me/sorcefraon"),
                ],

            ]

        ),

    )
