from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import algo
from datetime import datetime
import time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class genPrime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    range = db.Column(db.Text(), nullable=False)
    count = db.Column(db.Integer)
    elapsedTime = db.Column(db.Integer)
    algoUsed = db.Column(db.Text())
    dateGenerated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return self.id


@app.route("/")
def index():
    return "hello world"


@app.route("/algov1", methods=["POST"])
def handleAlgov1():

    response = {"count": 0, "generated": [], "errors": "", "elapsedTime": 0}

    upper = request.get_json()["a"]
    lower = request.get_json()["b"]

    try:
        if upper and lower:
            start = time.time()
            data = algo.algov1(upper, lower)
            end = time.time()
            elapsedTime = end - start

            response["count"] = len(data)
            response["generated"] = data
            response["elapsedTime"] = str(elapsedTime) + "s"
            response["errors"] = "None"

            newTask = genPrime(
                range=f"{upper}-{lower}",
                count=len(data),
                elapsedTime=elapsedTime,
                algoUsed="algov1",
            )

            db.session.add(newTask)
            db.session.commit()
        return response
    except Exception as e:
        response["errors"] = str(e)
        return response


@app.route("/algov2", methods=["POST"])
def handleAlgov2():

    response = {"count": 0, "generated": [], "errors": "", "elapsedTime": 0}

    upper = request.get_json()["a"]
    lower = request.get_json()["b"]

    try:
        if upper and lower:
            start = time.time()
            data = algo.algov2(upper, lower)
            end = time.time()
            elapsedTime = end - start

            response["count"] = len(data)
            response["generated"] = data
            response["elapsedTime"] = str(elapsedTime) + "s"
            response["errors"] = "None"

            newTask = genPrime(
                range=f"{upper}-{lower}",
                count=len(data),
                elapsedTime=elapsedTime,
                algoUsed="algov2",
            )

            db.session.add(newTask)
            db.session.commit()
        return response
    except Exception as e:
        response["errors"] = str(e)
        return response


@app.route("/algov3", methods=["POST"])
def handleAlgov3():

    response = {"count": 0, "generated": [], "errors": "", "elapsedTime": 0}

    upper = request.get_json()["a"]
    lower = request.get_json()["b"]

    try:
        if upper and lower:
            start = time.time()
            data = algo.algov3(upper, lower)
            end = time.time()
            elapsedTime = end - start

            response["count"] = len(data)
            response["generated"] = data
            response["elapsedTime"] = str(elapsedTime) + "s"
            response["errors"] = "None"

            newTask = genPrime(
                range=f"{upper}-{lower}",
                count=len(data),
                elapsedTime=elapsedTime,
                algoUsed="algov3",
            )

            db.session.add(newTask)
            db.session.commit()
        return response
    except Exception as e:
        response["errors"] = str(e)
        return response


if __name__ == "__main__":
    app.run(debug=True)
