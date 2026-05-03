from flask import Flask, render_template, request, jsonify, redirect, url_for
import re

app = Flask(__name__)

doctors = {
1:{
"id":1,
"name":"Sarah Patel, MD",
"specialty":"Neurologist",
"conditions":"Migraines, Epilepsy",
"experience":"12",
"education":"John Hopkins University School of Medicine",
"insurance":"Aetna, Blue Cross",
"location":"622 W 168th St, New York, NY",
"phone":"212-555-4412",
"image":"https://images.unsplash.com/photo-1559839734-2b71ea197ec2"
},
2:{
"id":2,
"name":"Michael Chen, MD",
"specialty":"Cardiologist",
"conditions":"Heart Disease, Hypertension",
"experience":"15",
"education":"Stanford School of Medicine",
"insurance":"Cigna, Aetna",
"location":"New York, NY",
"phone":"212-555-3321",
"image":"https://images.unsplash.com/photo-1622253692010-333f2da6031d"
},
3:{
"id":3,
"name":"Laura Gomez, MD",
"specialty":"Dermatologist",
"conditions":"Acne, Eczema",
"experience":"9",
"education":"UCLA School of Medicine",
"insurance":"Blue Cross",
"location":"New York, NY",
"phone":"212-555-9921",
"image":"https://images.unsplash.com/photo-1594824476967-48c8b964273f"
},
4:{
"id":4,
"name":"Emily Rogers, MD",
"specialty":"Neurologist",
"conditions":"Multiple Sclerosis, Parkinson’s Disease",
"experience":"14",
"education":"Columbia University Vagelos College of Physicians and Surgeons",
"insurance":"Aetna, Cigna",
"location":"New York, NY",
"phone":"212-555-7734",
"image":"https://images.unsplash.com/photo-1607746882042-944635dfe10e"
},

5:{
"id":5,
"name":"David Stein, MD",
"specialty":"Cardiologist",
"conditions":"Arrhythmia, Heart Failure",
"experience":"18",
"education":"Mount Sinai Icahn School of Medicine",
"insurance":"Blue Cross, UnitedHealthcare",
"location":"New York, NY",
"phone":"212-555-8843",
"image":"https://images.unsplash.com/photo-1582750433449-648ed127bb54"
},

6:{
"id":6,
"name":"Robert Williams, MD",
"specialty":"Cardiologist",
"conditions":"Coronary Artery Disease, Hypertension",
"experience":"20",
"education":"Harvard Medical School",
"insurance":"Aetna, Blue Cross",
"location":"Manhattan, NY",
"phone":"212-555-9923",
"image":"https://images.unsplash.com/photo-1612349317150-e413f6a5b16d"
},

7:{
"id":7,
"name":"Daniel Park, MD",
"specialty":"Neurologist",
"conditions":"Stroke, Seizure Disorders",
"experience":"13",
"education":"Johns Hopkins University School of Medicine",
"insurance":"UnitedHealthcare, Aetna",
"location":"New York, NY",
"phone":"212-555-4431",
"image":"https://images.unsplash.com/photo-1537368910025-700350fe46c7"
}
}

next_id = 8

@app.route("/")
def home():
    first_three = list(doctors.values())[:3]
    return render_template("home.html", doctors=first_three)


@app.route("/view/<int:id>")
def view(id):
    return render_template("view.html", doctor=doctors[id])


@app.route("/search")
def search():

    query = request.args.get("q", "")
    results = []

    pattern = re.compile(re.escape(query), re.IGNORECASE)

    for doc in doctors.values():

        if (query.lower() in doc["name"].lower() or
            query.lower() in doc["specialty"].lower() or
            query.lower() in doc["conditions"].lower()):

            highlighted = doc.copy()

            for field in ["name", "specialty", "conditions"]:
                highlighted[field] = pattern.sub(
                    lambda m: f"<span class='highlight'>{m.group()}</span>",
                    doc[field]
                )

            results.append(highlighted)

    return render_template(
        "search.html",
        results=results,
        query=query,
        count=len(results)
    )

@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/add_item", methods=["POST"])
def add_item():

    global next_id
    data = request.json

    data["id"] = next_id
    doctors[next_id] = data

    next_id += 1

    return jsonify({"id":data["id"]})


@app.route("/edit/<int:id>")
def edit(id):
    return render_template("edit.html", doctor=doctors[id])


@app.route("/update_item", methods=["POST"])
def update_item():

    data=request.json
    id=int(data["id"])

    doctors[id]=data

    return jsonify({"success":True})


if __name__ == "__main__":
    app.run(debug=True)
