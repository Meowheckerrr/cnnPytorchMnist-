
import requests
import pandas as pd


class CreateNBAData:
    """
    This class scrapes NBA.com offical api: data.nba.net.
    See https://data.nba.net/10s/prod/v1/today.json
    Args:
        season_year (int): Use the first year to specify season, e.g. specify 2019 for the 2019-2020 season.
    """
    def __init__(self, season_year):
        self._season_year = str(season_year)

    def create_players_df(self):
        """
        This function returns the DataFrame of player information.
        """
        request_url = "https://data.nba.net/prod/v1/{}/players.json".format(self._season_year)
        players_list = resp_dict['league']['standard']
        players_list_dict = []
        print("Creating players df...")
        for p in players_list:
            player_dict = {}
            for k, v in p.items():
                if isinstance(v, str) or isinstance(v, bool):
                    player_dict[k] = v
            players_list_dict.append(player_dict)
        df = pd.DataFrame(players_list_dict)
        filtered_df = df[(df['isActive']) & (df['heightMeters'] != '')]
        filtered_df = filtered_df.reset_index(drop=True)
        self._person_ids = filtered_df['personId'].values
        return filtered_df

    def create_stats_df(self):
        """
        This function returns the DataFrame of player career statistics.
        """
        self.create_players_df()
        career_summaries = []
        print("Creating player stats df...")
        for pid in self._person_ids:
            request_url = "https://data.nba.net/prod/v1/{}/players/{}_profile.json".format(self._season_year, pid)
            response = requests.get(request_url)
            profile_json = response.json()
            career_summary = profile_json['league']['standard']['stats']['careerSummary']
            career_summaries.append(career_summary)
        stats_df = pd.DataFrame(career_summaries)
        stats_df.insert(0, 'personId', self._person_ids)
        return stats_df
    
    def create_player_stats_df(self):
        """
        This function returns the DataFrame merged from players_df and stats_df.
        """
        players = self.create_players_df()
        stats = self.create_stats_df()
        player_stats = pd.merge(players, stats, left_on='personId', right_on='personId')
        return player_stats