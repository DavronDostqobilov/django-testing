from django.http import HttpRequest, JsonResponse
from django.views import View
from .models import Product


def to_dict(product: Product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.descripcion,
        "price": product.price
    }


class ProductView(View):
    def get(self, request: HttpRequest, pk: int = None) -> JsonResponse:
        if pk:
            try:
                product = Product.objects.get(id=pk)
                return JsonResponse(to_dict(product))
            except Product.DoesNotExist:
                return JsonResponse({"error": "object is not found."}, status=404)
        else:
            products = Product.objects.all()
            data = [to_dict(product) for product in products]

            return JsonResponse(data, safe=False)
