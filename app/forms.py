from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить")


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(max=6)], description='Требования к паролю: длина 6 символов,'
                                                                                ' используемые символы: латиница '
                                                                                '(строчные буквы)')
    surname = StringField("Фамилия", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    middlename = StringField("Отчество", validators=[DataRequired()])
    birthday = DateField("Дата рождения", format='%d.%m.%Y', description="Введите дату в формате DD.MM.YYYY",
                         validators=[DataRequired(message="Введите правильную дату")])
    placeBirth = StringField("Место рождения", validators=[DataRequired()])
    tel = StringField("Телефон", validators=[DataRequired()])


class EditPassword(FlaskForm):
    lastPassword = PasswordField("Текущий пароль", validators=[DataRequired()])
    newPassword = PasswordField("Новый пароль", validators=[DataRequired()])
    newPasswordRepeat = PasswordField("Новый пароль", validators=[DataRequired()])
