from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__, template_folder="templates")

# Load the pre-trained machine learning models
lgb_model_reed_space_A = joblib.load('lgb_model_reed_space_A.pkl')
lgb_model_reed_count_A = joblib.load('lgb_model_reed_count_A.pkl')


# Define the default route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extract input values from the form
        input_data = [
            float(request.form["WARP"]),
            float(request.form["WEFT"]),
            float(request.form["ENDS"]),
            float(request.form["PICKS"]),
            float(request.form["Width_a"]),
            float(request.form["Warp_Contraction"]),
            float(request.form["Weft_Contraction"]),
        ]
        print("input_data", input_data)

        # Check if any input value is less than 1 or greater than 10000
        if any(value < 1 or value > 10000 for value in input_data):
            return render_template("home.html", error="Invalid input.")

        # Convert inputs to a numpy array
        input_data = np.array([input_data])

        # Make predictions using the loaded models and round to 3 decimal places
        prediction_reed_space = round(lgb_model_reed_space_A.predict(input_data)[0], 3)
        prediction_reed_count = round(lgb_model_reed_count_A.predict(input_data)[0], 3)

        # Redirect to the result page with the prediction results
        return redirect(url_for("result", reed_space=prediction_reed_space, reed_count=prediction_reed_count))

    return render_template("home.html")


# Define the result route
@app.route("/result")
def result():
    reed_space = request.args.get("reed_space", None)
    reed_count = request.args.get("reed_count", None)
    return render_template("result.html", reed_space=reed_space, reed_count=reed_count)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
