#class Post:
#	def __init__(self, title, author, content, model):
#		self.tittle = title 
#		self.author = author
#		self.content = content
#		self.modle = model



from app import db 

class User(db.Model):
	id =db.Column(db.Integer, primary_key = True)
	firstname =db.Column(db.String(64))
	lastname =db.Column(db.String(64))
	username =db.Column(db.String(120), unique = True)
#	posts =db.relationship('Post', backref = 'author')


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	content =db.Column(db.Text)
	author =db.Column(db.Integer, db.ForeignKey('user.id'))

#from models import User, Post 

#casidy = User(1, '', '' ,'')

#post1 = Post('', '',1)

#post2 = Post('', '',1)

#class User(db.Model):
#	firstname =db.Column(db.String(70))
#	lastname =db.Column(db.String(70))
	#username = db.Column(db.String(180), unique = True)
	#author_id =db.Column(db.Integer, db.ForeignKey('user.id'))





















#print casidy.posts
