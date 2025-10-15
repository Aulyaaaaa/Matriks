import sys
import os
from flask import Flask, render_template

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from operations.linier_regression import regresi_emas

app = Flask(__name__)

@app.route('/')
def home():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'datasetemas.csv')
    result = regresi_emas(csv_path, days_ahead=7)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
