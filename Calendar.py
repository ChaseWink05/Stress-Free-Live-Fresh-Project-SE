import streamlit as st
from streamlit_calendar import calendar
import datetime
import uuid

def showCalendar():

    st.markdown("## Interactive Calendar with Event Input 📆")

    # Ensure session state contains an event list
    if "events" not in st.session_state:
        st.session_state["events"] = []

    # Ensure session state contains a selected event
    if "selected_event" not in st.session_state:
        st.session_state["selected_event"] = None

    # Calendar mode selection
    mode = st.selectbox(
        "Calendar Mode:",
        (
            "daygrid",
            "timegrid",
            "timeline",
            "resource-daygrid",
            "resource-timegrid",
            "resource-timeline",
            "list",
            "multimonth",
        ),
    )

    # Event input form
    with st.form("event_form"):
        st.write("### Add a New Event")

        title = st.text_input("Event Title")
        color = st.color_picker("Pick a Color", "#FF6C6C")
        start_date = st.date_input("Start Date", datetime.date.today())
        end_date = st.date_input("End Date", datetime.date.today())
        start_time = st.time_input("Start Time", datetime.time(9, 0))
        end_time = st.time_input("End Time", datetime.time(10, 0))
        resource_id = st.selectbox(
            "Resource ID", ["a", "b", "c", "d", "e", "f"], index=0
        )

        submitted = st.form_submit_button("Add Event")

        if submitted:
            new_event = {
                "id": str(uuid.uuid4()),  # Add unique id
                "title": title,
                "color": color,
                "start": f"{start_date}T{start_time}",
                "end": f"{end_date}T{end_time}",
                "resourceId": resource_id,
            }
            if new_event not in st.session_state["events"] and new_event["title"]:
                st.session_state["events"].append(new_event)
                st.success(f"✅ Event '{title}' added!")

    # Calendar resources
    calendar_resources = [
        {"id": "a", "building": "Building A", "title": "Room A"},
        {"id": "b", "building": "Building A", "title": "Room B"},
        {"id": "c", "building": "Building B", "title": "Room C"},
        {"id": "d", "building": "Building B", "title": "Room D"},
        {"id": "e", "building": "Building C", "title": "Room E"},
        {"id": "f", "building": "Building C", "title": "Room F"},
    ]

    # Calendar options
    calendar_options = {
        "editable": True,
        "navLinks": True,
        "resources": calendar_resources,
        "selectable": True,
    }

    # Display calendar with user-inputted & scraped events
    state = calendar(
        events=st.session_state["events"],
        options=calendar_options,
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
        """,
        key=mode,
    )

    # Update session state when events are modified in the UI
    if state.get("eventsSet") is not None:
        if isinstance(state["eventsSet"], list):
            st.session_state["events"] = state["eventsSet"]

    # Handle event click
    if state.get("eventClick") is not None:
        event_id = state["eventClick"]["event"]["id"]
        st.session_state["selected_event"] = next(
            (event for event in st.session_state["events"] if event["id"] == event_id), None
        )

    # Edit or delete selected event
    if st.session_state["selected_event"]:
        with st.form("edit_event_form"):
            st.write("### Edit Event")

            title = st.text_input("Event Title", st.session_state["selected_event"]["title"])
            color = st.color_picker("Pick a Color", st.session_state["selected_event"]["color"])
            start_date = st.date_input("Start Date", datetime.date.fromisoformat(st.session_state["selected_event"]["start"].split("T")[0]))
            end_date = st.date_input("End Date", datetime.date.fromisoformat(st.session_state["selected_event"]["end"].split("T")[0]))
            start_time = st.time_input("Start Time", datetime.time.fromisoformat(st.session_state["selected_event"]["start"].split("T")[1]))
            end_time = st.time_input("End Time", datetime.time.fromisoformat(st.session_state["selected_event"]["end"].split("T")[1]))
            resource_id = st.selectbox(
                "Resource ID", ["a", "b", "c", "d", "e", "f"], index=["a", "b", "c", "d", "e", "f"].index(st.session_state["selected_event"]["resourceId"])
            )

            update_submitted = st.form_submit_button("Update Event")
            delete_submitted = st.form_submit_button("Delete Event")

            if update_submitted:
                st.session_state["selected_event"].update({
                    "title": title,
                    "color": color,
                    "start": f"{start_date}T{start_time}",
                    "end": f"{end_date}T{end_time}",
                    "resourceId": resource_id,
                })
                st.success(f"✅ Event '{title}' updated!")
                st.session_state["selected_event"] = None

            if delete_submitted:
                st.session_state["events"].remove(st.session_state["selected_event"])
                st.success(f"✅ Event '{title}' deleted!")
                st.session_state["selected_event"] = None