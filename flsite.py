from flask import Flask
from flask import render_template
from flask import url_for
from flask import flash
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiop'
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

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error') 
    return render_template('contact.html', title='Обратная связь', menu=menu)

if __name__ == "__main__":
    app.run(debug=True)