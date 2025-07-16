# To use go-to terminal and run python old_Code/playsound_Gtr_Str_Trainer.py

from playsound3 import playsound
import random

a_string = "old_Code/Audio_Clips/A_string.mp3"
b_string = "old_Code/Audio_Clips/B_string.mp3"
d_string = "old_Code/Audio_Clips/D_string.mp3"
e_string = "old_Code/Audio_Clips/Upper_E_string.mp3"
g_string = "old_Code/Audio_Clips/G_string.mp3"
low_e_string = "old_Code/Audio_Clips/Lower_e_string.mp3"

ran_num_gen = random.randint(1,6)

if ran_num_gen == 1:
    string_name = "A"
    string_audio = a_string
    
elif ran_num_gen == 2:
    string_name = "B"
    string_audio = b_string

elif ran_num_gen == 3:
    string_name = "D"
    string_audio = d_string

elif ran_num_gen == 4:
    string_name = "E"
    string_audio = e_string

elif ran_num_gen == 5:
    string_name = "G"
    string_audio = g_string

elif ran_num_gen == 6:
    string_name = "Low E"
    string_audio = low_e_string

print("Guess the Guitar string \nPress ""r"" to replay the string, press ""q"" to quit \nChoices: ""A"","" B"","" D"","" E"","" G"","" low e""")
playsound(string_audio)
# print(string_name)
while True:
    guess = input("User guess: ").strip().lower()
    if guess == string_name.lower():
        print("Correct")
        break
    elif guess == "r":
        playsound(string_audio)
    elif guess == "q":
        print("Quitting")
        break
    else:
        print("Guess again")

