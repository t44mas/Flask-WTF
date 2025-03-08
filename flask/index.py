from flask import Flask, render_template, redirect

from forms.loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index/<title>')
def index(title):
    title = title
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('loginform.html', title='Авторизация', form=form)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    prof = ['врач', 'инженер', 'биолог', 'строитель']
    return render_template('list_prof.html', type=type_list, prof=prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {}
    params['title'] = 'Анкета'
    params['name'] = 'Mark'
    params['surname'] = 'Watny'
    params['education'] = 'среднее'
    params['profession'] = 'штурман марсохода'
    params['sex'] = 'male'
    params['motivation'] = 'Всегда мечтал застрять на Марсе!'
    params['ready'] = True
    return render_template('auto_answer.html', **params)


@app.route('/distribution')
def distribution():
    astronauts = [
        "Юрий Гагарин",
        "Нил Армстронг",
        "Базз Олдрин",
        "Алексей Леонов",
        "Салли Райд",
        "Валентина Терешкова",
        "Крис Хэдфилд",
        "Пегги Уитсон",
        "Сергей Крикалёв",
        "Тим Пик",
    ]
    return render_template('distribution.html', list1=astronauts)


@app.route('/table/<gender>/<age>')
def table(gender, age):
    gender = gender
    age = int(age)
    return render_template('table.html', gender=gender, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
