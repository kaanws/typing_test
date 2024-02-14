from datetime import datetime

a = datetime.now()

text = "The clouds formed beautiful animals in the sky that eventually created a tornado to wreak havoc."

print("Please type: {}".format(text))

user_input = input(": ").strip()

if text.lower() == user_input.lower():
    b = datetime.now()

    speed = b - a
    seconds = speed.total_seconds()
    letter_per_second = round(len(text) / seconds, 1)

    print("Your score is: {} seconds.".format(seconds))
    print("{} letters per second.".format(letter_per_second))
else:
    print("You failed. Please make sure to type the text as shown.")