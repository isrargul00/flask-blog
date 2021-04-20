from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text())
    date = db.Column(db.DateTime)

    def __str__(self):
        return f"post {self.content}"

@app.route('/')
def home():
    post = Post.query.all()
    return render_template('home.html',post=post)

if __name__ == '__main__':
    app.debug = True
    app.run()