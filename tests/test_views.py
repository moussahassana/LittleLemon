# In tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer 

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up the APIClient and create multiple test MenuItems
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="Pasta", price=12.99, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Burger", price=8.99, inventory=50)
        self.menu_item3 = MenuItem.objects.create(title="Salad", price=6.99, inventory=20)

    def test_getall(self):
        # Make a GET request to the menu endpoint
        response = self.client.get('/restaurant/menu/')
        
        # Check the status code
        self.assertEqual(response.status_code, 200)
        
        # Serialize the menu items
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        
        # Compare the serialized data with the response
        self.assertEqual(response.data, serializer.data)  # Ensure the response matches the serialized data
