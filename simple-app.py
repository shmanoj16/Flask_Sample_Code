#!/usr/bin/env python

from flask import Flask, Response,request


app = Flask(__name__)


@app.route("/")
def hello():
    return Response("Hi from your Flask app running in your Docker container!")

@app.route("/test")
def test():
    return Response("Hi! This is test response")


@app.route('/sum',methods=['GET','POST'])
def sum_fn():
    x=int(request.args.get('x'))
    y=int(request.args.get('y'))
    sum=x+y
    return {'data':sum}

if __name__ == "__main__":
    app.run("0.0.0.0", port=1234, debug=True)
