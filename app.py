from flask import Flask, redirect, url_for, jsonify, request
from views import views
import requests

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(views, url_prefix="/views")

@app.route('/')
def index():
    return redirect(url_for('views.index'))

@app.route("/hospitals")
def get_hospitals():
    hospitals = find_hospitals(50)
    return jsonify(hospitals)

def get_user_location():
    ip_url = "https://api.ipify.org"
    location_url = "http://ip-api.com/json"
    ip = requests.get(ip_url).text
    print(f"IP address: {ip}")
    location = requests.get(f"{location_url}/{ip}").json()
    print(f"Location info: {location}")
    return location["lat"], location["lon"]

def find_hospitals(max_radius):
    lat, lng = get_user_location()
    location = f"{lat},{lng}"
    radius = max_radius * 1609.34  # Convert miles to meters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": "hospital",
        "key": "AIzaSyBVcFCp2zsoinAa85PBwUhYfJ2mEc7bwYU"
    }
    response = requests.get(url, params=params)
    hospitals = response.json()["results"]
    results = []
    for hospital in hospitals:
        name = hospital["name"]
        address = hospital["vicinity"]
        rating = hospital.get("rating", "N/A")
        result = {"name": name, "rating": rating, "address": address}
        results.append(result)
    return results



@app.route('/submit_symptoms', methods=['POST'])
def submit_symptom():
    integumentary = request.form['integumentary']
    digestive = request.form['digestive']
    respiratory = request.form['respiratory']
    eyes = request.form['eyes']
    muscles_input = request.form['muscles']
    temperature = request.form['temperature']
    urinary = request.form['urinary']
    emotions = request.form['emotions']
    circulatory = request.form['circulatory']
    # Do something with the selected symptom values
    return 'Selected symptoms: {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(integumentary, digestive, respiratory, eyes, muscles_input, temperature, urinary, emotions, circulatory)


symptoms = [
    "Age",
    "Polyuria",
    "Polydipsia",
    "sudden weight loss",
    "weakness",
    "Polyphagia",
    "Genital thrush",
    "visual blurring",
    "Itching",
    "Irritability",
    "delayed healing",
    "partial paresis",
    "muscle stiffness",
    "Alopecia",
    "Obesity",
]


@app.route("/submit_diabetes", methods=["POST"])
def submit():
    age = request.form.get("age-input")
    polyphagia = request.form.get("excessively-hungry")
    polydipsia = request.form.get("excessively-thirsty")
    polyuria = request.form.get("urinating-excessively")
    thrush = request.form.get("genital-thrush")
    weakness = request.form.get("weakness")
    weight = request.form.get("lost-weight")
    blurring = request.form.get("vision-blurred")
    irritability = request.form.get("irritable")
    itching = request.form.get("itchy")
    healing = request.form.get("delayed-healing")
    paresis = request.form.get("partial-paresis")
    stiffness = request.form.get("stiff-muscles")
    alopecia = request.form.get("alopecia")
    obesity = request.form.get("obese")
  
    input_arr = [
        age,
        polyuria,
        polydipsia,
        weight,
        weakness,
        polyphagia,
        thrush,
        blurring,
        itching,
        irritability,
        healing,
        paresis,
        stiffness,
        alopecia,
        obesity,
    ]

  
  # do something with the submitted form data
    return "Selected symptoms: age {}, excessively_hungry {}, urinating_excessively {}, genital_thrush {}, weakness {}, lost_weight {}, vision_blurred {}, irritable {}, itchy {}, delayed_healing {}, partial_paresis {}, stiff_muscles {}, alopecia {}, obese {}".format(age, polyphagia, polyuria, thrush, weakness, weight, blurring, irritability, itching, healing, paresis, stiffness, alopecia, obesity)


if __name__ == '__main__':
    app.run(debug = True, port = 8000)

