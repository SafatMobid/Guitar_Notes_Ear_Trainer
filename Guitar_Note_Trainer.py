import os
# from playsound import playsound #issue installing playsound (not compatiable with newer version of python)

#print(os.getcwd()) #shows my directory

file_path = os.path.abspath("Audio_Clips/A_Note.mp3")
os.startfile(file_path)
