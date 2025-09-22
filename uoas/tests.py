from django.test import TestCase, Client
from django.urls import reverse
from printerapp.models import Slide

class SolarPageTests(TestCase):
    def setUp(self):
        # Create sample slides
        Slide.objects.create(
            image_url='https://example.com/image1.jpg',
            location='Location 1',
            project_link='https://example.com/project1'
        )
        Slide.objects.create(
            image_url='https://example.com/image2.jpg',
            location='Location 2',
            project_link='https://example.com/project2'
        )
        self.client = Client()

    def test_solar_page_status_code(self):
        response = self.client.get(reverse('solar'))
        self.assertEqual(response.status_code, 200)

    def test_solar_page_contains_slides(self):
        response = self.client.get(reverse('solar'))
        self.assertContains(response, 'Location 1')
        self.assertContains(response, 'Location 2')
        self.assertContains(response, 'https://example.com/image1.jpg')
        self.assertContains(response, 'https://example.com/image2.jpg')

class ContactPageTests(TestCase):
    def test_contact_page_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_post_valid(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Hello'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success

    def test_contact_page_post_invalid(self):
        response = self.client.post(reverse('contact'), {
            'name': '',
            'email': '',
            'message': ''
        })
        self.assertEqual(response.status_code, 302)  # Redirect after error

class PrinterPageTests(TestCase):
    def test_printer_page_status_code(self):
        response = self.client.get(reverse('printer'))
        self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
