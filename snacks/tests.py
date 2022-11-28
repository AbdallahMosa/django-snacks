from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class SnacksTitsing(SimpleTestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    def test_temp(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,"home.html")
    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)
    def test_temp_about(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response,"about.html")
