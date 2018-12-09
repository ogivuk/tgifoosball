from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from tournament.views import home_page
from tournament.models import Player

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new player'})
        self.assertIn('A new player', response.content.decode())
        self.assertTemplateUsed(response,'home.html')

class PlayerModelTest(TestCase):

    def test_saving_and_retrieving_players(self):
        first_player = Player()
        first_player.name = "The first (ever) player"
        first_player.save()

        second_player = Player()
        second_player.name = "Player the second"
        second_player.save()

        saved_players = Player.objects.all()
        self.assertEqual(saved_players.count(), 2)

        first_saved_player = saved_players[0]
        second_saved_player = saved_players[1]
        self.assertEqual(first_saved_player.name, "The first (ever) player")
        self.assertEqual(second_saved_player.name, "Player the second")