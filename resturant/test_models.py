from django.test import TestCase
from .models import MenuItem, Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="ice cream", price=30, inventory=12)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "ice cream : 30")

class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(Name="ahmad2", No_of_guests=3, BookingDate="2023-06-21T20:21:00Z")
        itemstr = booking.get_booking()

        self.assertEqual(itemstr, "ahmad2")