import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents = intents)

key = "MTA2MzUwOTMyMTI2ODM0Njk2MQ.GOomV0.iAba57Se68tvcOEJAxxG2tDfiFi7Ktb06GEp8Q"
# event listen for when bot is running
@bot.event
async def on_ready():
  guild_count = 0

  for guild in bot.guilds:
    print(f"- {guild.id} (name: {guild.name})")
    
    guild_count = guild_count + 1
  
  print("Sample DiscordBot is in " +str(guild_count) + " servers.")


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
  
bot.run(key)

