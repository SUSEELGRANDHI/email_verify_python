import flask
import emailverifier as ev
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/email_verify/', methods=['GET'])
def home():
    email = request.args["email"]
    return jsonify(ev.emailVerifier(email))

app.run()
