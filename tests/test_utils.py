import unittest
import pandas as pd
from app.utils import calculate_z_scores, calculate_vwap

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'price': [0.1809, 0.1805, 0.1804, 0.1796, 0.1795],
            'volume': [281247.50, 11.28, 97907.65, 8.62, 276.39]
        })

    def test_calculate_z_scores(self):
        z_scores = calculate_z_scores(self.df, 'volume')
        self.assertEqual(len(z_scores), len(self.df))
        self.assertIsInstance(z_scores, pd.Series)

    def test_calculate_vwap(self):
        vwap = calculate_vwap(self.df)
        self.assertGreater(vwap, 0)

if __name__ == '__main__':
    unittest.main()
