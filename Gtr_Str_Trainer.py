from pygame import mixer
import random

mixer.init()

str_library = {
    "a_str" : "Audio_Clips/A_Str.wav",
    "b_str" : "Audio_Clips/B_Str.wav",
    "d_str" : "Audio_Clips/D_Str.wav",
    "g_str" : "Audio_Clips/G_Str.wav",
    "up_e_str" : "Audio_Clips/Up_E_Str.wav",
    "low_e_str" : "Audio_Clips/Low_e_Str.wav"
}



def play_audio(path):
    # mixer.Sound(path) # loads music from Audio_Clips folder
    # mixer.Sound.play() # plays music

    mixer.music.load(path) # loads music from Audio_Clips folder
    mixer.music.play() # plays music


# Testing for six round mode where each guitar string is rndmly played and guessed once
# all 6 strings r guessed then game end, NO REPEAT
rounds = len(str_library)

for round_num in range (1, rounds + 1):
    print ("Round " + str(round_num) + ":")

    for index in range(round_num):
        if index < len(str_library):
            print("Working")


ran_num_gen = random.randint(1,6)

if ran_num_gen == 1:
    gtr_str_guess = "A"
    gtr_str_audio = str_library["a_str"]
    
elif ran_num_gen == 2:
    gtr_str_guess = "B"
    gtr_str_audio = str_library["b_str"]

elif ran_num_gen == 3:
    gtr_str_guess = "D"
    gtr_str_audio = str_library["d_str"]

elif ran_num_gen == 4:
    gtr_str_guess = "G"
    gtr_str_audio = str_library["g_str"]

elif ran_num_gen == 5:
    gtr_str_guess = "E"
    gtr_str_audio = str_library["up_e_str"]

elif ran_num_gen == 6:
    gtr_str_guess = "e"
    gtr_str_audio = str_library["low_e_str"]

print("Guess the Guitar string \nPress ""r"" to replay the string, press ""q"" to quit \nChoices: ""A"","" B"","" D"","" E"","" G"","" low e""")

play_audio(gtr_str_audio)

while True:
    user_guess = input("User Guess: ").strip().lower()
    if user_guess == gtr_str_guess.lower():
        print("Correct")
        break
    elif user_guess == "r":
        play_audio(gtr_str_audio)
    elif user_guess == "q":
        print("Quitting")
        break
    else:
        print("Guess Again")