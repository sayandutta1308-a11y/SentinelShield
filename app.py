from flask import Flask, render_template, request
from database import db, AttackLog
from detector import detect_attack


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///attacks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def home():

    scan_result = None

    if request.method == "POST":

        user_request = request.form["payload"]

        detected_attack = detect_attack(user_request)

        if detected_attack:

            new_log = AttackLog(
                ip_address=request.remote_addr,
                attack_type=detected_attack,
                payload=user_request
            )

            db.session.add(new_log)
            db.session.commit()

            scan_result = {
                "status": "MALICIOUS",
                "attack": detected_attack,
                "risk": "HIGH",
                "message": "Threat detected. Request blocked."
            }

        else:

            scan_result = {
                "status": "SAFE",
                "attack": "None",
                "risk": "LOW",
                "message": "No suspicious activity found."
            }


    return render_template(
        "index.html",
        result=scan_result
    )


@app.route("/dashboard")
def dashboard():

    attack_logs = AttackLog.query.all()

    return render_template(
        "dashboard.html",
        logs=attack_logs
    )


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)