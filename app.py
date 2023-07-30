import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model using joblib
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print("Error loading the model:", str(e))
    # Handle the error appropriately (e.g., log the error, set a default model, etc.).


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                     'mean smoothness', 'mean compactness', 'mean concavity',
                     'mean concave points', 'mean symmetry', 'mean fractal dimension',
                     'radius error', 'texture error', 'perimeter error', 'area error',
                     'smoothness error', 'compactness error', 'concavity error',
                     'concave points error', 'symmetry error', 'fractal dimension error',
                     'worst radius', 'worst texture', 'worst perimeter', 'worst area',
                     'worst smoothness', 'worst compactness', 'worst concavity',
                     'worst concave points', 'worst symmetry', 'worst fractal dimension']

    df = pd.DataFrame(features_value, columns=features_name)

    try:
        # Predict using the loaded model
        output = model.predict(df)
    except Exception as e:
        print("Error during prediction:", str(e))
        # Handle the error appropriately (e.g., return an error response to the client).

    if output == 0:
        res_val = "** breast cancer **"
    else:
        res_val = "no breast cancer"

    return render_template('index.html', prediction_text='Patient has {}'.format(res_val))


if __name__ == "__main__":
    app.run()
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model using joblib
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print("Error loading the model:", str(e))
    # Handle the error appropriately (e.g., log the error, set a default model, etc.).


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                     'mean smoothness', 'mean compactness', 'mean concavity',
                     'mean concave points', 'mean symmetry', 'mean fractal dimension',
                     'radius error', 'texture error', 'perimeter error', 'area error',
                     'smoothness error', 'compactness error', 'concavity error',
                     'concave points error', 'symmetry error', 'fractal dimension error',
                     'worst radius', 'worst texture', 'worst perimeter', 'worst area',
                     'worst smoothness', 'worst compactness', 'worst concavity',
                     'worst concave points', 'worst symmetry', 'worst fractal dimension']

    df = pd.DataFrame(features_value, columns=features_name)

    try:
        # Predict using the loaded model
        output = model.predict(df)
    except Exception as e:
        print("Error during prediction:", str(e))
        # Handle the error appropriately (e.g., return an error response to the client).

    if output == 0:
        res_val = "** breast cancer **"
    else:
        res_val = "no breast cancer"

    return render_template('index.html', prediction_text='Patient has {}'.format(res_val))


if __name__ == "__main__":
    app.run()
