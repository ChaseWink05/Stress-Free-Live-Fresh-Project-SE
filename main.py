import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_calendar import calendar
import Dashboard as DB
<<<<<<< Updated upstream
import ToDoList as TDL

=======
import Calendar

# Set page config as the first Streamlit command
st.set_page_config(page_title="Interactive Calendar", page_icon="📆")

#Test if you can see this
>>>>>>> Stashed changes
DB.main()
TDL.todo()
def example():
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="5",
    )
#example()
<<<<<<< Updated upstream
calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Building A", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}
calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

calendar = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )
st.write(calendar)
=======
Calendar.showCalendar()
>>>>>>> Stashed changes
