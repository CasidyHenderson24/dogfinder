# forms.py

from flask.ext.wtf import Form
from wtfforms import Textfield
from wtfforms.validators import Required 

class NewUserForm(Form):
	firstname = Textfield('firstname')
	lastname = Textfield('lastname')
	username = Textfield('username', validators = [Required()])
	