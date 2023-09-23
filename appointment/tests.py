from django.test import TestCase
from .models import Appointment


class AppointmentTests(TestCase):
    """
    Test Appointment Database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database
        """
        cls.appointment = Appointment.objects.create(
            booking_date='2023-12-18',
            time='09:00',
            no_in_party='3',
            )

    def test_model_content(self):
        """
        Test objects successfully created
        """
        self.assertEqual(self.appointment.booking_date, '2023-12-18')
        self.assertEqual(self.appointment.time, '09:00')
        self.assertEqual(self.appointment.no_in_party, '3')
