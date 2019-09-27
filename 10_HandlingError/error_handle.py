# Errors

# Syntax(grammar) Error: happens when Python cannot interpret your code, since we didn't follow the correct syntax for
# Python. These errors you're likely to get when you make a typo.
# (red underline) - (compile-time)

msg = 'Hello, World!'

# Exceptions (crash): happens when unexpected things happen during the execution of a program (run-time), even if
# the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see
# which exception is 'thrown' in the error message.
# -> please "read the error message!"

# try-except block
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        c = a / b
        break
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Invalid input. Please enter a number!")
    except KeyboardInterrupt:
        print("\nNo input taken.\n")
        break
    except ZeroDivisionError as e:
        print(f"Invalid Input: {e}")
    except EOFError as e:
        print(f"{e}")
        break
    finally:
        print("Done!")

# Value Error : Wrong invalid char
# Keyboard Interrupt : ^ + c
# EOF : ^ + d
