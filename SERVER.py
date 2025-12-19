from flask import Flask

app = Flask(__name__)
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
"""
@app.route('/user/<name>/<int:age>')
def my_mame(name, age):
    return f'<h1>My name is {name}.I\'m {age+1} years old.</h1>'

#@app.route('/calculator/addition/<int:a>/<int:b>')
#def addition(a,b):
  #return f'<h1>{a} + {b} = {a+b}<h1>'

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a,b):
    return f'<h1>{a} - {b} = {a-b}</h1>'

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a,b):
    return f'<h1>{a} * {b} = {a*b}</h1>'

app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a,b):
    return f'<h1>{a} / {b} = {a/b}<int:a>/</h1>'

@app.route('/calculator/power/<float:basee>/<floar:exponent>')
def power(base,exponent):
    return f'<h1>{base} <sup> {base} </sup> = {base**exponent}</h1>'
