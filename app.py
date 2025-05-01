from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
            <html>
            <body>
                <h1>Главная страница</h1>
                <p> <font color='red'> Вы создали свой первый сайт!</font></p>
                <a href="/hello/"> Перейти на страницу приветствия</a>
            </body>
            </html>
            """

@app.route('/hello/')
def hello():

    return """
            <html>
            <body>
                <h1>Страница приветсвия</h1>
                <p> <font color='red'> Что-бы перейти на Главную нажмите на ссылку ниже</font></p>
                <a href="/"> Перейти на Главную</a>
                <p> <font color='green'> Что-бы перейти к работе нажмите на ссылку ниже</font></p>
                <a href="/"> Перейти на Главную</a>
            </body>
            </html>
            """



if __name__ == "__main__":
    app.run()