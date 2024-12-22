from django.test import TestCase

# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())