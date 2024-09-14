from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)

# data1= pd.read_csv('./train_V2.csv')

# print(data1.info())



# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Example route for handling a form submission or request with JSON
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get JSON data from POST request
    if data:
        # Process the data as needed
        result = {"message": "Data received", "data": data}
        return jsonify(result), 200
    else:
        return jsonify({"error": "No data received"}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
