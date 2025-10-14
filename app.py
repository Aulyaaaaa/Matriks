from flask import Flask, render_template, request
import pandas as pd
from operations.linier_regression import linear_regression

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Baca dataset
    data = pd.read_csv('datasetemas.csv')

    # Jalankan regresi linear
    hasil, plot_path = linear_regression(data)

    # Kirim hasil ke template
    return render_template('index.html', hasil=hasil, plot_url=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
