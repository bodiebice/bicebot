import discord
from discord.ext import commands
import logging
from typing import Union, List

logger = logging.getLogger("bicebot")

# class for defining what the bot is
class BiceBot(commands.Bot):
  _PREFIX_ = "^"
  SELF_MENTION: str = None
  # stock bot on_ready stuff here
  async def on_ready(self):
    self.SELF_MENTION = f"<@{self.application_id}>"  # application ID = bot user ID
    logger.info("Syncing commands")
    await self.tree.sync()

    await self.change_presence(
      status=discord.Status.online,
      activity = discord.Streaming(
        name = "pitter patter lets get at 'er",
        url="github.com/bodiebice"
          
      )
    )

    async def get_prefix(self, message: discord.Message, /) -> Union[List[str], str]:
        # returns guild prefix ^
        return self._PREFIX 
    
    async def process_commands(self, message: discord.Message):
      # this framework isn't stock, I could've used stock but a previous bot i worked on
      # made by myself and my good friend Encast used this for command processing. 
      
      # Encast is very smart, his github is pretty rad too,  @Sulaxan

      if message.author.bot:
        return

      ctx = await self.get_context(message)
      # errors are bad. the code below checks for if there's no command, and just returns instead of throwing errors.
      if ctx.command is None:
        return
      await self.invoke(ctx)

    async def on_message(self, message: discord.Message, /) -> None:
      intercept = await self.preprocess_message(message)
      if intercept:
        return
      
      await super().on_message(message)