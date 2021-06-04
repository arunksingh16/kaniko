from flask import Flask, render_template, request, url_for, flash, redirect
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi This Image was build inside Kubernetes Cluster using Kaniko !"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
