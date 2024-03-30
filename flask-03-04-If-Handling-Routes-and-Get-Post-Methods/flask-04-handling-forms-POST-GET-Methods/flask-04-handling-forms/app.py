# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app

app = Flask(__name__)
# Create welcome page with main.html file and assign it to the root path
@app.route("/")
def home():
    return render_template("main.html", name= "SERKAN")

# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised



# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')


# Add a statement to run the Flask application
if __name__ == "__main__":
    app.run(debug=True)