from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)      

    def test_can_add_players_and_retrieve_them_later(self):
        # Foosball local admin opens the web app
        self.browser.get(self.live_server_url)

        # (S)he notices the name T.G.I.Foosball in the title and the first header
        self.assertIn('T.G.I.Foosball', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('T.G.I.Foosball', header_text)

        # The admin is invited to enter a new player
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter a new player name"
        )

        # The admin types "John Doe" into a text box
        inputbox.send_keys('John Doe')

        # When the admin hits enter, the page updates, and now the page lists
        # "1: John Doe" as a player in the list of players:
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: John Doe')

        # There is still a text box inviting the admin to add another player.
        # The admin enters "Jenny Doe":
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Jenny Doe')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both players in the list:
        self.wait_for_row_in_list_table('1: John Doe')
        self.wait_for_row_in_list_table('2: Jenny Doe')

        self.fail('Finish the test!')

        # Satisfied, the admin goes back to sleep
