from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()