import random
number = random.randint(1,20)
guesses = 6
i = 0
while i < 6:
    i += 1
    answer = input("guess which number is the correct number (from 1 to 20), you have " + str(7 - i) + " guesses: ")
    if int(answer) < number:
        print("The number you want is a little bit bigger!")
        continue
    elif int(answer) > number:
        print("the number you want is a little smaller")
    elif int(answer) == number:
        print("Good job, you guessed right!")
        break


