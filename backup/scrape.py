from bs4 import BeautifulSoup
import urllib.request

r = urllib.request.urlopen('https://understat.com/league/EPL').read()
soup = BeautifulSoup(r)
prettysoup = soup.prettify()

with open("EPLpretty.html", "w") as file:
    file.write(str(prettysoup))

# pickle.dump(soup, open("understatEPL.p", "wb"))
# print(soup.prettify())

# soup = pickle.load(open("understatEPL.p", "rb"))

# home_teams = soup.find_all("div", class_="team-home")
# away_teams = soup.find_all("div", class_="team-away")

# print(home_teams)

# print(away_teams)