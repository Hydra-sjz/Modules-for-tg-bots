from os import mkdir, path

from mbot import Mbot, bot, logger

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    Mbot().run()

with bot:
    bot.run_until_disconnected()
    logger.info('BOT STOPPED BROOO')
    bot.loop.run_until_complete(fetch.session.close())
