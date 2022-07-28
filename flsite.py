from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)
menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='О сайте', menu=menu)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Обратная связь', menu=menu)

if __name__ == "__main__":
    app.run(debug=True)