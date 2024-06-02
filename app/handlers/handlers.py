from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from parser import get_data
from config import timezone

from dotenv import load_dotenv
import os

load_dotenv('../../config/.env')

minute = int(os.getenv("MINUTE"))
hour = int(os.getenv("HOUR"))
word: str = os.getenv("WORD")

rt = Router(name='news')


@rt.message(CommandStart())
async def start(msg: Message):
    await msg.answer(f"Hi, {msg.from_user.first_name}.\n"
                     f"This bot can monitor the news from Binance.\n"
                     f"To start, type /monitoring")


@rt.message(Command(commands=["monitoring"]))
async def news(message: Message, bot: Bot, scheduler: AsyncIOScheduler):
    ids = message.from_user.id
    await message.answer(
        text=f"Monitoring started.\nWord: {word}.\n"
             f"Bot will notice you everyday in "
             f"{hour}:{str(minute) + "0" if minute == 0 else minute} {timezone.TIMEZONE}"
    )
    scheduler.add_job(bot.send_message, 'cron', hour=hour, minute=minute,
                      args=(ids, (get_data() if get_data()
                                  else datetime.now(timezone.TIMEZONE).strftime("%d.%m.%Y %H:%M:%S"))))
