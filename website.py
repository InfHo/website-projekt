# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2

from flask import Flask, render_template, url_for

import random

app = Flask(__name__)


posts = [
    {
        'author': 'test',
        'title':'Blog Post1',
        'content':'First Post Content',
        'date_posted':str(random.randint(1,10))
    },
        {
        'author': 'test2',
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

if __name__ == '__main__':
    app.run(debug=True)