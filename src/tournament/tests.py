from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from tournament.views import home_page
from tournament.models import Player

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': 'A new player'})

        self.assertEqual(Player.objects.count(), 1)
        new_player = Player.objects.first()
        self.assertEqual(new_player.name, 'A new player')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new player'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],'/tournament/the-only-tournament-in-the-world/')

    def test_only_saves_players_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Player.objects.count(), 0)

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

class TournamentViewTest(TestCase):

    def test_uses_tournament_template(self):
        response = self.client.get("/tournament/the-only-tournament-in-the-world/")
        self.assertTemplateUsed(response, "tournament.html")
    
    def test_displays_all_players(self):
        Player.objects.create(name="Player 1")
        Player.objects.create(name="Player 2")

        response = self.client.get("/tournament/the-only-tournament-in-the-world/")

        self.assertContains(response, "Player 1")
        self.assertContains(response, "Player 2")