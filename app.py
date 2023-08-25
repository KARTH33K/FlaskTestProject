from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "This is first flask test home page"

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The person passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person failed and the marks are: " + str(score)

##result check
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"

    return redirect(url_for(result, score=marks))


if __name__=='__main__':
    app.run(debug = True)