import pygame
import random

pygame.mixer.init()

a_string = "Audio_Clips/A_String.mp3"
b_string = "Audio_Clips/B_String.mp3"
d_string = "Audio_Clips/D_String.mp3"
g_string = "Audio_Clips/G_String.mp3"
e_string = "Audio_Clips/Upper_E_String.mp3"
low_e_string = "Audio_Clips/Lower_e_String.mp3"

def play_audio(path):
    pygame.mixer.music.load(path) # loads music from Audio_Clips folder
    pygame.mixer.music.play() # plays music

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
    string_name = "G"
    string_audio = g_string

elif ran_num_gen == 5:
    string_name = "E"
    string_audio = e_string

elif ran_num_gen == 6:
    string_name = "Low e"
    string_audio = low_e_string

print("Guess the Guitar string \nPress ""r"" to replay the string, press ""q"" to quit \nChoices: ""A"","" B"","" D"","" E"","" G"","" low e""")

play_audio(string_audio)

while True:
    guess = input("User Guess: ").strip().lower()
    if guess == string_name.lower():
        print("Correct")
        break
    elif guess == "r":
        play_audio(string_audio)
    elif guess == "q":
        print("Quitting")
        break
    else:
        print("Guess Again")