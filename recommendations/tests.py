from django.test import TestCase
from .models import Recommendation


class RecommendationTests(TestCase):
    """
    Test Recommendation Database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database
        """
        cls.recommendation = Recommendation.objects.create(
            type_of_recommendation='Catering',
            title='Test title',
        )

    def test_model_content(self):
        """
        Test objects successfully created
        """
        self.assertEqual(
            self.recommendation.type_of_recommendation, 'Catering')
        self.assertEqual(self.recommendation.title, 'Test title')
