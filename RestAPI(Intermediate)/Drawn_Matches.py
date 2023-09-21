import requests


def getData(url: str):
    respose = requests.get(url)
    data = respose.json()
    return data


def getNumDraws():
    year = 2012
    total_draws = 0

    for goals in range(0, 11):
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={goals}&team2goals={goals}"
        data = getData(url)
        total_draws += data['total']

        print(total_draws, data['total'])

    return total_draws


if __name__ == "__main__":
    print(f"Total draws: {getNumDraws()}")