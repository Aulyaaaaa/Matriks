import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
from operations.linier_regression import regresi_emas

app = Flask(__name__)

@app.route('/')
def home():
    result = regresi_emas("datasetemas.csv", days_ahead=7)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
