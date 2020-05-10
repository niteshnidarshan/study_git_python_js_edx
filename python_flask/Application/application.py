from flask import Flask # Import class 'Flask' from the module 'flask'
app = Flask(__name__)   # Instantiating a new web application called app.
                        # __name__ represents current file.

@app.route("/")         # aA decorator, which defines when a user goes to the route '/', then immediate below method will run.
def index():
    return "Hello World!"

@app.route("/user")
def getUserDetails():
    return {"user":"nitesh","password":"nidarshan"}

@app.route("/string")
def getString():
    name="nidarshan"
    return name[1]
