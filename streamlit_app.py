import subprocess
import os
import streamlit as st

# Path to your Django project directory
django_project_path = "."  # Update this path

# Function to start the Django server
def start_django():
    os.chdir(django_project_path)
    st.write("Starting Django server...")
    # Start Django server
    process = subprocess.Popen(["python", "manage.py", "runserver", "0.0.0.0:8501"])
    return process

# Streamlit UI
st.title("Launching Django Application...")
st.write("Please wait while the Django server starts.")

# Start Django
process = start_django()

st.success("Django server is running! Access your app directly at this Streamlit app URL.")
