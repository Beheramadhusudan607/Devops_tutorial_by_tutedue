import json
from flask import Flask, request, jsonify
from flask import render_template, request  
app = Flask(__name__)

API_DATA = [
    {
        "id": 1,
        "Task":"setup project environment",
        "Status":"completed"
    },
    {
        "id": 2,
        "Task":"create Flask app",
        "Status":"completed"
    },
    {
        "id": 3,
        "Task":"define API routes",
        "Status":"completed"        
    },
    {
        "id": 4,
        "Task":"add database integration",
        "Status":"pending"
    }
]
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('data')
    # You can process 'data' here if needed
    return render_template('success.html', data=data)


@app.route('/')
def home():
    return "Welcome to the Flask API!"
@app.route('/api/tasks', methods=['GET'])
def get_api_data():
    return jsonify(API_DATA)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)