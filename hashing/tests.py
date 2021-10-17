from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):# Test class for functional tests
    
    def setUp(self):#before all Test are done
        self.browser = webdriver.Firefox()
    
    def test_there_is_homepage(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('install', self.browser.page_source)

        
    def tearDown(self):#after all Test are done
        self.browser.quit()


