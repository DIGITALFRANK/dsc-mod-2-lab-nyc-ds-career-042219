import seaborn as sns

class MongoHandler():


    def get_teams(self, df):
        teams = df.HomeTeam.append(df.AwayTeam)
        unique_teams = set(teams)
        return list(unique_teams)


    def total_wins(self, df, team, wins = []):
        for unique_team in df.Unique_Team:
            for n in range(len(df.Unique_Team)):
                if team == df.HomeTeam[n] and df.FTR[n] == 'H':
                    wins.append(1)
                elif team == df.AwayTeam[n] and df.FTR[n] == 'A':
                    wins.append(1)
            # print(wins)
        return sum(wins)


    def total_goals(self, df, team, goals = []):
        for unique_team in df.Unique_Team:
            for n in range(len(df.Unique_Team)):
                if team == df.HomeTeam[n]:
                    goals.append(df.FTHG[n])
                elif team == df.AwayTeam[n]:
                    goals.append(df.FTAG[n])
            # print(goals)
        return sum(goals)


    def total_losses(self, df, team, losses = []):
        for unique_team in df.Unique_Team:
            for n in range(len(df.Unique_Team)):
                if team == df.HomeTeam[n] and df.FTR[n] == 'A':
                    losses.append(1)
                elif team == df.AwayTeam[n] and df.FTR[n] == 'H':
                    losses.append(1)
            # print(losses)
        return sum(losses)


    def plot_hist(self, team):
        wins_losses = [self.total_wins(team), self.total_loses(team)]
        sns.distplot(wins_losses, kde = False)


    def create_hist():
        pass

