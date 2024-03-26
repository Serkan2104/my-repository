from flask import Flask, render_template

app = Flask(__name__)

'''- Create a function named `head` which sends number `number1` and `number2` variables to the `index.html`. 
Use these variables into the `index.html` file. Assign a URL route the `head` function with decorator `@app.route('/')`.
'''
@app.route('/')
def head():
    return render_template("index.html", number1=10, number2= 20)

@app.route('/<string:num1>/<string:num2>')
def mynum(num1, num2):
    return render_template("index.html", number1=num1, number2=num2)

@app.route('/sum/<string:num1>/<string:num2>')
def sum(num1, num2):
    return render_template("body.html", value1=num1, value2=num2, sum= int(num1)+int(num2))



if __name__== "__main__":
    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=8081)