import os
from flask import Flask, render_template
# , render_template - встроенная функция Фласка для рендера html файла

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
# flask ожидает что html файлы находяться в папке templates которая находиться на уровне run.py


# @app.route путь к файлу + нужно использовать правильный синтаксис ссылок в html
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/career")
def career():
    return render_template("career.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) 
# debug=True не должно быть в завершенном приложении или в проекте отправленном на проверку
# стартовый код для запуска