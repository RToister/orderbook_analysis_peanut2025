import unittest
import pandas as pd
from app.analysis import analyze_orderbook

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'price': [0.1809, 0.1805, 0.1804, 0.1796, 0.1795],
            'volume': [281247.50, 11.28, 97907.65, 8.62, 276.39]
        })

    def test_analyze_orderbook_output(self):
        result = analyze_orderbook(self.df, "test")
        self.assertIsInstance(result, dict)
        self.assertIn("volume_anomalies", result)
        self.assertIn("price_anomalies", result)
        self.assertIn("local_spikes", result)
        self.assertIn("boundary_anomalies", result)

if __name__ == '__main__':
    unittest.main()
