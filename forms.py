from wtforms import Form 
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField 
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='long de campo 4 min and 5 max')
    ])
    nombre = StringField('Nombre', [
    validators.DataRequired(message="El campo es requerido")
    ])
    
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno') 
    email = EmailField('Correo')