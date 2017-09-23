from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starts_a_list_and_retrieve_it_later(self):
        # Maki has decided to make a to-do app to follow this tutorial.
        # She decides to visit the homepage first.
        self.browser.get('http://localhost:8000')

        # She notices the page title and that the header mentions to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # 'Browser title was ' + browser.title

        # She is asked to enter a to-do list item right away

        # Maki decides to add "Buy a new brain" into a text box.
        # Maki's brain is very tired.

        # Once hitting return, the page updates and now the page lists:
        # 1: Buy a new brain as an item in her to-do list

        # The text box awaits another item addition. Maki enters:
        # "Use new brain to learn test-driven development"

        # The page updates itself and displays both to-do list items.

        # Maki wonders if the site will remember what she put in her
        # list. Then she sees that the site has generated a unique URL
        # for her.

        # She visits that URL--her to-do list is saved!

        # With a slight mental victory, Maki re-thinks buying a new
        # brain and instead stays up all night trying to complete
        # this tutorial.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
