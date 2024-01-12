# Flask allows you to write a Python service which can serve HTTP request.
# Flask is a micro web framework for Python that allows you to easily build web applications.
from flask import Flask, request, jsonify
import util

app = Flask(__name__)


# 'get_location_names' is an endpoint.
@app.route('/get_location_names')
def get_location_names():
    # We have column.json where the locations are stored. Now we want to
    # access the locations. We can access the columns file using jsonify.
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')

    return response


# 'predict_home_price' is an endpoint.
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # Whenever we are making a HTTP call via request from
    # HTML application. We will get inputs in request.form.
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    return response


if __name__ == "__main__":
    print("Starting python flask server for Home Price Prediction...")
    app.run()