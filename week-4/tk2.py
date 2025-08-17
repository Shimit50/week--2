# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model
model_path = os.path.join('model', 'student_performance_model.joblib')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        hours = float(request.form.get('hours'))
        attendance = float(request.form.get('attendance'))
        assignments = float(request.form.get('assignments'))
        
        # Make prediction
        prediction = model.predict([[hours, attendance, assignments]])[0]
        
        return render_template('result.html', 
                             prediction=round(prediction, 2),
                             hours=hours,
                             attendance=attendance,
                             assignments=assignments)
    
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        
        hours = float(data['hours'])
        attendance = float(data['attendance'])
        assignments = float(data['assignments'])
        
        prediction = model.predict([[hours, attendance, assignments]])[0]
        
        return jsonify({
            'prediction': round(prediction, 2),
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

if __name__ == '__main__':
    app.run(debug=True)