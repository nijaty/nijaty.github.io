from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hciunozjjcdddy:6b3e4dc05ee5c618ed4cbabc9f72b1c1f46d44562b2a8a41278aad05ffca4533@ec2-174-129-231-100.compute-1.amazonaws.com:5432/dehajp0eht1mrt?sslmode=require'
db = SQLAlchemy(app)



class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    age_ = db.Column(db.Integer)

    def __init__(self, email_, age_):
        self.email_ = email_
        self.age_ = age_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        age = request.form["age_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, age)
            db.session.add(data)
            db.session.commit()
            average_age = db.session.query(func.avg(Data.age_)).scalar()
            average_age = round(average_age, 1)
            count = db.session.query(Data.age_).count()
            send_email(email, age, average_age, count)
            return render_template("success.html")
        return render_template('index.html', text="This email has already exists")


if __name__ == '__main__':
    app.run(debug=True)
