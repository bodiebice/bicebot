from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pandas import DataFrame 



def loadDatabase():
  uri = "INSERT_STRING_HERE"
  client = MongoClient(uri, server_api = ServerApi('1'))

  try:
    client.admin.command('ping')
    print("Pinged your deployment. Success")
  except Exception as e:
    print(e)
  print(client.list_database_names())
  tasksDB = client['tasks']
  item_details = tasksDB.tasksSaved.find()
  
  
  return(item_details)



if __name__ == "__main__":
  items = loadDatabase()
  items_df = DataFrame(items)
  print(items_df)
