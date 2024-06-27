from gtts import gTTS
import os
mytxt="Welcome to Python. Have a wonderful experience."
language="en"
myobj = gTTS(text=mytxt,lang=language,slow=False)
myobj.save("Pythonintro.mp3")

os.system("Pythonintro.mp3")
