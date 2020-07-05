from django.db import models

# Create your models here.


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=100)
    date = models.DateField()
    team1 = models.CharField(max_length=250)
    team2 = models.CharField(max_length=250)
    toss_winner = models.CharField(max_length=250)
    toss_decision = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=250)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    umpire1 = models.CharField(max_length=250, null=True)
    umpire2 = models.CharField(max_length=250, null=True)
    umpire3 = models.CharField(max_length=250, null=True)


class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=250)
    bowling_team = models.CharField(max_length=250)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=250)
    non_striker = models.CharField(max_length=250)
    bowler = models.CharField(max_length=250)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=250, null=True)
    dismissal_kind = models.CharField(max_length=250, null=True)
    fielder = models.CharField(max_length=250, null=True)
