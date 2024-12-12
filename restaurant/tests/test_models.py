from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_menu_str(self):
        # Create an instance of the Menu model
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        
        # Check the string representation of the menu item
        self.assertEqual(str(item), "IceCream : 80")
