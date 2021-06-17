from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Company
from myproject.company.forms import AddForm

company_blueprints=Blueprint('company',__name__,template_folder='templates/company')

@company_blueprints.route('/add',methods=['GET', 'POST'])
def add():
	form=AddForm()
	if form.validate_on_submit():
		name=form.name.data
		id=form.id.data
		new_company=Company(name,id)
		db.session.add(new_company)
		db.session.commit()
		return redirect(url_for('pilots.list'))	
	return render_template('add_company.html',form=form)

@company_blueprints.route('/list')
def company_list():
	companies= Company.query.all()
	return render_template('company_list.html',companies=companies)


