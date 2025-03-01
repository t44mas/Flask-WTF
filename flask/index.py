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
    params['name'] = 'Марк'
    return render_template('auto_answer.html', **params)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
