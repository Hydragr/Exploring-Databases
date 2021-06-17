from myproject import db

class Pilot(db.Model):

	__tablename__ = 'pilots'

	id = db.Column(db.Integer,primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	age = db.Column(db.Integer)
	rank = db.Column(db.Integer)
	company = db.relationship('Company',backref='pilot',uselist=False)

	def __init__(self,first_name,last_name,age,rank):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.rank = rank

	def __repr__(self):
		if self.company:
			return f"Pilot name is {self.first_name} {self.last_name} and company is {self.company.name}"
		else:
			return f"Pilot name is {self.first_name} {self.last_name} and has no company assigned yet."

class Company(db.Model):

    __tablename__ = 'company'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    pilot_id = db.Column(db.Integer,db.ForeignKey('pilots.id'))
    
    def __init__(self,name,pilot_id):
        self.name = name
        self.pilot_id = pilot_id
    def __repr__(self):
    	return f"Company name is {self.name}"