def guess_game():
    low = 1
    high = 100
    

    while True:
        guess = (high + low) // 2
        print("My guess is:", guess)

        feedback = input("Enter higher, lower or correct: ")

        if feedback == "higher":
           low = guess - 1
           guess = (high + low) // 2

        elif feedback == "lower":
            high = guess + 1
            guess = (high + low) // 2

        elif feedback == "correct":
            print("I guessed it!")
            break

guess_game()

numbers = [2, 5, 9, 11, 15, 20, 27, 35]

target = int(input("enter the target: "))

low = 0
high = len(numbers) - 1

while low <= high:

    mid = (high + low) // 2

    if numbers[mid] == target:
        print("found")
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1