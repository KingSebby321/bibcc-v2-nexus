import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_industry_events(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        events = []

        # Example: look for all <a> tags with class "event-link" (adjust based on actual site structure)
        for item in soup.find_all('a', class_='event-link'):
            title = item.get_text(strip=True)
            link = item.get('href')
            if title and link:
                events.append({'title': title, 'link': link})

        df = pd.DataFrame(events)
        print(f"Scraped {len(df)} events from {url}")
        return df

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage:
# df = scrape_industry_events("https://example.com/events")
# df.to_csv("scraped_events.csv", index=False)