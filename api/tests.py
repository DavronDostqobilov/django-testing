from django.test import TestCase
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        p = Product.objects.create(
            name='name 01',
            descripcion='desc 01',
            price=100.09
        )

    def test_is_created(self):
        count = Product.objects.all().count()
        self.assertEqual(count, 1)

    def test_name(self):
        p = Product.objects.first()
        self.assertEqual(p.name, 'name 01')



class ProductViewTestCase(TestCase):
    def setUp(self):
        p = Product.objects.create(
            name='name 01',
            descripcion='desc 01',
            price=100.09
        )
    
    def test_get_all_products(self):
        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)