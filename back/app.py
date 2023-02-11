from flask import Flask, request, jsonify
from tensorflow import keras

app = Flask(__name__)

#--- Testing : ---
from pathlib import Path
if not Path('./models/model.zip').is_file():
  raise Exception("Model not found, should be in models/ named 'model.zip'")

# -- Load model --
from pyunpack import Archive
Archive('./models/model.zip').extractall('./models/')

if not Path('./models/model.zip').is_file():
  raise Exception("Model not found, should be in models/ named 'model.zip'")

# -- Route for getting a prediction --
@app.route('/predict_rating', methods=['POST'])
def predict():
    #request.get_json(force=True)
    return {"prediction": 0.5}

# -- Let's start the App --
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)