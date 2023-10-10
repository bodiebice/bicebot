from command import (

  tasks
  # put command scripts into this here
)
import logging
import bicebot

logger = logging.getLogger("bicebot")

def init_commands(bot: bicebot.BiceBot):
  tree = bot.tree
  logger.info("Registering commands to command tree")
  #Area to Register Commands
  tree.add_command(tasks.getTasks)
  logger.info("Done registering all commands")

  logger.info("Registering chat-based commands")
  logger.info("Done registering all chat-based commands")


