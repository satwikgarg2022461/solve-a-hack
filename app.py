from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)

# data1= pd.read_csv('./train_V2.csv')

# print(data1.info())

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Example route for handling a form submission or request with JSON
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and file.filename.endswith('.csv'):
        # Save the file to the upload folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)
        
        # Print or process the dataframe (for demonstration, printing first few rows)
        return df.head(2).to_html()  # Re

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
