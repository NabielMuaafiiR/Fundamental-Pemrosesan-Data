import unittest
from unittest.mock import patch
import pandas as pd
from utils.load import load_to_csv


class TestLoad(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_load_to_csv(self, mock_to_csv):
        # Arrange
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Act
        load_to_csv(df, 'test.csv')
        
        # Assert
        mock_to_csv.assert_called_once_with('test.csv', index=False)

if __name__ == '__main__':
    unittest.main()