from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

from forms import RegisterForm

register_blueprint = Blueprint('register', __name__, template_folder='templates')

@register_blueprint.route('/', methods=['GET', 'POST'])
def reg_bl():
	register_form = RegisterForm()

	if request.method == 'POST':
		if register_form.validate_on_submit():
			flash('OK!')
			return
		flash('NO')

	return render_template('register/register.html', register_form=register_form), 200