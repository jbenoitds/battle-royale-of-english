from gtts import gTTS
from modulesh.voice import speak
import os

# Your input string
text = "Finir au Futur simple; je finis tu finis"


# Extract the first three words
first_three_words = ' '.join(text.split(';')[:1])
remaining_text = ' '.join(text.split(';')[1:]).strip()

speak(first_three_words)

input_text = input('Enter what follows: ')
if input_text == remaining_text:
    print('Yeah!')
else:
    print(remaining_text, input_text)