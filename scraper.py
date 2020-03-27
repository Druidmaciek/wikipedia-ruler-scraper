import requests
from bs4 import BeautifulSoup

def make_request(url: str) -> str:
    """ Makes a HTTP GET Request.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    raise Exception(f"Request Failed. Status Code {response.status_code} with URL: {url}")

def scrape_ruler(url: str) -> dict:
    """Parse Wikipedia ruler page for data."""
    content = make_request(url)
    soup = BeautifulSoup(content "html.parser")
    data_table = soup.find("table", {"class": "infobox vcard"})
    table_rows = data_table.find_all("tr")
    data_rows = filter(lambda row: row.find("th") and row.find("td"), table_rows)
    data = {x.find("th").text: x.find("td").text.strip() for x in rows}
    data["Ruler"] = data_table.find("tr").text
    return data
