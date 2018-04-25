from flask import Flask
import requests
app = Flask(__name__)



@app.route('/')
def index():
    return(open("index.html", "r").read())

@app.route('/ip')
def ip():
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    return(ip)

@app.route('/css/style.css')
def style():
    return(open('css/style.css', 'r').read())

@app.route('/tmp')
def tmp():
    return(open('tmp.html', 'r').read())

###def application(env, start_response):###
   ### start_response('200 OK', [('Content-Type', 'text/html')])###
   ### return [b"Hello from MacPaw"]###
