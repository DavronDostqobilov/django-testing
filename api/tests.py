from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def test_is_created(self):
        p1 = Product.objects.create(
            name='name 01',
            descripcion='desc 01',
            price=100.09
        )
        p2 = Product.objects.create(
            name='name 02',
            descripcion='desc 02',
            price=140.90
        )

        count = Product.objects.all().count()

        self.assertEqual(count, 2)