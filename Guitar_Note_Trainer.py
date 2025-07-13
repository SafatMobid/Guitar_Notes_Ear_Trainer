import os
from playsound import playsound

#print(os.getcwd()) #shows my directory

file_path = os.path.abspath("Audio_Clips/A_Note.mp3")
#file_path = os.path.abspath("Audio_Clips/B_Note.mp3")
os.startfile(file_path)
