#This acts as the main page of the app, where the user can see their upcoming events and tasks at a glance.
import streamlit as st
import random
import ToDoList
def main():
    # Sample data
    schedule = [
        {"date": "2025-03-01", "event": "Midterm Exam"},
        {"date": "2025-04-15", "event": "Project Deadline"}
    ]

    # Streamlit App
    st.set_page_config(page_title="Student Dashboard", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Scheduler", "To-Do List", "Magic Wand"])

    if page == "Dashboard":
        st.title("📌 Student Dashboard")
        st.write("Welcome to your student dashboard! Here you can see your upcoming events and tasks at a glance.")

        # Display schedule
        st.subheader("📅 Upcoming Events")
        for event in schedule:
            st.write(f"**{event['date']}** - {event['event']}")

        # Display To-Do List
        st.subheader("✅ To-Do List")
        todo = ToDoList.todo()
        todo.display_tasks("Important")

    elif page == "Scheduler":
        st.title("📅 Scheduler")
        st.write("Here you can manage your class schedule and deadlines.")
        # Placeholder for scheduler functionality

    elif page == "To-Do List":
        st.title("✅ To-Do List")
        st.write("Manage your tasks and keep track of what needs to be done.")
        # Placeholder for To-Do List functionality

        todo = ToDoList.todo()
        col1,col2,col3, col4 = st.columns(4)
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

if __name__ == "__main__":
    main()
