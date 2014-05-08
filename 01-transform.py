import json

import requests
import pyquery

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

# Extract
response = requests.get("https://www.crtmoorings.com/auctions/search.php")
document = pyquery.PyQuery(response.content)

# Transform
headings = document.find("h3.vacancy_summary")
for h in headings.items():
    mooring = get_mooring_details(h)
    print json.dumps(mooring, indent=2)
