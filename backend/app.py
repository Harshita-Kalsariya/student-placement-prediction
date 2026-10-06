from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib
import os


# --------------------------------------------------
# Flask App
# --------------------------------------------------=

app = Flask(__name__)


# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "frontend"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "rf_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "scaler_pipeline.pkl"
)


# --------------------------------------------------
# Check Files
# --------------------------------------------------

print("Model path:")
print(MODEL_PATH)

print("Scaler path:")
print(SCALER_PATH)

print("Model exists:",
      os.path.exists(MODEL_PATH))

print("Scaler exists:",
      os.path.exists(SCALER_PATH))


# --------------------------------------------------
# Load Model and Preprocessor
# --------------------------------------------------

try:

    rf_model = joblib.load(
        MODEL_PATH
    )

    scaler_pipeline = joblib.load(
        SCALER_PATH
    )

    print("Random Forest model loaded successfully!")
    print("Scaler pipeline loaded successfully!")


except Exception as e:

    print("Error loading model:")
    print(e)

    rf_model = None
    scaler_pipeline = None


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def home():

    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


# --------------------------------------------------
# Frontend Files
# --------------------------------------------------

@app.route("/<path:filename>")
def frontend_files(filename):

    return send_from_directory(
        FRONTEND_DIR,
        filename
    )


# --------------------------------------------------
# Prediction API
# --------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        if rf_model is None:

            return jsonify({
                "success": False,
                "error": "Random Forest model could not be loaded."
            })


        if scaler_pipeline is None:

            return jsonify({
                "success": False,
                "error": "Scaler pipeline could not be loaded."
            })


        # --------------------------------------------------
        # Get Data
        # --------------------------------------------------

        data = request.get_json()

        print("\nReceived Data:")
        print(data)


        # --------------------------------------------------
        # Create Input DataFrame
        # --------------------------------------------------

        input_data = {

            "gender": data["gender"],

            "age": float(data["age"]),

            "degree": data["degree"],

            "branch": data["branch"],

            "cgpa": float(data["cgpa"]),

            "backlogs": int(data["backlogs"]),

            "internships": int(data["internships"]),

            "certifications": int(
                data["certifications"]
            ),

            "coding_skills": float(
                data["coding_skills"]
            ),

            "communication_skills": float(
                data["communication_skills"]
            ),

            "aptitude_score": float(
                data["aptitude_score"]
            ),

            "projects": int(
                data["projects"]
            )
        }


        df = pd.DataFrame(
            [input_data]
        )


        print("\nInput DataFrame:")
        print(df)


        # --------------------------------------------------
        # Preprocessing
        # --------------------------------------------------

        X_processed = scaler_pipeline.transform(
            df
        )


        print("\nPreprocessing completed!")


        # --------------------------------------------------
        # Prediction
        # --------------------------------------------------

        prediction = rf_model.predict(
            X_processed
        )[0]


        # --------------------------------------------------
        # Probability
        # --------------------------------------------------

        probability = None

        if hasattr(
            rf_model,
            "predict_proba"
        ):

            probabilities = (
                rf_model.predict_proba(
                    X_processed
                )[0]
            )

            probability = float(
                max(probabilities) * 100
            )


        # --------------------------------------------------
        # Convert Prediction
        # --------------------------------------------------

        if prediction in [
            1,
            "1",
            True,
            "Placed",
            "Yes"
        ]:

            result = "Placed"

        else:

            result = "Not Placed"


        # --------------------------------------------------
        # Response
        # --------------------------------------------------

        return jsonify({

            "success": True,

            "prediction": result,

            "probability": probability

        })


    except Exception as e:

        print("\nPrediction Error:")
        print(e)

        return jsonify({

            "success": False,

            "error": str(e)

        })


# --------------------------------------------------
# Run App
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )