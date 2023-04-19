# import statements
import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# logger initialization
logger = logging.getLogger(__name__)

# funiction of configuration and launch bot
async def main():
    
    # logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    # output to console information about launch bot
    logger.info('Starting bot')

    # load configuration to variable config
    config: Config = load_config()

    # bot and dispatcher initialization
    bot: Bot = Bot(config.tg_bot.token, parse_mod='HTML')
    dp: Dispatcher = Dispatcher()

    # routers registration in dispatcher
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # missing accumulated updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
