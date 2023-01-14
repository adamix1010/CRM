from django.shortcuts import reverse
from django.test import TestCase


class LandingPageTest(TestCase):
    def test_landing_page_get(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")

# TO DO: write rest of the tests for views
