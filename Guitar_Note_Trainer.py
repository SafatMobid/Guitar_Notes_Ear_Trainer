import os
from playsound3 import playsound

# #print(os.getcwd()) #shows my directory

# a_note = os.path.abspath("Audio_Clips/A_Note.mp3")
# #file_path = os.path.abspath("Audio_Clips/B_Note.mp3")
# os.startfile(a_note)

audio_folder = os.path.join(os.path.dirname(__file__), "Audio_Clips")

a_note = os.path.join(audio_folder, "A_Note.mp3")


playsound(a_note)