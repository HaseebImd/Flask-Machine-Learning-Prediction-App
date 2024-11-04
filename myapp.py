from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__, template_folder="templates")

# Load the pre-trained machine learning models
lgb_model_reed_space_A = joblib.load("lgb_model_reed_space_A.pkl")
lgb_model_reed_count_A = joblib.load("lgb_model_reed_count_A.pkl")
lgbm_warp_model = joblib.load("lgbm_warp_model.pkl")
lgbm_weft_model = joblib.load("lgbm_weft_model.pkl")


# Define the default route
@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")


# Define the predict route
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Extract input values from the form
        input_data = [
            float(request.form["WARP"]),
            float(request.form["WEFT"]),
            float(request.form["ENDS"]),
            float(request.form["PICKS"]),
            float(request.form["Width_a"]),
        ]
        print("input_data", input_data)

        # Check if any input value is less than 1 or greater than 10000
        if any(value < 1 or value > 10000 for value in input_data):
            return render_template("predict.html", error="Invalid input.")

        # Convert inputs to a numpy array
        input_data = np.array([input_data])

        # Make predictions for warp and weft contraction
        warp_contraction = int(lgbm_warp_model.predict(input_data)[0])
        weft_contraction = int(lgbm_weft_model.predict(input_data)[0])

        # Prepare new input data with predicted contractions
        contraction_input = np.array(
            [
                [
                    input_data[0][0],
                    input_data[0][1],
                    input_data[0][2],
                    input_data[0][3],
                    input_data[0][4],
                    warp_contraction,
                    weft_contraction,
                ]
            ]
        )

        # Make predictions for reed space and reed count using the contraction values
        prediction_reed_space = int(
            lgb_model_reed_space_A.predict(contraction_input)[0]
        )
        prediction_reed_count = int(
            lgb_model_reed_count_A.predict(contraction_input)[0]
        )

        # Redirect to the result page with the prediction results
        return redirect(
            url_for(
                "result",
                reed_space=prediction_reed_space,
                reed_count=prediction_reed_count,
                warp_contraction=warp_contraction,
                weft_contraction=weft_contraction,
            )
        )

    # If the request method is GET, render the predict.html page
    return render_template("predict.html")


# Define the result route
@app.route("/result")
def result():
    reed_space = request.args.get("reed_space", None)
    reed_count = request.args.get("reed_count", None)
    warp_contraction = request.args.get("warp_contraction", None)
    weft_contraction = request.args.get("weft_contraction", None)
    return render_template(
        "result.html",
        reed_space=reed_space,
        reed_count=reed_count,
        warp_contraction=warp_contraction,
        weft_contraction=weft_contraction,
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True)