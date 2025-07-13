# import os
from playsound3 import playsound
import random

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

# playsound(a_note)
# playsound(b_note)
# playsound(d_note)
# playsound(e_note)
# playsound(g_note)
# playsound(low_e_note)

ran_num_gen = random.randint(1,6)

if ran_num_gen == 1:
    note_name = "A"
    note_audio = a_note

elif ran_num_gen == 2:
    note_name = "B"
    note_audio = b_note

elif ran_num_gen == 3:
    note_name = "D"
    note_audio = d_note

elif ran_num_gen == 4:
    note_name = "E"
    note_audio = e_note

elif ran_num_gen == 5:
    note_name = "G"
    note_audio = g_note

elif ran_num_gen == 6:
    note_name = "Low_E"
    note_audio = low_e_note

playsound(note_audio)