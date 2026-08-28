from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Product


class InventoryAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword2026!"
        )

        response = self.client.post(
            "/api/token/",
            {
                "username": "testuser",
                "password": "TestPassword2026!",
            },
            format="json",
        )

        self.access_token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic products"
        )

    def test_authenticated_user_can_list_products(self):
        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_list_products(self):
        self.client.credentials()

        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_product(self):
        data = {
            "name": "Mechanical Keyboard",
            "sku": "ELEC-002",
            "category": self.category.id,
            "description": "Mechanical USB keyboard",
            "price": "79.99",
            "stock": 10,
            "is_active": True,
        }

        response = self.client.post(
            "/api/products/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_product_price_cannot_be_negative(self):
        data = {
            "name": "Invalid Product",
            "sku": "TEST-001",
            "category": self.category.id,
            "price": "-10.00",
            "stock": 5,
        }

        response = self.client.post(
            "/api/products/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("price", response.data)