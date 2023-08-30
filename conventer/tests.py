from django.test import SimpleTestCase


# Create your tests here.
class SimpleTest(SimpleTestCase):
    def testing_currency_app(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
