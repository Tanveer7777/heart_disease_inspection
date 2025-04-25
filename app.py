from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('DT_Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal']),
        ]

        input_data = np.array([features])
      
        prediction = model.predict(input_data)

        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
