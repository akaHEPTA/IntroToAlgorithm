score = 0

while True:
    try:
        score = int(input("Enter your score: "))
        break
    except ValueError:  # Value error exception control
        print("Entered value is not correct, try again.")

if score >= 90:
    print("Your grade is A.")
elif 90 > score >= 80:
    print("Your grade is B.")
elif 80 > score >= 70:
    print("Your grade is C.")
elif 70 > score >= 60:
    print("Your grade is D.")
elif 60 > score:
    print("Your grade is F.")
