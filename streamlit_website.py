import streamlit as st
import webbrowser
import subprocess
import os

# Function to start Django server
def start_django():
    django_project_path = "."  # Update this to your Django project path
    os.chdir(django_project_path)
    
    # Run Django server
    subprocess.Popen(["python", "manage.py", "runserver"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Redirect to Django app
st.title("Redirecting to Django Application...")
start_django()
webbrowser.open("http://127.0.0.1:8000")
