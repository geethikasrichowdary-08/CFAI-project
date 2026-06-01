from flask import Flask, render_template, request
import heapq
import webbrowser
from threading import Timer

app = Flask(__name__)

# CO5 - Bayesian Risk Prediction
def bayes_risk(severity):
    probabilities = {
        "Low": 0.35,
        "Medium": 0.65,
        "High": 0.90
    }
    return probabilities.get(severity, 0.50)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan", methods=["POST"])
def plan():

    village = request.form["village"]
    disaster = request.form["disaster"]
    affected = int(request.form["affected"])
    injured = int(request.form["injured"])
    severity = request.form["severity"]

    # CO1 - Resource Estimation Rules

    food = affected * 3
    water = affected * 5
    medicine = max(1, injured // 5)

    shelters = max(1, affected // 50)
    rescue = max(1, affected // 500)

    # CO5 - Bayesian Risk Prediction

    risk = round(bayes_risk(severity) * 100, 2)

    # CO1 - Priority Queue

    pq = []

    priority_map = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    heapq.heappush(
        pq,
        (priority_map[severity], village)
    )

    priority_level = severity.upper()

    # CO2 - Route Planning Concept

    route = f"HQ → Zone B → Relief Camp → {village}"

    return render_template(
        "result.html",

        village=village,
        disaster=disaster,
        severity=severity,

        food=food,
        water=water,
        medicine=medicine,

        shelters=shelters,
        rescue=rescue,

        risk=risk,
        route=route,

        priority_level=priority_level
    )


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)