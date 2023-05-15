from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_locations', methods=['GET'])
def get_locations():
    response = jsonify({
        'locations' : util.get_locations()
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    bedroom = int(request.form['bhk'])
    bathrooms = int(request.form['bath'])
    area = float(request.form['total_sqft'])
    floor_number = int(request.form['floor_no'])
    locations = request.form['location']
    furniture = request.form['type']
    age = int(request.form['age'])

    if furniture == 'Furnished':
        Furnished = 1
        Semifurnished = 0
    elif furniture == 'Semifurnished':
        Furnished = 0
        Semifurnished = 1
    else:
        Furnished = 0
        Semifurnished = 0

    c0_to_1_Year_Old = 0
    c1_to_5_Year_Old = 0
    c10_Year_Old = 0

    if age == 1:
        c0_to_1_Year_Old = 1
    elif age == 2:
        c1_to_5_Year_Old = 1
    elif age == 4:
        c10_Year_Old = 1
    

    response = jsonify({
        'estimated_price': util.predict_price(bedroom,bathrooms,area,floor_number,Furnished,Semifurnished,c0_to_1_Year_Old, c1_to_5_Year_Old, c10_Year_Old, locations)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)