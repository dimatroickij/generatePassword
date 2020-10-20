import random

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash

from app import app, db
from app.forms import LoginForm, RegistrationForm, EditPassword
from app.models import User


@app.route('/')
@login_required
def hello_world():
    return render_template("lr1.html")


@app.route('/login/', methods=['post', 'get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('hello_world'))

        flash('Неправильный логин или пароль')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/registration/', methods=['post', 'get'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('hello_world'))

    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form.get('username')).first()
            if user:
                flash('Пользователь с таким логином уже существует')
                return redirect(url_for('registration'))

            newUser = User(username=request.form.get('username'),
                           password_hash=generate_password_hash(request.form.get('password')),
                           name=request.form.get('name'), surname=request.form.get('surname'),
                           middlename=request.form.get('middlename'), birthday=request.form.get('birthday'),
                           placeBirth=request.form.get('placeBirth'), tel=request.form.get('tel'))
            db.session.add(newUser)
            db.session.commit()
            flash('Вы успешно зарегистрировались в системе')
            return redirect(url_for('login'))

    return render_template('registration.html', form=form)


# длина пароля 6 символов, символы - латиница (строчные символы), при смене пароля: проверка на отсутствие повторяющихся символов
@app.route('/editPassword/', methods=['post', 'get'])
@login_required
def editPassword():
    form = EditPassword()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == current_user.username).first()
        if user and user.check_password(form.lastPassword.data):
            lastPassword = set(list(form.lastPassword.data))
            newPassword = set(list(form.newPassword.data))
            if (len(lastPassword) == len(lastPassword - newPassword)):
                if form.newPassword.data == form.newPasswordRepeat.data:
                    user.password_hash = generate_password_hash(form.newPassword.data)
                    db.session.commit()
                    logout_user()
                    flash('Вы успешно сменили пароль')
                    return redirect(url_for('login'))
                flash('Введённые пароли не совпадают')
                return redirect(url_for('editPassword'))

            flash('Новый пароль содержит символы из старого пароля')
            return redirect(url_for('editPassword'))

        flash('Вы ввели неверный пароль')
        return redirect(url_for('editPassword'))
    return render_template('editPassword.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из системы")
    return redirect(url_for('login'))


@app.route('/generatePassword')
def generatePassword():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    symbols = """!"#$%&'()*"""
    id = request.args.get('inputId')
    b1 = alphabet[random.randint(0, 25)].upper()
    b2 = alphabet[random.randint(0, 25)].upper()
    b3 = str((len(id) ** 2) % 10)
    b4 = str(random.randint(0, 9))
    b5 = symbols[random.randint(0, 9)]
    b6 = alphabet[random.randint(0, 25)]
    alphabet.upper()
    return b1 + b2 + b3 + b4 + b5 + b6