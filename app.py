from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import email_service

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'ENTER YOUR POSGRESQL TABLE ADDRESS'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]

        if(db.session.query(Data).filter(Data.email == email).count() == 0):
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()

            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()
            email_service.send_email(email, height, average_height, count)

            return render_template("success.html")

        return render_template("index.html", text="Seems like we've got something from that email already.")


if __name__ == '__main__':
    app.debug = True
    app.run()
