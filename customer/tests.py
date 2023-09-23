from django.test import TestCase
from django.contrib.auth.models import User


class TestCustomerModel(TestCase):
    """
    Test Customer Model
    """
    def test_string_representation(self):
        user = User(username="Test")
        self.assertEqual(str(user), user.username)
