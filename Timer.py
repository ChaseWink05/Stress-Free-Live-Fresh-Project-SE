#This class is the timer class that handles
import time
import streamlit as st


class timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0



    def countdown(self, minutes):
        total_seconds = minutes * 60
        tempTimer = st.sidebar.empty()
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            tempTimer.write(timer)
            time.sleep(1)
        st.sidebar.write("Time's up!")