try:
    import pyttsx3
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install pyttsx3')
    import pyttsx3
def TTS(text):
    E=pyttsx3.init()
    E.setProperty('rate',125)
    v=E.getProperty('voices')
    E.setProperty('voice', v[0].id)
    E.say(text)
    E.runAndWait()
    