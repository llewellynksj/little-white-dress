from django.test import TestCase
from django.urls import reverse
from .models import Product, Category


class ProductTests(TestCase):
    """
    Test Product Database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database
        """
        cls.product = Product.objects.create(
            item_name='Test',
            price='999',)

    def test_model_content(self):
        """
        Test objects successfully created
        """
        self.assertEqual(self.product.item_name, 'Test')
        self.assertEqual(self.product.price, '999')

    def test_url_exists_at_correct_location(self):
        """
        Test url location correct
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)


class CategoryTests(TestCase):
    """
    Test Category Database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database
        """
        cls.category = Category.objects.create(
            category_name='Test')

    def test_model_content(self):
        """
        Test objects successfully created
        """
        self.assertEqual(self.category.category_name, 'Test')
