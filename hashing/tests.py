from django.test import TestCase
from .forms import HashForm
from selenium import webdriver
import hashlib

# class FunctionalTestCase(TestCase):# Test class for functional tests
    
#     def setUp(self):#before all Test are done
#         self.browser = webdriver.Firefox()
    
#     def test_there_is_homepage(self):
#         self.browser.get('http://127.0.0.1:8000')
#         self.assertIn('Enter hash here:', self.browser.page_source)

#     def test_hash_of_hello(self):#all function names should start with "test" for testing functions
#         self.browser.get('http://127.0.0.1:8000')
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys('hello')
#         self.browser.find_element_by_name('submit').click()
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',self.browser.page_source)


#     def tearDown(self):#after all Test are done
#         self.browser.quit()

class unitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')    


    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())
