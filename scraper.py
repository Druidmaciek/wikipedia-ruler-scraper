from typing import List

import requests
from bs4 import BeautifulSoup


def make_request(url: str) -> str:
    """ Makes a HTTP GET Request.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def scrape_ruler(url: str) -> dict:
    """Parse Wikipedia ruler page for data."""
    content = make_request(url)
    soup = BeautifulSoup(content, "html.parser")
    data_table = soup.find("table", {"class": "infobox vcard"})
    table_rows = data_table.find_all("tr")
    data_rows = [row for row in table_rows if row.find('th') and row.find('td')]
    data = {x.find("th").text: x.find("td").text.strip() for x in data_rows}
    data["Ruler"] = data_table.find("tr").text
    return data


def scrape_rulers(url: str) -> List[dict]:
    """ Scrape all rulers from wikipedia rulers page """
    content = make_request(url)
    soup = BeautifulSoup(content, "html.parser")
    ruler_urls = ["https://en.wikipedia.org" + x.find("a")["href"] for x in soup.find_all('big') if x.find('a')]
    return [scrape_ruler(ruler_url) for ruler_url in ruler_urls]
