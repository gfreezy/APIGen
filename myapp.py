#import MySQLdb
from flask import Flask, g, request
from flask import render_template

app = Flask(__name__)
app.debug = True
@app.route('/')
def hello():
    return render_template('hello.html') 

if __name__ == '__main__':
    app.run()
