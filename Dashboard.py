import streamlit as st
import random
import ToDoList
from Timer import Timer
from streamlit_calendar import calendar
from NCFCalendarScraper import scraper_page  # Import scraper page

def main():
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
        timer = Timer()

        # Sidebar Timer Controls
        minutes = st.sidebar.number_input("Set Timer (minutes)", min_value=1, max_value=60, value=5)
        start_button = st.sidebar.button("Start Timer")
        stop_button = st.sidebar.button("Stop Timer")

        # Start Timer
        if start_button and not st.session_state.timer_running:
            timer.start_timer(minutes)
            timer.display_timer()

        # Stop Timer
        if stop_button:
            timer.stop_timer()

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
