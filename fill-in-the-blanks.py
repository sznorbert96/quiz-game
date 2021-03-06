# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

hard = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
hard_answer = ["function","variables","none","list"]

# The answer for ___1___ is 'function'. Can you figure out the others?
# The answer for ___2___ is "variables".
# The answer for ___3___ is "None"
# The answer for ___4___ is "List"

easy = ''' The ___1___ variable can't be add to the ___2___ "str" ,because before that we need to ___3___  it from "int" to "str". If we want to print out four stars like this "****" we can use this formula: an "str" variable like "*" ___4___ by an "int" variable like "4".'''
easy_answer = ["int","variable","convert","multiply"]

medium = '''In a ___1___ you can store multiple elements in order, and it  can be any type of ___2___. The ___3___ start from 0. You can set the list's elemnts to another ___4___'''
medium_answer = ["list","variable","indexes","list"]

blanks = ["___1___","___2___","___3___","___4___"]

def ask(question,answer):
	"""This procedure takes 2 inputs (the sentense, and the correct answers) depends on diff's value"""
	for x in range(len(answer)):
		print(question)
		guess =""
		while not answer[x] in guess:
			guess = raw_input("Guess what can be the ___"+str(x+1)+"___?: ")
			if answer[x] in guess:
				print("")
				print("Correct")
				question = question.replace(blanks[x], answer[x])
				print("")
			else:
				print("")
				print("Uncorrect")
				print("")
				print(question)

def start_game():
	"""This procedure has no input, it just take a raw_input ,then depends on this value calls the "ask" function"""
	diff = raw_input("Select the game difficulty (easy, medium, hard): ")
	correct = False
	if diff == "easy":
		ask(easy,easy_answer)
	correct = False
	if diff == "medium":
		ask(medium, medium_answer)
	if diff == "hard":
		ask(hard, hard_answer)

start_game()
# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
