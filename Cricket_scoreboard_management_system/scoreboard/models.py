from django.db import models

# Create your models here.

class Match(models.Model):
    match_number = models.PositiveSmallIntegerField(unique = True, default=1, blank = False, null = True)
    match_date = models.DateField(auto_now_add = True, blank = False, null = True)
    match_location = models.CharField(max_length = 15, blank = False, null = True)
    match_over = models.IntegerField(blank = False, default=1)

class Team(models.Model):
    team_number = [
        (1, 'Team 1'),
        (2, 'Team 2'),
    ]
    match_number = models.ForeignKey(Match, on_delete = models.CASCADE, blank = False, null = True, default = 1)
    team_name = models.CharField(max_length =20, blank = False, null = True)
    team_coach = models.CharField(max_length = 10, blank = False, null = True)
    team_homeground = models.CharField(max_length = 15, blank = True, null = True)
    team_number = models.IntegerField(default = 1, choices = team_number)

class Player(models.Model):
    role = [
        ('BT', 'Batsman'),
        ('B', 'Bowler'),
        ('AR', 'All Rounder'),
    ]
    player_name = models.CharField(max_length=15, blank = False, null = True)
    player_team = models.ForeignKey(Team, on_delete = models.CASCADE, blank = False, null = True)
    match_number = models.ForeignKey(Match, on_delete = models.CASCADE, blank = False, null = True, default = 1)
    player_role = models.CharField(max_length = 2, choices = role)


class Score(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    match_number = models.ForeignKey(Match, on_delete = models.CASCADE, blank = False, null = True, default = 1)
    team_number = models.ForeignKey(Team, default = 1, on_delete=models.CASCADE)
    run = models.PositiveIntegerField()
    wickets = models.PositiveIntegerField()
    overs = models.PositiveIntegerField()