from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# -----------------------------
# DATA STORAGE
# -----------------------------

volunteers = []

donations = []

missing_persons = []

shelters = [
    {
        "name": "Central Shelter",
        "capacity": 500,
        "food": 300,
        "water": 400
    },
    {
        "name": "Community Hall",
        "capacity": 250,
        "food": 150,
        "water": 200
    }
]

hospitals = [
    {
        "name": "City Hospital",
        "beds": 120,
        "icu": 25,
        "ambulances": 10
    },
    {
        "name": "District Hospital",
        "beds": 80,
        "icu": 15,
        "ambulances": 5
    }
]

# -----------------------------
# AI MODULES
# -----------------------------

def flood_prediction(rainfall):

    if rainfall > 100:
        return "High Flood Risk"

    elif rainfall > 60:
        return "Moderate Flood Risk"

    return "Low Flood Risk"


def assign_volunteer(skill):

    for v in volunteers:

        if skill.lower() in v["skill"].lower():

            return v["name"]

    return "No Suitable Volunteer Found"


# -----------------------------
# ROUTES
# -----------------------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/government")
def government():

    return render_template(
        "government.html",
        volunteers=volunteers,
        donations=donations,
        missing_persons=missing_persons,
        shelters=shelters,
        hospitals=hospitals
    )


# -----------------------------
# VOLUNTEERS
# -----------------------------

@app.route("/volunteer",
           methods=["GET", "POST"])
def volunteer():

    if request.method == "POST":

        volunteers.append(
            {
                "name": request.form["name"],
                "skill": request.form["skill"],
                "availability":
                request.form["availability"]
            }
        )

        return redirect("/volunteer")

    return render_template(
        "volunteer.html",
        volunteers=volunteers
    )


# -----------------------------
# MISSING PERSONS
# -----------------------------

@app.route("/missing",
           methods=["GET", "POST"])
def missing():

    if request.method == "POST":

        missing_persons.append(
            {
                "name": request.form["name"],
                "age": request.form["age"],
                "description":
                request.form["description"],
                "status": "Missing"
            }
        )

        return redirect("/missing")

    return render_template(
        "missing.html",
        persons=missing_persons
    )


# -----------------------------
# DONATIONS
# -----------------------------

@app.route("/donation",
           methods=["GET", "POST"])
def donation():

    if request.method == "POST":

        donations.append(
            {
                "donor":
                request.form["donor"],

                "item":
                request.form["item"],

                "quantity":
                request.form["quantity"],

                "status":
                "Received"
            }
        )

        return redirect("/donation")

    return render_template(
        "donation.html",
        donations=donations
    )


# -----------------------------
# SHELTERS
# -----------------------------

@app.route("/shelters")
def shelters_page():

    return render_template(
        "shelters.html",
        shelters=shelters
    )


# -----------------------------
# HOSPITALS
# -----------------------------

@app.route("/hospitals")
def hospitals_page():

    return render_template(
        "hospitals.html",
        hospitals=hospitals
    )


# -----------------------------
# AI RISK PREDICTION
# -----------------------------

@app.route("/risk")
def risk():

    prediction = flood_prediction(120)

    return render_template(
        "risk.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)