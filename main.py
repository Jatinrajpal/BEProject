from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html",title="home")


@app.route("/register")	
def register():
    return render_template("register.html",title="register")
    		
@app.route("/about")
def about():
    return "<h1>About Page</h1>"
if __name__ == '__main__':
    app.run(debug=True,port=8080)