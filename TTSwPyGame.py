from gtts import gTTS

# Import pygame for playing the converted audio
import pygame

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks, Abhishek!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome1.mp3")

# Initialize the mixer module
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load("welcome1.mp3")

# Play the loaded mp3 file
pygame.mixer.music.play()