import flask
from flask import request, jsonify,Response
from user_plan import user_plan
from flask_cors import CORS
import emailverifier as ev

user_id = "5c25cf3b9f23431252703981"
user = user_plan()
bool_ = user.get_user_plan_id(user_id)
print(bool_)
if bool_ == True:
     result = ev.checkUsername("prathasaxena30@gmail.com")
     result = {"status":"verified","confidence":result}
     if len(result)> 0:
            user.update_users()
     print(result)

