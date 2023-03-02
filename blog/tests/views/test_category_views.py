# Core Django imports
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.test import Client
from django.test import TestCase
from django.urls import reverse

# Third party django app imports
# from model_mommy import mommy


# Blog application imports
from blog.models.article_models import Article
from blog.models.category_models import Category


class CategoriesListViewTestCase(TestCase):
    """
    Class to test the list of all categories
    """

    def setUp(self):
        self.client = Client()
        # self.categories = mommy.make(Category, _quantity=5)

    def test_categories_list_view_status_code(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(response.status_code, 200)

    def test_categories_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(response.status_code, 200)
