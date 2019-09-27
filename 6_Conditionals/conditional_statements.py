# Getting user input
# input(prompt) - it prints the prompt message and waits for the user input and when user hits enter,
#                 it returns the user input as "string".

user_input = int(input("Enter you age?"))

if user_input >= 21:
    print("You can start drinking.")
elif 13 < user_input < 21:
    print("Study hard for SAT!")
else:
    print("Play video games!")

