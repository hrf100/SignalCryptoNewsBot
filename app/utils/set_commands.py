from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from loguru import logger


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='start'
        ),
        BotCommand(
            command='monitoring',
            description='start monitoring'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
    logger.info('Starting commands are successfully configured')
