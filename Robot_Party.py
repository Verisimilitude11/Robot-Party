#### ---- INPUT ---- ####

# Ask "How many people are here? ", typecast to an int,
# and assign to the variable people
people = int(input("How many people are here? "))

# Ask "Is the music loud or soft? l/s " and assign to
# the variable music
music = input("Is the music loud or soft? l/s ")

# Ask "Does someone want to dance with you? y/n " and
# assign to the variable dance
dance = input("Does someone want to dance with you? y/n ")


#### ---- ROBOT RULES ---- ####

# IF people is GREATER THAN 3 AND music is EQUAL TO "s"
if people > 3 and music == "s":

    # Print "Turn the music up."
    print("Turn the music up.")

# ELIF people is LESS THAN 4 AND music is EQUAL TO "l"
elif people < 4 and music == "1":

    # PRINT "Turn the music down."
    print("Turn the music down.")

# ELIF music is EQUAL TO "l" OR dance is EQUAL TO "y"
elif music == "1" or dance == "y":

    # Print "Bust a groove!" (or similar dance message)
    print("Bust a groove!")

# ELSE
else:

    # Print "Chat with guests."
    print("Chat with guests.")
