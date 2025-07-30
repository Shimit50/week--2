from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def api_status():
    return {"message": "API is working"}, 200

if __name__ == '__main__':
    app.run(debug=True)