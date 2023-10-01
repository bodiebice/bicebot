import discord
import config
import command_manager
import time
import signal
import logging
import bicebot

logger = logging.getLogger("bicebot")

def init():
  logger.setLevel(logging.INFO)



def init_bot(bot: bicebot.BiceBot):
  command_manager.init_commands(bot)

def main():
  intents = discord.Intents.default()
  intents.message_content = True

  bot = bicebot.BiceBot(intents = intents, command_prefix = None)

  if config.get(config.CONFIG_BOT_TOKEN) is None:
    logger.critical(f"No {config.CONFIG_BOT_TOKEN} environment variable set")
    return
  
  init_bot(bot)
  bot.run(config.get(config.CONFIG_BOT_TOKEN))

if __name__ == "__main__":
  init()
  main()

