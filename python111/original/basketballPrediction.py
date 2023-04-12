from pyvizml import CreateNBAData




cnd = CreateNBAData(2019)
player_stats = cnd.create_player_stats_df()