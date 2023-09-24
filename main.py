import logging

from bot import BotSubclass

logging.basicConfig(
    level = logging.INFO, filename="bot.log",
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    bot = BotSubclass()
    bot.setup()
    bot.run()


