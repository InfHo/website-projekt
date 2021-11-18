# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2

from flask import Flask, render_template
from forms_hallo import RegistrationForm, LoginForm

#import random

app = Flask(__name__)

#app.config['SECRET_KEY'] = '4aee34cc1e4462c4565d5af52395119f'


posts = [
    {
        'author': 'Philipp',
        'title':'Blog Post1',
        'content':'First Post Content',
        'date_posted':"11.11.2021"
    },
        {
        'author': 'Patrick',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'Oktober, 14, 2021'
    }
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="Hallo")
"""
@app.route("/register")
def register():
    form = RegistrationForm()  
    return render_template('register.html', title="Register", form=form)
"""

"""@app.route("/login")
def register():
    form = LoginForm()  
    return render_template('login.html', title="Login", form=form)

"""

if __name__ == '__main__':
    app.run(debug=True)