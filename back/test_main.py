import json
import unittest
from app import app
import pandas as pd

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_classify(self):
        tmp = [0] * 2249
        tmp[120] = 1
        
        rating = self.app.post('/predict_rating', data = json.dumps(tmp))
        self.assertEqual(rating.status_code, 200)
        self.assertEqual(type(rating.data), bytes)

if __name__ == '__main__':
    unittest.main()