import asyncio

import utils
import handlers
from loader import dp, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from middleware import SchedulerMiddleware
from config import timezone


async def main():
    scheduler = AsyncIOScheduler(timezone=timezone.TIMEZONE)
    scheduler.start()
    dp.update.middleware(SchedulerMiddleware(scheduler=scheduler))
    dp.include_router(handlers.rt)
    await utils.set_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    utils.setup_logger("INFO", ["aiogram.bot.api"])
    asyncio.run(main())
