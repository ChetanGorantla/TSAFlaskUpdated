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

if __name__ == '__main__':
    app.run(debug = True, port = 8000)

