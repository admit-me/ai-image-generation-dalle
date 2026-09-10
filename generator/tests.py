from django.test import Client, SimpleTestCase
from django.urls import reverse


class ImageGeneratorViewTests(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_get_page_loads(self):
        response = self.client.get(reverse('generate_image'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AI-Powered Image Generator')

    def test_empty_prompt_is_rejected(self):
        response = self.client.post(reverse('generate_image'), {'prompt': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a prompt.')
