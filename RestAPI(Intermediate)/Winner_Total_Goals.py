import requests


def getData(url: str):
    response = requests.get(url)
    data = response.json()
    return data


def getTotalGoalsUtil(url: str, total_pages: int, total_goals: int, is_home_game: int):
    for i in range(1, total_pages + 1):
        page_url = url + f"&page={i}"
        data = getData(page_url)['data']
        for match in data:
            if is_home_game:
                total_goals += int(match["team1goals"])
            else:
                total_goals += int(match["team2goals"])
                
    return total_goals
    

def getTotalGoals(team: str, year: int, competition: str):

    total_goals = 0
    url_team_1 = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team1={team}"
    url_team_2 = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team2={team}"
    
    total_pages_team_1 = getData(url_team_1)["total_pages"]
    total_pages_team_2 = getData(url_team_2)["total_pages"]
        
    total_goals = getTotalGoalsUtil(url_team_1, total_pages_team_1, total_goals, 1)
    total_goals = getTotalGoalsUtil(url_team_2, total_pages_team_2, total_goals, 0)
    
    return total_goals


def getWinnerTotalGoals(competition, year):
    url_winner = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}"
    data = getData(url_winner)["data"][0]
    winning_team = data["winner"]
    total_goals = getTotalGoals(winning_team, year, competition)
    return total_goals


if __name__ == "__main__":
  competition = "UEFA Champions League"
  year = 2011
  print(f"Total goals by winning team: {getWinnerTotalGoals(competition, year)}")