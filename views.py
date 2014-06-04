# -*- coding: utf-8 -*-

#from app import app, models, db 
#from flask import render_template 
#from models import Post, User


#.route('/')
#	some_post = Post("Not in the mood", "Casidy", "get out my face!")
#	some_other_post = Post("bye bye bye", "Casidy", "lil gurl dont get knocked out!")
	
#	return render_template("book.html",posts = [some_post, some_other_post])

#	@app.route(‘/index’)
#def index():
#	users = User.query.all()
 #  	return render_template(‘index.html’, users = users)	


from app import app, db 
components from other files
from flask import Flask, render_template,
	redirect
from models import Post, User
from forms import NewUserForm

@app.route('/')
def index():
 	all_user = User.query.all()
 	posts = Post.query.all()
 	return render_template("index.html", users = all_user, posts = posts)

 @app.route('/add_user', methods = ['GET', 'POST'])
 def add_user():
 	form = NewUserForm()
 	if form.validate_on_submit():
 		user = User()
 		form.populate_obj(user)
 		db.session.add(user)
 		db.session.commit()
 		return redirect('/')
 		return render_template("add_user.html", form =form) 