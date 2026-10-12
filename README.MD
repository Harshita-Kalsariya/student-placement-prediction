# 🎓 Student Placement Prediction

## Live Demo

Open Student Placement Prediction :->  https://student-placement-prediction-7uni.onrender.com

An AI & Machine Learning project that predicts whether a student is likely to get placed based on their academic and skill-related information.

## 🚀 Features

* Student details input through a web interface
* Placement prediction using Machine Learning
* Random Forest classification model
* Data preprocessing and feature scaling
* Flask backend
* HTML, CSS & JavaScript frontend
* Prediction result: **Placed / Not Placed**

## 📊 Input Features

The model uses student information such as:

* Student ID
* Gender
* Age
* Degree
* Branch
* CGPA
* Backlogs
* Internships
* Certifications
* Coding Skills
* Communication Skills
* Aptitude Score
* Projects
* Company Type

> `placed` is the target variable predicted by the model. `package_lpa` is not required as an input because it is known only after placement.

## 🤖 Machine Learning

**Algorithm:** Random Forest Classifier

**Target:** `placed`

The trained model and preprocessing pipeline are saved inside the `models/` folder.

```text
models/
├── rf_model.pkl
└── scaler_pipeline.pkl
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Flask-CORS
* HTML
* CSS
* JavaScript
* Joblib

## 📁 Project Structure

```text
Student-Placement-Prediction/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── Indian_Student_Placement_Dataset_2025.csv
│
├── models/
│   ├── rf_model.pkl
│   └── scaler_pipeline.pkl
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Student-Placement-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask application

```bash
python backend/app.py
```

Then open the URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## 🎯 Prediction

Enter the student's details and submit the form.

The system processes the input using the trained ML pipeline and returns:

```text
Placement Prediction: Placed
```

or

```text
Placement Prediction: Not Placed
```

## 📌 Project Goal

The goal of this project is to demonstrate how Machine Learning can be integrated with a web application to predict student placement outcomes from academic, skill, and internship-related information.

## 👩‍💻 Author

**Harshita**

Built as an AI & Machine Learning project for learning and portfolio development.
