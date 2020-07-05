from django.core.management import BaseCommand
from django.conf import settings
from ipl_app.models import Match, Delivery
import csv


class Command(BaseCommand):
    """
  Add ipl data to db
  """

    def handle(self, **options):
        self.add_ipl_details()

    @staticmethod
    def add_ipl_details():
        print(settings.STATICFILES_DIRS)
        path = settings.STATICFILES_DIRS[0]
        counter = 0
        with open(path + "/csv/matches.csv") as f:
            reader = csv.reader(f)
            print('start matches')
            for row in reader:
                counter = counter + 1
                if counter != 1:
                    _, created = Match.objects.get_or_create(
                        id=row[0],
                        season=row[1],
                        city=row[2],
                        date=row[3],
                        team1=row[4],
                        team2=row[5],
                        toss_winner=row[6],
                        toss_decision=row[7],
                        result=row[8],
                        dl_applied=row[9],
                        winner=row[10],
                        win_by_runs=row[11],
                        win_by_wickets=row[12],
                        player_of_match=row[13],
                        venue=row[14],
                        umpire1=row[15],
                        umpire2=row[16],
                        umpire3=row[17]
                    )
            print('stop matches')
        counter = 0
        with open(path + "/csv/deliveries.csv") as f:
            reader = csv.reader(f)
            print('start deliveries')
            for row in reader:
                counter = counter + 1
                if counter != 1:
                    _, created = Delivery.objects.get_or_create(
                        match_id=row[0],
                        inning=row[1],
                        batting_team=row[2],
                        bowling_team=row[3],
                        over=row[4],
                        ball=row[5],
                        batsman=row[6],
                        non_striker=row[7],
                        bowler=row[8],
                        is_super_over=row[9],
                        wide_runs=row[10],
                        bye_runs=row[11],
                        legbye_runs=row[12],
                        noball_runs=row[13],
                        penalty_runs=row[14],
                        batsman_runs=row[15],
                        extra_runs=row[16],
                        total_runs=row[17],
                        player_dismissed=row[18],
                        dismissal_kind=row[19],
                        fielder=row[20]
                    )
            print('stop deliveries')