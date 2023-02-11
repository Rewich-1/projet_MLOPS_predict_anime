from flask import Flask, request, jsonify
from tensorflow import keras
import numpy as np

app = Flask(__name__)

#--- Testing : ---
from pathlib import Path
if not Path('./models/model.zip').is_file():
  raise Exception("Model not found, should be in models/ named 'model.zip'")

from pyunpack import Archive
Archive('./models/model.zip').extractall('./models/')

if not Path('./models/model.h5').is_file():
  raise Exception("Model not found in the zip, should be named 'model.h5'")

# -- Load model --
model = keras.models.load_model('./models/model.h5')

# -- Route for getting a prediction --
@app.route('/predict_rating', methods=['POST'])
def predict():
    data = np.array(request.get_json(force=True)['data']).astype("float32")
    return {"prediction": model.predict(data)}

# -- Let's start the App --
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)