from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from selenium import webdriver

from homepage.views import index


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resloves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'<title>Growth Studio-Enjoy Create&Share</title>', response.content)


class HomePageTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.selenium.maximize_window()
        super(HomePageTestCase, self).setUp()
        
    def tearDown(self):
        self.selenium.quit()
        super(HomePageTestCase, self).tearDown()
        
    def test_can_visit_homepage(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn("Growth Studio-Enjoy Create&Share", self.selenium.title)
        