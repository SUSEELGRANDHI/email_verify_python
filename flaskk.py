import flask
from techfinder.wappalyzerr import techfind
import emailverifier as ev
from flask import request, jsonify,Response
from user_plan import user_plan
from flask_cors import CORS,cross_origin
from domainsearch.check_database import CheckDatabase
from twitter_search.search_tweets import TwitterSearch

app = flask.Flask(__name__)
CORS(app)


@app.route('/get_tweets',methods=['GET'])
def get_tweets():
    keyword = request.args["keyword"]
    twitter = TwitterSearch()
    response = twitter.get_tweets(keyword)
    return jsonify({'response': response})


@app.route('/domain_search', methods = ['GET'])
def domain_search():
    email_list = []
    domain = request.args["domain"]
    user_id = request.args["id"]
    user = user_plan()
    bool = user.get_user_plan_id(user_id,"domain_search_limit")
    if bool == True:
        print("bool is true")
        cd = CheckDatabase(domain)
        email_list = cd.check_database()
        if len(email_list) == 0:
            print("not in db")
            try:
                email_list = cd.search_google()
            except Exception as e:
                email_list = cd.search_duckduckgo()
            if len(email_list)>0:
                cd.people_save()
        user.update_users("domain_search_limit")
        return jsonify({'emails': email_list})
    else:
        return jsonify({'limit':'exceeded'})


@app.route('/tech_finder/', methods = ['POST'])
def techfinderapi():
    #url = 'http://www.nupowerrenewables.in/'
    url = request.form['websiteurl']
    print(url)
    return jsonify(techfind(url))


@app.route('/email_verify/', methods=['GET'])
def home():
    print("hey")
    email = request.args["email"]
    user_id = request.args["id"]
    user = user_plan()
    bool_ = user.get_user_plan_id(user_id,"email_verification_limit")
    if bool_ == True:
        result = ev.checkUsername(email)
        if len(result)> 0:
            user.update_users("email_verification_limit")
        return jsonify(result)
    if bool_ ==False:
        return jsonify({"message": "you have exceeded your email verifier limit"})
    if type(bool_) == str :
        return  jsonify({"message":"User does not exit"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
