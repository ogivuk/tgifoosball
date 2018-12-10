from django.db import models

class Tournament(models.Model):
    pass

class Player(models.Model):
    name = models.TextField(default='')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, default=None)
