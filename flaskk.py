import flask
import emailverifier as ev
from flask import request, jsonify
from user_plan import user_plan

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/email_verify/', methods=['GET'])
def home():
    email = request.args["email"]
    user_id = request.args["id"]
    user = user_plan()
    bool = user.get_user_plan_id(user_id)
    if bool == True:
        result = ev.emailVerifier(email)
        if len(result)> 0:
            user.update_users()
        return jsonify(result)
    if bool == False:
        return jsonify({"message":"You have exceeded your Email vefifier limit"})
    if type(bool) == str :
        return jsonify({"message":"User does not exit"})

app.run()
