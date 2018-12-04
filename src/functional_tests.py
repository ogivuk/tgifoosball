from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_players_and_retrieve_them_later(self):
        # Foosball local admin opens the web app
        self.browser.get('http://localhost:8000')

        # (S)he notices the name TGIFoosball in the title
        self.assertIn('TGIFoosball', self.browser.title)
        self.fail("Finish the test!")

        # The admin is invited to enter a new player

        # The admin types "John Doe" into a text box

        # When the admin hits enter, the page updates, and now the page lists
        # "1: John Doe" as a player in the list of players:

        # There is still a text box inviting the admin to add another player.
        # The admin enters "Jenny Doe":

        # The page updates again, and now shows both players in the list:

        # Satisfied, the admin goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
