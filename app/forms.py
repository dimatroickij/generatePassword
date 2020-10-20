import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, ValidationError


def checkPassword(form, field):
    if len(field.data) > 6:
        raise ValidationError('Длина пароля не должна превышать 6 символов')
    if re.match('[a-z]+', field.data) is None or re.match('[a-z]+', field.data).group(0) != field.data:
        raise ValidationError('Пароль должен состоять только из латиницы (строчные буквы)')


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить")


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[checkPassword, DataRequired()],
                             description='Требования к паролю: длина 6 символов, используемые символы: латиница'
                                         ' (строчные буквы)')
    surname = StringField("Фамилия", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    middlename = StringField("Отчество", validators=[DataRequired()])
    birthday = DateField("Дата рождения", format='%d.%m.%Y', description="Введите дату в формате DD.MM.YYYY",
                         validators=[DataRequired(message="Введите правильную дату")])
    placeBirth = StringField("Место рождения", validators=[DataRequired()])
    tel = StringField("Телефон", validators=[DataRequired()])


class EditPassword(FlaskForm):
    lastPassword = PasswordField("Текущий пароль", validators=[DataRequired()])
    newPassword = PasswordField("Новый пароль", validators=[checkPassword, DataRequired()])
    newPasswordRepeat = PasswordField("Повторите новый пароль", validators=[DataRequired()])
