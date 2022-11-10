"""
# Data Mining Project
# Web Scraper of Goal.com

Skills:
-Make requests using the most common HTTP methods
-Customize your requests’ headers and data, using the query string and message body
-Inspect data from your requests and responses
-Make authenticated requests
-Configure your requests to help prevent your application from backing up or slowing down

-Inspect the HTML structure of your target site with your browser’s developer tools
-Decipher data encoded in URLs
-Use requests and Beautiful Soup for scraping and parsing data from the Web
-Step through a web scraping pipeline from start to finish
-Build a script that fetches job offers from the Web and displays relevant information in your console
"""
# Imports
import functions
from functions import *
from datetime import date, timedelta


def main():
    """
    Main function, controls the general logic.
    :return:
    """
    base_url = "https://www.goal.com/en/results/"
    dynamic_url = "2022-11-01"
    first_date = date(2022, 11, 1)
    url = base_url + dynamic_url
    url_response = make_request(url)
    duration = timedelta(days=9)
    for d in range(duration.days + 1):
        day = first_date + timedelta(days=d)
        dynamic_url = day
        url = base_url + str(day)
        print(url)
        url_response = make_request(url)
        teams = parse_content(url_response)
        print(teams)
    pass



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
