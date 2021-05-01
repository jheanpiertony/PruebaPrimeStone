from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestFrontViews(TestCase):
    def test_homeview(self):
        url = reverse('front:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
