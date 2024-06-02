from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv('../config/.env')

token: str = os.getenv("TOKEN")

bot = Bot(token)

dp = Dispatcher()

__all__ = (
    "bot",
    "dp"
)
