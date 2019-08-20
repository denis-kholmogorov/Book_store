from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPagesView

class HomePagesTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Книжки')
        self.assertNotContains(self.response, 'Сиськи')

    def test_homepage_does_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Sisi')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')
        self.assertNotContains(self.response, 'Сиськи')

    def test_homepage_does_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Sisi')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPagesView.as_view().__name__
        )