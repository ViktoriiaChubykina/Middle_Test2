from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nature")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Nature")
        self.assertTrue(isinstance(self.category, Category))

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Nature")

class ImageModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nature")
        self.image = Image.objects.create(
            title="Test Image",
            image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            age_limit=18
        )
        self.image.categories.add(self.category)

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Test Image")
        self.assertTrue(isinstance(self.image, Image))
        self.assertEqual(self.image.age_limit, 18)
        self.assertEqual(self.image.categories.count(), 1)

    def test_image_string_representation(self):
        self.assertEqual(str(self.image), "Test Image")

    def test_image_category_relationship(self):
        self.assertIn(self.category, self.image.categories.all())