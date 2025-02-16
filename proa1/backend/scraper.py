import requests
from bs4 import BeautifulSoup
import json

def scrape_events():
    url = "https://www.eventbrite.com.au/d/australia--sydney/all-events/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    events = []
    for event in soup.find_all("div", class_="search-event-card-wrapper"):
        title = event.find("div", class_="eds-event-card__formatted-name--is-clamped").text.strip()
        date = event.find("div", class_="eds-text-bs").text.strip()
        link = event.find("a", class_="eds-event-card-content__action-link")["href"]

        events.append({
            "title": title,
            "date": date,
            "link": link
        })

    with open("events.json", "w") as f:
        json.dump(events, f, indent=4)

    return events
