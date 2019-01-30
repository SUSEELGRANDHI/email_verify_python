import pymongo
from bson.objectid import ObjectId

class user_plan():

    def __init__(self):
        self.myclient= pymongo.MongoClient("mongodb://ec2-100-24-147-34.compute-1.amazonaws.com:27017/",serverSelectionTimeoutMS = 10000)
        self.mydb = self.myclient["Intelligense_mongo"]
        self.users = self.mydb["users"]
        self.plans = self.mydb["plans"]


    def update_users(self,limit_name):
        if self.user_doc!= None:
            id = self.user_doc["_id"]
            self.user_doc[limit_name] = self.user_doc[limit_name] + 1
            self.users.update({"_id": id},self.user_doc)

    def get_user_plan_id(self,userid,limit_name):
        self.user_doc = self.users.find_one({"_id":ObjectId(userid)})
        if self.user_doc != None:
            plan_name = self.user_doc["plan_name"]
            limit_used = self.user_doc[limit_name]
            plan_doc = self.plans.find_one({"name":plan_name})
            total_limit = plan_doc[limit_name]
            if limit_used < total_limit:
                return True
            else:
                return False
        else:
             return "User doens't exist"