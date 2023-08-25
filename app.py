from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "This is first flask test home page"

@app.route('/page2')
def welcome_page2():
    return "This is second page in the test web app"


if __name__=='__main__':
    app.run(debug = True)