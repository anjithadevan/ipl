from django.shortcuts import render
from django.views.generic import TemplateView
from ipl_app.models import Match
# Create your views here.


class IplView(TemplateView):
    template_name = "ipl_app/ipl.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        seasons = Match.objects.all().values_list('season', flat=True).distinct()
        winner_dict = {}
        seasons_winners = []
        toss_winner_list = []
        player_of_match = []
        winner_location = []
        bat_decided_per = []
        winner_with_large_runs = []
        location_with_matches = []
        for season in seasons:
            # Top 4 teams in terms of wins

            winners = Match.objects.filter(season=season).values_list('winner', flat=True)
            winner = self.get_list_from_query_set(winners)
            winner_list = []
            for i in range(0, 4):
                max_winner = max(winner, key=winner.count)
                winner_list.append(max_winner)
                winner = list(filter((max_winner).__ne__, winner))
            winner_dict[season] = winner_list

            # team won the most number of tosses in the season
            toss_winner_list.append(self.get_max_value(season, 'toss_winner'))

            # maximum number of Player of the Match awards in the whole season
            player_of_match.append(self.get_max_value(season, 'player_of_match'))

            # seasonal winners
            seasons_winners.append(self.get_max_value(season, 'winner'))

            # location of the most number of wins for the top team
            match = Match.objects.filter(season=season, winner=max_winner).values_list('city', flat=True)
            match_winner = self.get_list_from_query_set(match)
            winner_location.append(max(match_winner, key=match_winner.count))

            # % of teams decided to bat when they won the toss
            match = Match.objects.filter(season=season)
            match_count = match.count()
            match_count_for_bat = Match.objects.filter(season=season, toss_decision='bat').count()
            bat_decided_per.append((match_count_for_bat/match_count)*100)

            # team won by the highest margin of runs  for the season
            teams = match.values_list('team1', flat=True).distinct()
            winning_team_dict = {}
            for team in teams:
                winning_team_runs_list = match.filter(winner=team).values_list('win_by_runs', flat=True)
                winning_team_dict[team] = sum(winning_team_runs_list)
            winner_with_large_runs.append(max(winning_team_dict, key=winning_team_dict.get))

            # location hosted most number of matches and win % and loss % for the season
            location_with_matches.append(self.get_max_value(season, 'city'))

        context['seasons'] = self.get_list_from_query_set(seasons)
        context['seasons_winners'] = seasons_winners
        context['winners'] = winner_dict
        context['max_toss_winner'] = toss_winner_list
        context['player_of_match'] = player_of_match
        context['winner_location'] = winner_location
        context['bat_decided_per'] = bat_decided_per
        context['winner_with_large_runs'] = winner_with_large_runs
        context['location_with_matches'] = location_with_matches
        return self.render_to_response(context)

    def get_list_from_query_set(self, query_set):
        req_list = []
        for val in query_set:
            req_list.append(val)
        return req_list

    def get_max_value(self, season, val_list_content):
        match = Match.objects.filter(season=season).values_list(val_list_content, flat=True)
        match_winner = self.get_list_from_query_set(match)
        return max(match_winner, key=match_winner.count)