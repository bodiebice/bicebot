import discord
import timeutil
from pymongo import MongoClient
import config


# below is a function to get the MangoDB loaded.

def loadDatabase():
  CONNECTION_STRING = config.get(config.MONGO_CONNECTION_STRING)
  client = pymongo.MongoClient(CONNECTION_STRING)
  tasksDB = client[tasks]
  


class task():
  def __init__(self, title, duedate):
    self.title = title
    self.duedate = parser.parse(duedate)

  def updateTitle(self, newTitle):
    self.title = newTitle
  
  def updateDueDate(self, newDate):
    self.duedate = parser.parse(newDate)


class tasklist(commands.Cog):
  object


  def __init__(self, bot):
        self.bot = bot
        self._last_member = None
  
