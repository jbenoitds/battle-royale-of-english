import pyttsx3
# Initialize the pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
### !!! voice: 1 but pb
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
engine.say("je joue a Roblox")
engine.runAndWait()