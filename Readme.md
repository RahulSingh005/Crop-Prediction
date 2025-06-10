# Crop Prediction Model

A machine learning-powered web application that predicts the most suitable crop to grow based on soil and environmental conditions using Random Forest classification.

## 🌱 Overview

This Flask web application helps farmers and agricultural enthusiasts determine the best crop to cultivate based on key agricultural parameters. The model analyzes soil composition (NPK levels, pH) and environmental factors (temperature, humidity, rainfall) to provide accurate crop recommendations.

## ✨ Features

- **Real-time Prediction**: Get instant crop recommendations based on input parameters
- **User-friendly Interface**: Clean, responsive web interface with agricultural theming
- **Machine Learning Powered**: Uses Random Forest algorithm for accurate predictions
- **Multiple Crop Support**: Predicts from a variety of crops including rice, wheat, maize, cotton, and more
- **Input Validation**: Ensures all required parameters are provided

### 📱 Main Interface
![generated-image (3)](https://github.com/user-attachments/assets/a21e4ce8-b190-443a-88be-838d41d6ebc2)

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Pickle

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.7+
- pip (Python package manager)

## 🚀 Installation

 **Clone the repository**
     ```bash
    git clone https://github.com/RahulSingh005/Crop-Prediction.git
    ```

## 🎯 Usage
1. **Start the Flask application**
    ```bash
    python app.py
    ```
2. **Access the application**
Open your web browser and navigate to `http://localhost:5000`

3. **Make Predictions**
- Enter the required parameters:
  - **Nitrogen (N)**: Soil nitrogen content
  - **Phosphorus (P)**: Soil phosphorus content  
  - **Potassium (K)**: Soil potassium content
  - **Temperature**: Average temperature (°C)
  - **Humidity**: Relative humidity (%)
  - **pH**: Soil pH level
  - **Rainfall**: Annual rainfall (mm)
- Click "Predict" to get the recommended crop

## 📊 Dataset Information

The model is trained on agricultural data containing:
- **Features**: 7 input parameters (N, P, K, Temperature, Humidity, pH, Rainfall)
- **Target**: Crop types (21 different crops)
- **Source**: https://www.kaggle.com/code/prasadchaskar/crop-prediction-99-accuracy

### Sample Input Values:
    Nitrogen: 90
    Phosphorus: 42
    Potassium: 43
    Temperature: 20.87
    Humidity: 82.00
    pH: 6.50
    Rainfall: 202.93

## 🤖 Model Information

- **Algorithm**: Random Forest Classifier
- **Accuracy**: 99%
- **Features**: 7 input features
- **Classes**: 21 crop types
- **Training**: Trained on agricultural dataset

### Supported Crops:
'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee'

### Local Development
     python app.py
     
## 🚀 Deployment

    
