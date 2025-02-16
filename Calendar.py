import streamlit as st
from streamlit_calendar import calendar
import datetime

def showCalendar():

    st.markdown("## Interactive Calendar with Event Input 📆")

    # Ensure session state contains an event list
    st.session_state.setdefault("events", [])

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
                "title": title,
                "color": color,
                "start": f"{start_date}T{start_time}",
                "end": f"{end_date}T{end_time}",
                "resourceId": resource_id,
            }
            st.session_state["events"].append(new_event)
            st.success(f"Event '{title}' added!")
            st.experimental_rerun()  # This will trigger a page refresh

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

    if "resource" in mode:
        if mode == "resource-daygrid":
            calendar_options.update({
                "initialDate": str(datetime.date.today()),
                "initialView": "resourceDayGridDay",
                "resourceGroupField": "building",
            })
        elif mode == "resource-timeline":
            calendar_options.update({
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
                },
                "initialDate": str(datetime.date.today()),
                "initialView": "resourceTimelineDay",
                "resourceGroupField": "building",
            })
        elif mode == "resource-timegrid":
            calendar_options.update({
                "initialDate": str(datetime.date.today()),
                "initialView": "resourceTimeGridDay",
                "resourceGroupField": "building",
            })
    else:
        if mode == "daygrid":
            calendar_options.update({
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": str(datetime.date.today()),
                "initialView": "dayGridMonth",
            })
        elif mode == "timegrid":
            calendar_options.update({"initialView": "timeGridWeek"})
        elif mode == "timeline":
            calendar_options.update({
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "timelineDay,timelineWeek,timelineMonth",
                },
                "initialDate": str(datetime.date.today()),
                "initialView": "timelineMonth",
            })
        elif mode == "list":
            calendar_options.update({
                "initialDate": str(datetime.date.today()),
                "initialView": "listMonth",
            })
        elif mode == "multimonth":
            calendar_options.update({"initialView": "multiMonthYear"})

    # Display calendar with user-inputted events
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
        if isinstance(state["eventsSet"], list):  # Ensure correct type
            st.session_state["events"] = state["eventsSet"]

    st.write(state)
