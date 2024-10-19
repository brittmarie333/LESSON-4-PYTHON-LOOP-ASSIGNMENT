#Objective: The aim of this assignment is to deepen your understanding of Python's range() function.
#Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. 
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, 
# loop through every day of the week and for each day, randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood.
#Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
import random
mood = ['happy', 'sad', 'energetic', 'calm']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in weekdays:
    mood = random.choice(mood)
    print(f"On {day}, you were feeling {mood}.")


  