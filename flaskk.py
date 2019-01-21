import flask
import emailverifier as ev
from flask import request, jsonify,Response
from user_plan import user_plan
from flask_cors import CORS,cross_origin

app = flask.Flask(__name__)
CORS(app)

@app.route('/email_verify/', methods=['GET'])
def home():
    print("hey")
    email = request.args["email"]
    user_id = request.args["id"]
    user = user_plan()
    bool_ = user.get_user_plan_id(user_id)
    resp = Response("")
    if bool_ == True:
        result = ev.checkUsername(email)
        if len(result)> 0:
            user.update_users()
        resp = Response(str(result))
    if bool_ == False:
        resp = Response(str({"message":"You have exceeded your Email vefifier limit"}))
    if type(bool_) == str :
        resp =  Response(str({"message":"User does not exit"}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
