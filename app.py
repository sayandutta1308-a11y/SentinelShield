from flask import Flask, render_template, request
from database import db, AttackLog
from detector import detect_attack


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attacks.db'


db.init_app(app)


with app.app_context():
    db.create_all()



@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route(
    "/scan",
    methods=["POST"]
)
def scan():

    data = request.form[
        "payload"
    ]

    result = detect_attack(
        data
    )


    if result != "Safe":

        attack = AttackLog(

            ip_address=
            request.remote_addr,

            attack_type=result,

            payload=data

        )


        db.session.add(
            attack
        )

        db.session.commit()


    return render_template(
        "index.html",
        result=result
    )



@app.route("/dashboard")
def dashboard():

    logs = AttackLog.query.all()

    return render_template(
        "dashboard.html",
        logs=logs
    )



if __name__ == "__main__":

    app.run(
        debug=True
    )