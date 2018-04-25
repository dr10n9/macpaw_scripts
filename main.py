from flask import Flask
import requests
app = Flask(__name__)



@app.route('/')
def index():
    return("Hello asd")

@app.route('/ip')
def ip():
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    return(ip)


###def application(env, start_response):###
   ### start_response('200 OK', [('Content-Type', 'text/html')])###
   ### return [b"Hello from MacPaw"]###
