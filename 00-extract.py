import requests
import pyquery

# Extract
response = requests.get("https://www.crtmoorings.com/auctions/search.php")
document = pyquery.PyQuery(response.content)

# Transform
headings = document.find("h3.vacancy_suummary")
for h in heading.items():
    print h.text()
