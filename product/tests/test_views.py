from django.test import TestCase
from django.urls import reverse
from models import Model, Description

COUNT_PRODUCTS = 5

PRODUCT_NAMES = ['Albert', 'Albert Lite', 'Marie']


class TestView(TestCase):
    def test_get_detail(self):
        response = self.client.get(reverse('product:product_detail', args=['albert-lite']))
        self.assertEqual(response.status_code, 200)

    def test_get_list(self):
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)
