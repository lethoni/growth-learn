from django.test import TestCase
from .models import Blog, User
from datetime import datetime
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


# Create your tests here.
class BlogpostListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='loic', email='hello@qq.com',
                                             password='phodal')
    def test_blog_list_page(self):
        Blog.objects.create(title='hello', author=self.user, slug='this_is_a_test',
                            body='This is a blog', posted=datetime.now)
        response = self.client.get('/blog/')
        self.assertIn(b'This is a blog', response.content)

class HomepageTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.user = User.objects.create_user(username='loic', email='hello@qq.com',
                                             password='phodal')
        super(HomepageTestCase, self).setUp()

        def tearDown(self):
            self.selenium.quit()
            super(HomepageTestCase, self).tearDown()

        def test_should_goto_blog_page_from_homepage(self):
            Blog.objects.create(title='hello', author=self.user, slug='this_is_a_test',
                                body='This is blog detail', posted=datetime.now)
            self.selenium.get('%s%s' %(self.live_server_url, "/"))
            self.selenium.find_element_by_link_text('博客').click()
            self.assertIn('This is blog detail', self.selenium.page_source)

        def test_not_found_blog(self):
            response = self.client.get('blog/this_not_a_blog.html')
            self.assertEqual(404, response.status_code)

