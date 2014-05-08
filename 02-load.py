import json

import dataset
import requests
import pyquery

URL = "https://www.crtmoorings.com/auctions/search.php"

engine = dataset.connect('sqlite:///moorings.db')

def get_mooring_details(heading):
    mooring = {}
    mooring["Title"] = heading.text()
    details = heading.next()
    mooring["Image URL"] = details(".vacancy_main_img a img").attr("src")

    # For each paragraph element in the vacancy_details divs
    for d in details.find(".vacancy_details p").items():
        # If the paragraph element has a child "strong" element
        if d.find("strong").length > 0:
            # Split the text on the first colon
            key, val = d.text().split(":", 1)
            # Trim any whitespace
            key, val = key.strip(), val.strip()
            # Put the details in the dict
            mooring[key] = val

    return mooring


def scrape(url):
    auctions = engine['auctions']

    # Extract
    response = requests.get(url)
    document = pyquery.PyQuery(response.content)

    # Transform
    headings = document.find("h3.vacancy_summary")
    for h in headings.items():
        mooring = get_mooring_details(h)

        # Load
        auctions.insert(mooring)

    # Confirm what we've got
    print("%d rows in auctions table" % len(auctions))


if __name__ == "__main__":
    scrape(URL)
