import pymongo
from bson.objectid import ObjectId

class user_plan():

    def __init__(self):
        self.myclient= pymongo.MongoClient("mongodb://ec2-100-24-147-34.compute-1.amazonaws.com:27017/",serverSelectionTimeoutMS = 10000)
        self.mydb = self.myclient["Intelligense_mongo"]
        self.users = self.mydb["users"]
        self.plans = self.mydb["plans"]

    def get_user_plan_id(self,userid):
        self.user_doc = self.users.find_one({"_id":ObjectId(userid)})
        if self.user_doc != None:
            plan_name = self.user_doc["plan_name"]
            email_verification_limit_used = self.user_doc["email_verification_limit"]
            plan_doc = self.plans.find_one({"name":plan_name})
            total_limit = plan_doc["email_verification_limit"]
            if email_verification_limit_used < total_limit:
                return True
            else:
                return False
        else:
             return "User doens't exist"

    def update_users(self):
        if self.user_doc!= None:
            id = self.user_doc["_id"]
            self.user_doc["email_verification_limit"] = self.user_doc["email_verification_limit"] + 1
            self.users.update({"_id": id},self.user_doc)
