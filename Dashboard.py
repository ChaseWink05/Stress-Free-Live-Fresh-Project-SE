import streamlit as st
import random
import ToDoList
from Timer import timer
from streamlit_calendar import calendar
from NCFCalendarScraper import scraper_page  # Import scraper page

<<<<<<< Updated upstream
def main():
    st.set_page_config(page_title="Student Dashboard", layout="wide")
=======
    # Streamlit App
    #st.set_page_config(page_title="Student Dashboard", layout="wide")
>>>>>>> Stashed changes

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Scheduler", "To-Do List", "NCF Website Scraper", "Magic Wand"])

    if page == "Dashboard":
        st.title("📌 Student Dashboard")
        st.write("Welcome to your student dashboard! Here you can see your upcoming events and tasks at a glance.")

        # Display upcoming events
        st.subheader("📅 Upcoming Events")
        if "calendar_events" in st.session_state and st.session_state["calendar_events"]:
            for event in st.session_state["calendar_events"]:
                st.write(f"**{event['start']}** - {event['title']}")
        else:
            st.write("No upcoming events.")

        # Display Calendar
        st.subheader("📆 Calendar")
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
        }

        # Load events from session state
        if "calendar_events" not in st.session_state:
            st.session_state["calendar_events"] = []

        # Display the calendar
        calendar(events=st.session_state["calendar_events"], options=calendar_options, key="calendar")

        # Display To-Do List
        st.subheader("✅ To-Do List")
        todo = ToDoList.todo()
        todo.display_tasks("Important")

    elif page == "Scheduler":
        st.title("📅 Scheduler")
        st.write("Here you can manage your class schedule and deadlines.")

    elif page == "To-Do List":
        st.title("✅ To-Do List")
        st.write("Manage your tasks and keep track of what needs to be done.")

        todo = ToDoList.todo()
        col1, col2, col3, col4 = st.columns(4)

        # Timer integration
        minutes = st.sidebar.number_input("Set a timer (minutes)", min_value=0, max_value=60)
        Timer = timer()
        if st.sidebar.button("Start Timer"):
            Timer.countdown(minutes)
        if st.sidebar.button("End Timer"):
            st.sidebar.write(f"Timer ended. Total time: {Timer.stop()} seconds")

        with col1:
            st.header("Create")
            userInput = st.text_input("Enter a task")
            label = st.selectbox("Label", ["In Progress", "Important", "Done"])
            if st.button("Add Task"):
                todo.add_task(userInput, label)
        with col2:
            st.header("Doing")
            todo.display_tasks("In Progress")
        with col3:
            st.header("IMPORTANT")
            todo.display_tasks("Important")
        with col4:
            st.header("Done")
            todo.display_tasks("Done")

    elif page == "NCF Website Scraper":
        scraper_page()  # Load the scraper page

if __name__ == "__main__":
    main()
