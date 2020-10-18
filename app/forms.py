from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить")


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    middlename = StringField("Отчество", validators=[DataRequired()])
    birthday = DateField("Дата рождения", format='%d.%m.%Y', description="Введите дату в формате DD.MM.YYYY",
                         validators=[DataRequired(message="Введите правильную дату")])
    placeBirth = StringField("Место рождения", validators=[DataRequired()])
    tel = StringField("Телефон", validators=[DataRequired()])


class EditPassword(FlaskForm):
    lastPassword = PasswordField("Текущий пароль", validators=[DataRequired()])
    newPasswords = PasswordField("Новый пароль", validators=[DataRequired()])
