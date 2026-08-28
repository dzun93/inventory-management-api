from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category").all().order_by("name")
    serializer_class = ProductSerializer

    filterset_fields = ["category", "is_active"]
    search_fields = ["name", "sku", "description", "category__name"]
    ordering_fields = ["name", "price", "stock", "created_at"]
    ordering = ["name"]