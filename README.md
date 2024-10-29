# Flask Machine Learning Prediction App

This is a Flask web application that uses pre-trained machine learning models to make predictions based on user input. The application predicts `Reed Space` and `Reed Count` using LightGBM models.

## Features

- User input form for prediction parameters
- Validation of input values
- Predictions using pre-trained LightGBM models
- Display of prediction results

## Requirements

- Python 3.7+
- Flask 3.0.3
- joblib 1.4.2
- numpy 2.1.2
- scikit-learn 1.5.2
- lightgbm 4.5.0

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HaseebImd/Flask-Machine-Learning-Prediction-App.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Place the pre-trained model files (`lgb_model_reed_space_A.pkl` and `lgb_model_reed_count_A.pkl`) in the project directory.

## Usage

1. Run the Flask application:
    ```sh
    python myapp.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the required input values and submit the form to get predictions.

## File Structure

- `myapp.py`: Main application file containing the Flask routes and prediction logic.
- `templates/`: Directory containing HTML templates.
  - `home.html`: Template for the home page with the input form.
  - `result.html`: Template for displaying prediction results.
- `requirements.txt`: List of required Python packages.


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [LightGBM](https://lightgbm.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
