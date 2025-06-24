import sys
sys.path.append('d:/JARVIS-V1.0')
from Engine.TTS import TTS
try:
    import webbrowser
    import wikipedia
except ModuleNotFoundError:
    import subprocess
    subprocess.run("pip install wikipedia")
    import wikipedia

from Engine.TTS import TTS
def get_answer(text):
    try:
        return wikipedia.summary(text,sentences=1)
    except Exception:
        TTS("Searching about your request sir")
        webbrowser.open(f"https://www.google.com/search?q={text}")
        TTS(f"You can see the search result about {text} in your screen")
        
import pywhatkit as kt    
import datetime
import time
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
tasks = []


def send_email(subject, body, to_email):
    from_email = "ujjwalchauhan671@gmail.com"  
    from_password = "pvnx ejmv jpav mfld"  
    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    # Create the email
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    # Send the email
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()
    print("Email sent successfully!")
    
# Add a task to the schedule
def add_task():
    try:
        TTS("What is the task, sir?")
        task_name = input("Task: ").strip()
        
        if "send email" in task_name.lower():
            TTS("Please provide the recipient's email address, sir.")
            to_email = input("Recipient's email: ").strip()
            TTS("What should the email contain, sir?")
            email_body = input("Email body: ").strip()
            TTS("When should the email be sent, sir? Please provide the time in 'YYYY-MM-DD HH:MM' format.")
            due_time = input("Due time (YYYY-MM-DD HH:MM): ").strip()
            due_datetime = datetime.datetime.strptime(due_time, "%Y-%m-%d %H:%M")
            
            tasks.append({
                "name": "Send Email",
                "time": due_datetime,
                "email": to_email,
                "body": email_body
            })
            TTS(f"Email task added for {due_datetime.strftime('%A, %B %d, %Y at %I:%M %p')}, sir.")
        else:
            TTS("When is the task due, sir? Please provide the time in 'YYYY-MM-DD HH:MM' format.")
            due_time = input("Due time (YYYY-MM-DD HH:MM): ").strip()
            due_datetime = datetime.datetime.strptime(due_time, "%Y-%m-%d %H:%M")
        
            tasks.append({"name": task_name, "time": due_datetime})
            TTS(f"Task '{task_name}' added for {due_datetime.strftime('%A, %B %d, %Y at %I:%M %p')}, sir.")
    except ValueError:
        TTS("The time format seems incorrect, sir. Please try again.")
    except Exception as e:
        TTS(f"An unexpected error occurred: {str(e)}")

# Show all scheduled tasks
def show_tasks():
    if not tasks:
        TTS("You have no tasks scheduled, sir.")
    else:
        TTS("Here are your scheduled tasks, sir:")
        for i, task in enumerate(sorted(tasks, key=lambda x: x["time"]), 1):
            task_time = task["time"].strftime("%A, %B %d, %Y at %I:%M %p")
            TTS(f"{i}. {task['name']} at {task_time}")

# Reminder for upcoming tasks
def task_reminder():
    while True:
        now = datetime.datetime.now()
        for task in tasks[:]:  
            if now >= task["time"]:
                TTS(f"Sir, it's time for your task: {task['name']}.")
                try:
                    if "play" in task["name"].lower():
                        song_name = task["name"].replace("play", "").strip()
                        TTS(f"Playing {song_name} for you, sir.")
                        kt.playonyt(song_name)
                
                    elif task["name"].lower() == "send email":
                        to_email = task["email"]
                        body = task["body"]
                        subject = "Automated Task Email"
                        send_email(subject, body, to_email)
                        TTS(f"Email sent to {to_email} regarding the task.")
                except Exception as e:
                    TTS(f"An error occurred while handling the task: {e}")
                finally:
                    tasks.remove(task)
        time.sleep(10) 
        

# Start the reminder service
def start_reminder():
    TTS("Task reminder service started, sir.")
    reminder_thread = threading.Thread(target=task_reminder, daemon=True)
    reminder_thread.start()


import requests

def get_news(country=None, topic=None, api_key="b94029726e094d339888ba6dc07f0cd1"):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
    }
    
    if country:
        params["country"] = country
    
    if topic:
        params["q"] = topic
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        news_data = response.json()
        
        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])
            if articles:
                headlines = [
                    f"{i + 1}. {article['title']} ({article['source']['name']})"
                    for i, article in enumerate(articles[:3])
                ]
                return "\n".join(headlines)
            else:
                return "No news articles found for your request."
        else:
            return f"Error fetching news: {news_data.get('message', 'Unknown error')}"
    except requests.RequestException as e:
        return f"Failed to fetch news: {str(e)}"


import os
def open_app(app_name):
    try:
        apps = {
            "notepad": r"C:\Windows\notepad.exe",
            "calculator": r"C:\Windows\System32\calc.exe",
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "report": r"C:\Users\ASUS\Downloads\Ujjwal_CSE_MINI_PROJECT_Report2.docx",
            "vs code":r"C:\Users\ASUS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
        }
        # Check if the app is in the dictionary
        if app_name.lower() in apps:
            app_path = apps[app_name.lower()]
            TTS(f"Opening {app_name}, sir.")
            os.startfile(app_path)
        else:
            TTS(f"Sorry, I couldn't find {app_name} in the list of available applications, sir.")
    except Exception as e:
        TTS(f"An error occurred while trying to open {app_name}: {str(e)}")
