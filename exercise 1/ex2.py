# part 1:Given a string s = "Introduction to CS", print the first 5 characters, the last 5 characters, and the string reversed.
def string_slicing():
    str_var = "Introduction to CS"

    print(str_var[:5])
    print(str_var[-5:])
    print(str_var[::-1])

# part 2:Take a string and print it in all uppercase, all lowercase, and title case.
def case():
    str_var = "Introduction to CS"

    print(str_var.lower())
    print(str_var.upper())
    print(str_var.title())

#part 3: Write code to check whether a given word is a palindrome (reads the same forwards and backwards).
def palindrome_check():
    word = "madam"

    if word == word[::-1]:
        print("palindrome")

    else:
        print("Not Palindrome")

#part 4:Count how many vowels appear in a given sentence.
def count_vowels():
    str_var = "Introduction to CS"
    vowels = "aeiouAEIOU"
    count = 0

    for i in str_var:
        if i in vowels:
            count += 1
    print(count)

def main():
    string_slicing()
    case()
    palindrome_check()
    count_vowels()


if __name__ == "__main__":
    main()