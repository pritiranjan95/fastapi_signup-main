from pymongo import MongoClient
from Config.database import mongo_client, DB


class MonogoConnection():
    def __init__(self) -> None:
        self.mongoclient=None
        self.database=None
        self.host=None
        self.port=None

    def __init__(self,host,port) -> None:
        self.host=host
        self.port=port
        self.mongoclient=MongoClient(host,port)

    def __init__(self,url) -> None:
        self.url=url
        self.mongoclient=MongoClient(self.url)
    
    
    
    def get_database(self,db_name):                   #We can call it eith 2nd or 3rd constructor
        self.database=self.mongoclient[db_name]
        return self.database
    
    def get_database_with_host(self,db_name,host,port):              #We can call it with the first constructor

        self.mongoclient=MongoClient(host,port)
        self.database=self.mongoclient[db_name]
        return self.database


# mongo_client="mongodb://localhost:27017"
# DB= "User_Details"

db=MonogoConnection(mongo_client)
db=db.get_database(DB)

# if __name__=="__main__":
#     db["demo_collection"].insert_one({"Name":"Bapi"})

