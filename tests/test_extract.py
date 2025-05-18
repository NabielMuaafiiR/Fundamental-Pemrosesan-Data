import unittest
from unittest.mock import patch, MagicMock
from utils.extract import scrape_products

class TestExtract(unittest.TestCase):

    @patch('utils.extract.requests.Session.get')
    def test_scrape_main_success(self, mock_get):
        # Arrange
        url = "https://fashion-studio.dicoding.dev/"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"""
        <html>
            <body>
                <div class="collection-card">
                    <h3 class="product-title">Test Product</h3>
                    <div class="price-container">$10</div>
                    <p>Rating: 5 stars</p>
                    <p>Colors: Red, Blue</p>
                    <p>Size: M, L</p>
                    <p>Gender: Unisex</p>
                </div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        # Act
        result = scrape_products(url)

        # Assert
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn('title', result[0])
        self.assertEqual(result[0]['title'], 'Test Product')

    @patch('utils.extract.requests.Session.get')
    def test_scrape_main_failure(self, mock_get):
    # Arrange
      url = "https://fashion-studio.dicoding.dev/"
      mock_response = MagicMock()
      mock_response.status_code = 404
      mock_response.raise_for_status.side_effect = Exception("404 Client Error")  # Simulasikan error
      mock_get.return_value = mock_response

      # Act & Assert
      with self.assertRaises(Exception) as context:
        scrape_products(url)
        self.assertIn('Gagal mengakses URL', str(context.exception))



if __name__ == '__main__':
    unittest.main()