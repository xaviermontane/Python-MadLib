"""
-------------------------------------------------------------------------------
Name:		mad_lib_assignment.py
Purpose:	a description of your program

Author:		Montane.X

Created:	01/03/2022
------------------------------------------------------------------------------
"""

f = open("story.txt")
story = f.read()
# Opens the .txt file and it's now ready to be printed.

print(
    "\nWelcome to the Mad Lib game - Come up with words to fill in the blanks for the story\n"
)
print("\t\t\t\tTour The Campus\n")
print(story)
# Introduction to the game.
print(" ")
# Empty string for spacing purposes.

name1 = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
fame = input("Enter a famous person name: ")
noun = input("Enter a noun: ")
num = input("Enter a number: ")
adj2 = input("Enter an adjective: ")
plant = input("Enter a plant: ")
place = input("Enter a place: ")
adv = input("Enter an adjective: ")
name2 = input("Enter a name: ")
verb1 = input("Enter a verb: ")
inj = input("Enter an interjection: ")
song = input("Enter a song: ")
adj3 = input("Enter an adjective: ")
adj4 = input("Enter an adjective: ")
plur = input("Enter a plural noun: ")
verb2 = input("Enter a verb: ")
# Variables.

print(" ")
print(
    "Welcome to the University of",
    name1 + ". Our",
    adj1,
    "campus was founded by",
    fame,
    "and built in 1806. We begin at our",
    noun,
    "building.",
    "This building houses",
    num,
    "classrooms. To your left, the",
    adj2,
    "dormitory is visible just beyond the",
    plant + ". Our students come from all over the",
    place,
    "because we",
    adv,
    "accept anyone who applies.\n" + "We will end the tour here at",
    name2,
    "hall which houses the Admissions Office. Feel free to",
    verb1,
    "an application.",
    inj,
    "folks, you're in for a treat! The marching band is practicing our Alma Mater,",
    song + ". Notice how they march in a",
    adj3,
    "formation, it is the signature move of our University.\n"
    + "Financial aid is available to all",
    adj4,
    "applicants. More information is available on our website",
    plur + ".com.",
    "Thank you for",
    verb2,
    "with us today.\n",
)
# Final output, all user inputs are printed and replace the blank spaces.
