


((((# Guide for activating virtual enviroments, python:))))

virtualenv and pip_test_env
. pip_test_env/bin/activate
pip_test_env\Scripts\activate.bat





((((# Guide for deactivating virtual enviroments, python:))))

deactivate



((((# Guide for creating a new virtual enviroment and installing flask on it))))

sudo easy_install virtualenv or sudo pip install virtualenv
sudo apt-get install python-virtualenv
mkdir myproject
cd myproject
virtualenv venv
New python executable in venv/bin/python
you should get something like this: Installing distribute............done.
. venv/bin/activate or venv\scripts\activate
pip install Flask
sudo pip install Flask
this command is used to install (pip) > easy_install pip



((((#Guide for launching flask app on my local computer))))

you should already have code for the app already existing and must be stable ex:

"from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()"
when you run the command in the terminal you should get something like this:
$ python hello.py
 * Running on http://127.0.0.1:5000/
 
 
 
 So what did that code do?

First we imported the Flask class. An instance of this class will be our WSGI application.
Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.
We then use the route() decorator to tell Flask what URL should trigger our function.
The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
Finally we use the run() function to run the local server with our application. The if __name__ == '__main__': makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module.
To stop the server, hit control-C.

Externally Visible Server
If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have debug disabled or trust the users on your network, you can make the server publicly available simply by changing the call of the run() method to look like this:

app.run(host='0.0.0.0')
This tells your operating system to listen on all public IPs.
Debug Mode
The run() method is nice to start a local development server, but you would have to restart it manually after each change to your code. That is not very nice and Flask can do better. If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

There are two ways to enable debugging. Either set that flag on the application object:

app.debug = True
app.run()
Or pass it as a parameter to run:

app.run(debug=True)
Both methods have the exact same effect.

Attention
Even though the interactive debugger does not work in forking environments (which makes it nearly impossible to use on production servers), it still allows the execution of arbitrary code. This makes it a major security risk and therefore it must never be used on production machines.
Screenshot of the debugger in action:

screenshot of debugger in action
Have another debugger in mind? See Working with Debuggers.

Routing
Modern web applications have beautiful URLs. This helps people remember the URLs, which is especially handy for applications that are used from mobile devices with slower network connections. If the user can directly go to the desired page without having to hit the index page it is more likely they will like the page and come back next time.

As you have seen above, the route() decorator is used to bind a function to a URL. Here are some basic examples:

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
But there is more to it! You can make certain parts of the URL dynamic and attach multiple rules to a function.

Variable Rules
To add variable parts to a URL you can mark these special sections as <variable_name>. Such a part is then passed as a keyword argument to your function. Optionally a converter can be used by specifying a rule with <converter:variable_name>. Here are some nice examples:

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
The following converters exist:

int	accepts integers
float	like int but for floating point values
path	like the default but also accepts slashes
Unique URLs / Redirection Behavior
Flask’s URL rules are based on Werkzeug’s routing module. The idea behind that module is to ensure beautiful and unique URLs based on precedents laid down by Apache and earlier HTTP servers.

Take these two rules:

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
Though they look rather similar, they differ in their use of the trailing slash in the URL definition. In the first case, the canonical URL for the projects endpoint has a trailing slash. In that sense, it is similar to a folder on a file system. Accessing it without a trailing slash will cause Flask to redirect to the canonical URL with the trailing slash.

In the second case, however, the URL is defined without a trailing slash, rather like the pathname of a file on UNIX-like systems. Accessing the URL with a trailing slash will produce a 404 “Not Found” error.

This behavior allows relative URLs to continue working even if the trailing slash is omitted, consistent with how Apache and other servers work. Also, the URLs will stay unique, which helps search engines avoid indexing the same page twice.
URL Building
If it can match URLs, can Flask also generate them? Of course it can. To build a URL to a specific function you can use the url_for() function. It accepts the name of the function as first argument and a number of keyword arguments, each corresponding to the variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters. Here are some examples:

>>> from flask import Flask, url_for
>>> app = Flask(__name__)
>>> @app.route('/')
... def index(): pass
...
>>> @app.route('/login')
... def login(): pass
...
>>> @app.route('/user/<username>')
... def profile(username): pass
...
>>> with app.test_request_context():
...  print url_for('index')
...  print url_for('login')
...  print url_for('login', next='/')
...  print url_for('profile', username='John Doe')
...
/
/login
/login?next=/
/user/John%20Doe
If GET is present, HEAD will be added automatically for you. You don’t have to deal with that. It will also make sure that HEAD requests are handled as the HTTP RFC (the document describing the HTTP protocol) demands, so you can completely ignore that part of the HTTP specification. Likewise, as of Flask 0.6, OPTIONS is implemented for you automatically as well.


Static Files
Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just create a folder called static in your package or next to your module and it will be available at /static on the application.

To generate URLs for static files, use the special 'static' endpoint name:

url_for('static', filename='style.css')
The file has to be stored on the filesystem as static/style.css.

Rendering Templates
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine for you automatically.

To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

