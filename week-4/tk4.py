# Student Performance Prediction App

A Flask web application that predicts student performance based on:
- Hours studied
- Attendance percentage
- Assignments submitted

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the app: `python app.py`
2. Access the web interface at `http://localhost:5000`
3. Alternatively, send POST requests to `/api/predict` with JSON data

## API Example

```json
{
    "hours": 15,
    "attendance": 90,
    "assignments": 7
}