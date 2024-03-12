from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import pandas as pd
import os

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'test'
jwt = JWTManager(app)

# Load data from CSV
path = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv('{}/asset/openblocklabs-dataset.csv'.format(path))

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # TODO: save user and password in database
    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/points', methods=['GET'])
@jwt_required()
def get_points():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    wallet_address = request.args.get('wallet_address')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    # Ensure all parameters are provided
    if not (wallet_address and from_date and to_date):
        return jsonify({"error": "Missing parameters"}), 400

    # Filter the data based on the input criteria
    filtered_data = data[(data['wallet_address'] == wallet_address) &
                         (pd.to_datetime(data['date']) >= from_date) &
                         (pd.to_datetime(data['date']) <= to_date)]

    # Calculate the sum of point values
    total_points = filtered_data['point_value'].sum()

    # Response
    return jsonify({
        "wallet_address": wallet_address,
        "from_date": from_date,
        "to_date": to_date,
        "total_points": total_points
    })


if __name__ == '__main__':
    app.run(debug=True)
