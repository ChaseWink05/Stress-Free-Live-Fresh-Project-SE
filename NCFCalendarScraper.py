import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

class NCFCalendarScraper:
    def __init__(self, url="https://www.ncf.edu/academics/academic-calendar/"):
        self.url = url
        self.academic_events = []

    def fetch_calendar(self):
        """Fetches the NCF academic calendar with a user-agent header."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        try:
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            tables = soup.find_all("table")
            for table in tables:
                rows = table.find_all("tr")
                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) == 2:
                        date = cols[0].text.strip()
                        event = cols[1].text.strip()
                        self.academic_events.append({"date": date, "event": event})

            return self.academic_events
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the calendar: {e}")
            return []

    def get_dataframe(self):
        """Returns the scraped academic calendar as a DataFrame."""
        return pd.DataFrame(self.academic_events)

def scraper_page():
    st.title("📅 NCF Academic Calendar Scraper")
    st.write("Click the button below to fetch academic events from NCF.")

    scraper = NCFCalendarScraper()

    if st.button("Scrape NCF Calendar"):
        events = scraper.fetch_calendar()
        if events:
            df = scraper.get_dataframe()
            st.success(f"Successfully scraped {len(events)} events!")
            st.write(df)

            # Button to add events to the calendar
            if st.button("Add Events to Calendar"):
                if "calendar_events" not in st.session_state:
                    st.session_state["calendar_events"] = []

                # Convert events into calendar format and store in session state
                for event in events:
                    event_data = {
                        "title": event["event"],
                        "start": event["date"],
                        "end": event["date"]
                    }
                    if event_data not in st.session_state["calendar_events"]:
                        st.session_state["calendar_events"].append(event_data)

                st.success("Events added to your calendar! Go to the Dashboard to see them.")
        else:
            st.warning("No events found. Please try again later.")
