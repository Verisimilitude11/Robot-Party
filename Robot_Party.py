people = int(input("How many people are here? "))

music = input("Is the music loud or soft? l/s ")

dance = input("Does someone want to dance with you? y/n ")

if people > 3 and music == "s":

    print("Turn the music up.")

elif people < 4 and music == "1":

    print("Turn the music down.")

elif music == "1" or dance == "y":

    print("Bust a groove!")

else:

    print("Chat with guests.")
