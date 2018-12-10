from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from tournament.views import home_page
from tournament.models import Player, Tournament

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

class TournamentandPlayerModelTest(TestCase):

    def test_saving_and_retrieving_players(self):
        tournament = Tournament()
        tournament.save()

        first_player = Player()
        first_player.name = "The first (ever) player"
        first_player.tournament = tournament
        first_player.save()

        second_player = Player()
        second_player.name = "Player the second"
        second_player.tournament = tournament
        second_player.save()

        saved_list = Tournament.objects.first()
        self.assertEqual(saved_list, tournament)

        saved_players = Player.objects.all()
        self.assertEqual(saved_players.count(), 2)

        first_saved_player = saved_players[0]
        second_saved_player = saved_players[1]
        self.assertEqual(first_saved_player.name, "The first (ever) player")
        self.assertEqual(first_saved_player.tournament, tournament)
        self.assertEqual(second_saved_player.name, "Player the second")
        self.assertEqual(second_saved_player.tournament, tournament)

class TournamentViewTest(TestCase):

    def test_uses_tournament_template(self):
        response = self.client.get("/tournament/the-only-tournament-in-the-world/")
        self.assertTemplateUsed(response, "tournament.html")
    
    def test_displays_all_players(self):
        tournament = Tournament.objects.create()
        Player.objects.create(name="Player 1", tournament=tournament)
        Player.objects.create(name="Player 2", tournament=tournament)

        response = self.client.get("/tournament/the-only-tournament-in-the-world/")

        self.assertContains(response, "Player 1")
        self.assertContains(response, "Player 2")

class NewTournamentTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/tournament/new', data={'item_text': 'A new player'})

        self.assertEqual(Player.objects.count(), 1)
        new_player = Player.objects.first()
        self.assertEqual(new_player.name, 'A new player')

    def test_redirects_after_POST(self):
        response = self.client.post('/tournament/new', data={'item_text': 'A new player'})

        self.assertRedirects(response, '/tournament/the-only-tournament-in-the-world/')