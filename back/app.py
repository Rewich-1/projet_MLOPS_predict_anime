from flask import Flask, request, jsonify
from tensorflow import keras

app = Flask(__name__)

#--- Testing : ---
#-----------------

# -- Load model --
#model = 

# -- Route for getting a prediction --
@app.route('/predict_rating', methods=['POST'])
def predict():
    #request.get_json(force=True)
    return {"prediction": 0.5}

# -- Let's start the App --
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)