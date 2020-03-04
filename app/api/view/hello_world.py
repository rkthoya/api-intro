from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    user = [{'user_id':1,'username':'richie','email':'email.com'},
            {'user_id':2,'username':'2','email':'2.com'},
            {'user_id':3,'username':'3','email':'3.com'}]
    return {'users':user}