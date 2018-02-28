from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return "<h1>Hello, I'm Back</h1> <h3>Your Browser is %s</h3> <p>Follow my lead</p>" %user_agent

@app.route('/user/<name>')
def user(name):
    return "<h3>Welcome %s!</h3>" %name



if __name__=='__main__':
    app.run(debug = True)
