from django.test import TestCase
from django.urls import reverse
from models import Model, Description, Variety, Gallery, Slider, Color, Category, Feature, VideoUrl, RewardsImage, \
    Specification

PRODUCTS = (
    ('Cat1', 'Albert',),
    ('Cat2', 'Marie',)
)


class TestView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for product in PRODUCTS:
            category = Category.objects.create(name=product[0])

    def test_get_detail(self):
        response = self.client.get(reverse('product:product_detail', args=['albert-lite']))
        self.assertEqual(response.status_code, 200)

    def test_get_list(self):
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)
