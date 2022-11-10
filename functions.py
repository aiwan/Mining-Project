import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def make_request(url):
    """

    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

def parse_content(url_response):
    """
    """
    soup = BeautifulSoup(url_response.content, "html.parser")
    teams = soup.select("span.team-name")
    teams_list = []
    for team in teams:
        #for data in match:
            #print("type data: ", type(data))
            #soup = BeautifulSoup(data, "html.parser")
            #team_name = soup.find_all("span", class_="team-name")
            #print(team.text)
        teams_list.append(team.text)
        # home_team = match.find("div", class_="team-home").text
        # away_team = match.find("div", class_="team-away").text
        #matches_list.append([home_team, away_team])
    # print(matches_list)
    # print(f"matches_list length: {len(matches_list)}")
    return teams_list
