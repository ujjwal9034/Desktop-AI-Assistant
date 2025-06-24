from Engine.STT import STT
from Engine.TTS import TTS
from Brain.Brain import get_answer,get_news
from Brain.Brain import add_task,show_tasks,start_reminder,task_reminder
from Brain.Brain import open_app
import webbrowser
import requests
# Main part of your program
api_key = "b94029726e094d339888ba6dc07f0cd1"  # Replace with your API key
base_url = "https://newsapi.org/v2/top-headlines"
country_code = {
    "us": "us",
    "india": "in",
    "uk": "gb",
    "australia": "au",
    "canada": "ca",
}

try:
    import pywhatkit as kt
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install pywhatkit')
    import pywhatkit as kt

print("Please press the key 1 or 2 to start")
x = int(input())
if x == 1:
    while True:
        text = input("Command: ").lower()
        
        if "jarvis" in text:
            text = text.replace("jarvis", "").strip()
            if "who is" in text:
                text = text.replace("who is", "").strip()
            if "what is" in text:
                text = text.replace("what is", "").strip()
            TTS(get_answer(text))

        if "add task" in text:
            add_task()

        if "show tasks" in text:
            show_tasks()

        if "start reminders" in text:
            start_reminder()

        if "search in youtube" in text:
            query = text.replace("search in youtube", "").strip()
            TTS("Searching about your request, sir.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        if "search in google" in text:
            query = text.replace("search in google", "").strip()
            TTS("Searching about your request, sir.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            TTS(f"You can see the search result about {query} on your screen.")
        
        if "weather" in text:
            query = text.replace("weather", "").strip()
            TTS("Fetching weather information, sir.")
            webbrowser.open(f"https://www.google.com/search?q=weather+{query}")
            TTS(f"The weather in {query} is displayed on your screen.")
            
        if "music on youtube"in text:
             text=text.replace("jarvis","")
             text=text.replace("music on youtube","")
             text=text.replace("play","")
             TTS(f"playing your music {text}")
             kt.playonyt(text)
             TTS('enjoy sir')  
        
        if "open" in text:
            app_name = text.replace("open", "").strip()
            open_app(app_name)
     
             
        if "news in" in text:
            country_name = text.replace("news in", "").strip().lower()
            country = country_code.get(country_name)  # Use the dictionary to get the country code
            if country:
                TTS(f"Fetching the latest news from {country_name.capitalize()}, sir.")
                news = get_news(country=country)
            else:
                news = f"Sorry, I couldn't find news for {country_name}."
            TTS(news)
            print(news)

        elif "news about" in text:
            topic = text.replace("news about", "").strip().lower()
            TTS(f"Fetching the latest news about {topic}, sir.")
            news = get_news(topic=topic)
            TTS(news)
            print(news)


        
elif x == 2:
    while True:
        text = str(STT()).lower()
        
        
        if "jarvis" in text:
            text = text.replace("jarvis", "").strip()
            if "who is" in text:
                text = text.replace("who is", "").strip()
            if "what is" in text:
                text = text.replace("what is", "").strip()
            TTS(get_answer(text))

        if "add task" in text:
            add_task()

        if "show tasks" in text:
            show_tasks()

        if "start reminders" in text:
            start_reminder()

        if "search in youtube" in text:
            query = text.replace("search in youtube", "").strip()
            TTS("Searching about your request, sir.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        if "search in google" in text:
            query = text.replace("search in google", "").strip()
            TTS("Searching about your request, sir.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            TTS(f"You can see the search result about {query} on your screen.")

        if "weather" in text:
            query = text.replace("weather", "").strip()
            TTS("Fetching weather information, sir.")
            webbrowser.open(f"https://www.google.com/search?q=weather+{query}")
            TTS(f"The weather in {query} is displayed on your screen.")
        
        if "music on youtube"in text:
             text=text.replace("jarvis","")
             text=text.replace("music on youtube","")
             text=text.replace("play","")
             TTS(f"playing your music {text}")
             kt.playonyt(text)
             TTS('enjoy sir')  

        if "open" in text:
            app_name = text.replace("open", "").strip()
            open_app(app_name)
            
        if "news in" in text:
            country_name = text.replace("news in", "").strip().lower()
            country = country_code.get(country_name)  # Use the dictionary to get the country code
            if country:
                TTS(f"Fetching the latest news from {country_name.capitalize()}, sir.")
                news = get_news(country=country)
            else:
                news = f"Sorry, I couldn't find news for {country_name}."
            TTS(news)
            print(news)

        elif "news about" in text:
            topic = text.replace("news about", "").strip().lower()
            TTS(f"Fetching the latest news about {topic}, sir.")
            news = get_news(topic=topic)
            TTS(news)
            print(news)