import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
pickle_in = open("model_fish.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)

    categories = {
        0: 'Bream',
        1: 'Roach',
        2: 'Whitefish',
        3: 'Parkki',
        4: 'Perch',
        5: 'Pike',
        6: 'Smelt'
    }

    predicted_class = categories[prediction[0]]

    return render_template('index.html', prediction_text='The fish belong to species {}'.format(predicted_class))


if __name__ == '__main__':
    app.run()