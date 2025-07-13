import os
from playsound3 import playsound

# #print(os.getcwd()) #shows my directory

# a_note = os.path.abspath("Audio_Clips/A_Note.mp3")
# #file_path = os.path.abspath("Audio_Clips/B_Note.mp3")
# os.startfile(a_note)

# notes = os.path.join(os.path.dirname(__file__), "Audio_Clips")

# a_note = os.path.join(notes, "A_Note.mp3")
# b_note = os.path.join(notes, "B_Note.mp3")
# d_note = os.path.join(notes, "D_Note.mp3")
# e_note = os.path.join(notes, "Upper_E_Note.mp3")
# g_note = os.path.join(notes, "G_Note.mp3")
# low_e_note = os.path.join(notes, "Lower_e_Note.mp3")

a_note = "Audio_Clips/A_Note.mp3"
b_note = "Audio_Clips/B_Note.mp3"
d_note = "Audio_Clips/D_Note.mp3"
e_note = "Audio_Clips/Upper_E_Note.mp3"
g_note = "Audio_Clips/G_Note.mp3"
low_e_note = "Audio_Clips/Lower_e_Note.mp3"


playsound(a_note)