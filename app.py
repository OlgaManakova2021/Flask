import pickle
# import sklearn
# import numpy

import flask
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/') #127.0.0.1:5000 + /  =  127.0.0.1:5000/
# def index():
#     return """
#             <html>
#             <body>
#                 <h1>Главная страница</h1>
#                 <p><font color='red'>Это учебная страница</font></p>
#                 <h2><a href='/example'>Страница приветствия ...</a></h2>
#             </body>
#             </html>
#             """
#
# @app.route('/example') #127.0.0.1:5000 + /example = 127.0.0.1:5000/example
# def example():
#     return """
#             <html>
#             <body>
#                 <h1>Страница приветствия</h1>
#                 <p><font color='green'>Здесь может быть любое содержимое ...</font></p>
#                 <h2><a href='/'>На главную</a></h2>
#             </body>
#             </html>
#             """

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/example')
def example():
    return render_template('index_hello.html')

@app.route('/salary', methods = ['POST', 'GET'])
def main():
    if flask.request.method == "GET":
        return render_template("main.html")

    if flask.request.method == "POST":
        with open('lr_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        exp = float(flask.request.form['experience'])
        y_pred = loaded_model.predict([[exp]])

        return render_template("main.html", result = int((y_pred[0])))


if __name__ == "__main__":
    app.run()