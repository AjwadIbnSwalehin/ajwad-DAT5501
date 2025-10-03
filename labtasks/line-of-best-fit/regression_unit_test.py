import unittest
import numpy as np
import pandas as pd
import os
from regression import generate_synthetic_data, create_graph

class TestSyntheticDataGeneration(unittest.TestCase):
    
    def setUp(self):
        self.filename = "test_synthetic_data.csv"
        self.png_filename = "test_synthetic_data.png"
        np.random.seed(42)  # Set a seed for reproducibility in tests

    def tearDown(self):
        # Clean up: remove the test files if they exist
        try:
            os.remove(self.filename)
            os.remove(self.png_filename)
        except FileNotFoundError:
            pass

    def test_generate_synthetic_data(self):
        x_values, y_values_noisy, m, b = generate_synthetic_data(filename=self.filename)
        
        # Check the length of generated synthetic data
        self.assertEqual(len(x_values), 100)
        self.assertEqual(len(y_values_noisy), 100)
        
        # Ensure the CSV file is created and has the correct content
        self.assertTrue(os.path.exists(self.filename))
        df = pd.read_csv(self.filename)
        self.assertEqual(len(df), 100)
        self.assertIn('x', df.columns)
        self.assertIn('y', df.columns)
    
    def test_create_graph(self):
        # Generate data and create a graph
        generate_synthetic_data(filename=self.filename)
        create_graph(filename=self.filename, png_filename=self.png_filename)
        
        # Ensure that the PNG file is created by the `create_graph` function
        self.assertTrue(os.path.exists(self.png_filename))

if __name__ == '__main__':
    unittest.main()