import pymongo 
from mail_finder_duckduckgo import get_emails_duck
from mail_finder_google import get_emails_google

class CheckDatabase():
    
    def __init__(self,domain):
        self.myclient= pymongo.MongoClient("mongodb://ec2-100-24-147-34.compute-1.amazonaws.com:27017/",serverSelectionTimeoutMS = 10000)
        self.intelligense = self.myclient["Intelligense_mongo"]
        self.organisation = self.intelligense["organisations"]
        self.people = self.intelligense["people"]
        self.domain_col = self.intelligense["domain_search"]
        self.domain = domain
        self.organisation_doc = self.organisation.find_one({'domain': self.domain})
        self.email_list = []


    def check_database(self):
        if self.organisation_doc != None:
            organisation_id = self.organisation_doc["_id"]
            people_cols = self.people.find({'organisation_id': organisation_id})
            if people_cols.count() > 0:
                for people_col in people_cols:
                    self.email_list.append(people_col["email"])
                return self.email_list
            else:
                return [] 
        else:
            domain_org = self.domain_col.find({'domain':self.domain})
            if domain_org.count() > 0:
                for domain in domain_org:
                    self.email_list.append(domain["email"])
                return self.email_list
            else:
                return [] 
                

    def search_duckduckgo(self):
        self.email_list =  get_emails_duck(self.domain)
        return self.email_list
    
    def search_google(self):
        print("email_list ", self.email_list)
        self.email_list = get_emails_google(self.domain)
        return self.email_list

    def people_save(self):
         if self.organisation_doc != None:
             print("save")
             organisation_id = self.organisation_doc["_id"]
             for email in self.email_list:
                 info = {}
                 info["email"] = email
                 info["organisation_id"] = organisation_id
                 self.people.update({'email':email},info, upsert= True)
         else :
              for email in self.email_list:
                 info = {}
                 info["email"] = email
                 info["domain"] = self.domain
                 self.domain_col.update({'email':email},info, upsert= True)