import discord
import timeutil
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from pandas import DataFrame


# below is a function to get the MangoDB loaded.

def loadDatabase():
  CONNECTION_STRING = "INSERT_STRING_HERE"
  client = MongoClient(CONNECTION_STRING, server_api = ServerApi('1'))
  return(client)

@discord.app_commands.command(name = "get_tasks", description="get list of tasks, duh")
async def getTasks(interaction: discord.Interaction):
  toGive = None
  client = loadDatabase()
  tasksToDo = DataFrame(client.tasks.tasksSaved.find())
  toGive = tasksToDo

  await interaction.response.send_message(toGive)


# TO-DO: 
# 
# Clean up getTasks output on discord client side
# 
# Implement discord function to get all three main things from the user 
# (Task, Date Due, and Low/Med/High Priority)
  
  
    


  
