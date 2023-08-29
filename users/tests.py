from django.test import TestCase
from .models import Users

# Create your tests here.

class UserModelTest(TestCase):

    def setUpTestData():
        Users.objects.create(name='Jennifer', bio='Hello, my name is Jennifer. These are my recipes.')

    def test_user(self):
        recipe = Users.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_bio(self):
        recipe = Users.objects.get(id=1)
        field_label = recipe._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

