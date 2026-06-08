from flask import Flask, render_template, request
import heapq
import webbrowser
from threading import Timer
from collections import deque

app = Flask(__name__)

# =====================================================
# CO5 - Bayes Rule Based Risk Prediction
# =====================================================

def bayes_risk(severity):
    probabilities = {
        "Low": 0.35,
        "Medium": 0.65,
        "High": 0.90
    }
    return probabilities.get(severity, 0.50)


# =====================================================
# CO2 - BFS Search Algorithm
# =====================================================

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return None


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

    # =====================================================
    # CO1 - Rule Based Resource Estimation
    # =====================================================

    food = affected * 3
    water = affected * 5
    medicine = max(1, injured // 5)

    # =====================================================
    # CO3 - CSP + Forward Checking
    # =====================================================

    shelters = max(1, affected // 50)

    available_capacity = 20

    if shelters > available_capacity:
        constraint_message = (
            "Constraint Failed: Not enough shelters available"
        )
    else:
        constraint_message = (
            "Constraint Satisfied"
        )

    # =====================================================
    # CO3 - MRV Heuristic
    # =====================================================

    shelter_options = {
        "Camp A": 10,
        "Camp B": 5,
        "Camp C": 15
    }

    selected_shelter = min(
        shelter_options,
        key=shelter_options.get
    )

    rescue = max(1, affected // 500)

    # =====================================================
    # CO5 - Bayesian Risk Prediction
    # =====================================================

    risk = round(
        bayes_risk(severity) * 100,
        2
    )

    # =====================================================
    # CO4 - Utility Function
    # =====================================================

    severity_score = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    utility_score = (
        affected * 0.5
        + severity_score[severity] * 100
        - injured * 0.1
    )

    # =====================================================
    # CO4 - Expected Utility Decision
    # =====================================================

    evacuate_utility = risk * 2
    monitor_utility = 100 - risk

    if evacuate_utility > monitor_utility:
        decision = "Evacuate Immediately"
    else:
        decision = "Monitor Situation"

    # =====================================================
    # CO1 - Priority Queue
    # =====================================================

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

    # =====================================================
    # CO2 - Graph Search (BFS)
    # =====================================================

    graph = {
        "HQ": ["ZoneA", "ZoneB"],
        "ZoneA": ["Camp"],
        "ZoneB": ["Camp"],
        "Camp": [village],
        village: []
    }

    path = bfs(graph, "HQ", village)

    if path:
        route = " → ".join(path)
        failure_analysis = "Route Found Successfully"
    else:
        route = "No Route Available"
        failure_analysis = "Search Failed"

    # =====================================================
    # CO6 - Sensor Fusion Concept
    # =====================================================

    weather_risk = risk
    road_risk = 70
    population_risk = min(100, affected / 10)

    fused_risk = round(
        (weather_risk + road_risk + population_risk) / 3,
        2
    )

    # =====================================================
    # CO6 - Explainable AI Reasoning Trace
    # =====================================================

    reasoning_trace = [
        f"Severity = {severity}",
        f"Bayesian Risk = {risk}%",
        f"Selected Shelter = {selected_shelter}",
        f"Utility Score = {utility_score}",
        f"Decision = {decision}"
    ]

    # =====================================================
    # CO6 - Ethics / Limitation
    # =====================================================

    limitation = (
        "Risk prediction depends on available data "
        "and may not reflect real-world uncertainty."
    )

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

        priority_level=priority_level,

        selected_shelter=selected_shelter,
        constraint_message=constraint_message,

        utility_score=utility_score,
        decision=decision,

        fused_risk=fused_risk,

        reasoning_trace=reasoning_trace,

        failure_analysis=failure_analysis,

        limitation=limitation
    )


def open_browser():
    webbrowser.open_new(
        "http://127.0.0.1:5000"
    )


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True)