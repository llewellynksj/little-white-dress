from django.test import TestCase
from .models import ContactDetail, Enquiry


class ContactDetailTests(TestCase):
    """
    Test ContactDetail Database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database
        """
        cls.contact = ContactDetail.objects.create(
            first_line_of_address='Test address 1',
            second_line_address='Test address 2',
            city='Test city',
            county='Test county',
            postcode='Test code',
            telephone='01234567891',
            email='test@test.com',
            )

    def test_model_content(self):
        """
        Test objects successfully created
        """
        self.assertEqual(self.contact.first_line_of_address, 'Test address 1')
        self.assertEqual(self.contact.second_line_address, 'Test address 2')
        self.assertEqual(self.contact.city, 'Test city')
        self.assertEqual(self.contact.county, 'Test county')
        self.assertEqual(self.contact.postcode, 'Test code')
        self.assertEqual(self.contact.telephone, '01234567891')
        self.assertEqual(self.contact.email, 'test@test.com')

    def test_url_exists_at_correct_location(self):
        """
        Test url location correct
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


class EnquiryTests(TestCase):
    """
    Test Enquiry Database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Create test database
        """
        cls.enquiry = Enquiry.objects.create(
            full_name='Test Name',
            email='test@test.com',
            message='This is a test!',
        )

    def test_model_content(self):
        """
        Test objects successfully created
        """
        self.assertEqual(self.enquiry.full_name, 'Test Name')
        self.assertEqual(self.enquiry.email, 'test@test.com')
        self.assertEqual(self.enquiry.message, 'This is a test!')
