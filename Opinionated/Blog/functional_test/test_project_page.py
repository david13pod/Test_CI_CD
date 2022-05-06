import time
from selenium import webdriver
from Blog.models import Post,Comment
from django.contrib.auth.models import  User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse



class TestProjectPage(StaticLiveServerTestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser = webdriver.Chrome('Blog/functional_test/chromedriver')

    def tearDown(self):
        self.browser.close

    def test_firsttest(self):
        self.browser.get(self.live_server_url)
        # time.sleep(50)

        newpage=self.browser.find_element_by_class_name('content')
        print(newpage.find_element_by_id('no_post').text)
        self.assertEquals(newpage.find_element_by_id('no_post').text, 'No post yet')


### other useful commands
# .find_element_by_tag_name('a').click()
# check if the redirect equlas the currenturl
# .current_url
# click_url=self.live_server_url + reverse('buttonurl')

# .find_element_by_link_text('submit').click()
# use to get the element with an anchor tag just using the name

