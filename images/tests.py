from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class ImageTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.location = Location(name="juja")
        self.location.save()

        self.category = Category(name="trip")
        self.category.save()



        self.image = Image(image = "ggg.jpg",name="new",desc="hkjhlhj ljkh",loc=self.location,category=self.category)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

        self.assertTrue(isinstance(self.location,Location))
        self.assertTrue(isinstance(self.category,Category))