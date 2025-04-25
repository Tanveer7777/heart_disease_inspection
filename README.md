🫀 Heart Disease Prediction Model using Flask

This repository contains a machine learning model that predicts the risk of heart disease based on various clinical factors. The model is integrated into a web application built with Flask, allowing users to input their health data and receive instant predictions.

🔍 Overview

This project leverages a trained machine learning model (model.pkl) to predict the likelihood of heart disease based on clinical features such as:

Age, sex, chest pain type,Resting blood pressure, cholesterol levels,Fasting blood sugar, ECG results, maximum heart rate,Exercise-induced angina, oldpeak, and more.

📂 Project Structure

Heart_Disease_Inspection/ – Contains the Flask app and Python backend app.py. Main Flask application file DT-Model.pkl , Pickle file containing the trained machine learning model, templates/ – HTML templates rendered by Flask in which two html filesis there index.html – Landing page with the form to collect user input & result.html – Page displaying the heart disease prediction result and static/css/- css desings rendering by python

📊 About the Model

Model Type: Random Forest Accuracy: 97% Dataset: www.keggle.com

✨ Features: Interactive user interface for easy data entry Displays real-time prediction results Simple and responsive design

🔧 Technologies Used:

Flask: Web framework for building the app Scikit-learn: For machine learning model training and evaluation HTML/CSS: For the frontend Pickle: For model serialization

📁 Additional Notes:

The app is designed to be easily deployable and user-friendly, with input validation and error handling. You can modify or retrain the model with your own dataset if needed.
