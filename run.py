import os

import json
# Next, go back to the run.py file, and now we want Python to import the data.
# To do that, we first need to import the JSON library, because we're going to be passing
# the data that's coming in as JSON.

from flask import Flask, render_template, request, flash
# , render_template - встроенная функция Фласка для рендера html файла
# request - встроенная функция Фласка для передачи запросов (форм)
# Sometimes we want to display a non-permanent message to the user, something that only stays on screen until we refresh the page, or go to a different one. These are called 'flashed messages' in Flask. Чтобы использовать флеш-сообщения, нам нужно создать секретный ключ, потому что Flask криптографически подписывает все сообщения в целях безопасности. Это может показаться сложным, но на самом деле все, что нам нужно сделать, это предоставить секретный ключ. который Flask может использовать для подписи сообщений.

if os.path.exists("env.py"):
    import env
# Теперь мы можем вернуться к нашему файлу run.py, и под нашим импортом вверху нам просто нужно чтобы импортировать еще одну библиотеку, называемую env. Но мы хотим импортировать env только в том случае, если система может найти файл env.py. если os.path.exists("env.py"): импортировать env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
# We now want to grab the hidden variable, which we've called SECRET_KEY. To use it, after we instantiate our app, we need to write: app.secret_key = os.environ.get("SECRET_KEY").


@app.route("/")
def index():
    return render_template('index.html')
# flask ожидает что html файлы находяться в папке templates которая находиться на уровне run.py


# @app.route путь к файлу + нужно использовать правильный синтаксис ссылок в html
@app.route("/about")
def about():
    data = []
    
    # We need to have Python open the JSON file in order to read it. This is called a 'with' block.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # записываем в data то что прочитал json

    return render_template("about.html", page_title="About", list_of_numbers = [1,2,3], company=data)
                                    #  add new argument to function render_template
                                    # It's best practice to use an underscore when defining python variables.
                                    # доьбавляем новый аргумент company который возвращает render_template 
                                    # и присваеваем ему значение data  


@app.route("/about/<member_name>")
# Угловые скобки будут передавать данные из URL-пути в наше представление ниже, и я решил назвать этот параметр: 'member_name'.
def about_member(member_name):
    member = {}
    # We need to have Python open the JSON file in order to read it. This is called a 'with' block.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # записываем в data то что прочитал json
        for obj in data:
            # loop in data
            # Затем мы хотим проверить, совпадает ли ключ URL этого объекта из файла с именем member_name, через которое мы прошли из пути URL. if obj["url"] == member_name: Если они совпадают, то мы хотим, чтобы наш пустой объект 'member' из строки 24 был равен объекту в этом экземпляре цикла.
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# Причина, по которой это происходит, заключается в том, что по умолчанию все представления Flask будут обрабатывать GET-запрос. Если нам нужно начать обрабатывать что-то помимо этого, например, POST или другие методы, DELETE или PUT, тогда нам нужно явно указать, что наш маршрут может принимать эти методы. method=["GET", "POST"]

# К объекту запроса также прикреплено гораздо больше вещей. Когда мы отправляем форму, к ней фактически прикреплен объект формы.

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
        # ImmutableMultiDict([('name', 'Mike'), ('email', 'bilanmo88@gmail.com'), ('phone', '+49155636401'), ('message', 'Hello')])
        print(request.form.get("name"))
        # Because this is a dictionary, we can actually use a standard Python method of accessing the keys for that dictionary. If I print(request.form.get("name")), this will allow us to get the 'name' value from - Mike1412
        print(request.form["email"])
        # другой вид записи. получаем значение email

        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
        
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) 
# debug=True не должно быть в завершенном приложении или в проекте отправленном на проверку
# стартовый код для запуска