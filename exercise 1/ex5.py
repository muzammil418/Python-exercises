def print_numbers():
    for i in range(1, 21):
        print(i)

    for i in range(2, 21, 2):
        print(i)

def quit_loop():
    while True:
        str_var = input("enter a string: ")

        if str_var == "quit":
            break

def count_letter():
    str_var = input("enter the string: ")
    letter = input("enter a letter: ")
    count = 0

    for i in str_var:
        if i == letter:
            count += 1

    print(count)

def sum_of_digits():
    num = input("enter a number: ")
    int_var = 0

    for i in num:
        int_var += int(i)

    print(int_var)

print_numbers()
quit_loop()
count_letter()
sum_of_digits()