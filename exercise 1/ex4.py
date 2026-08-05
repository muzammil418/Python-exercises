def check_number():
    num = int(input("enter a number: "))

    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")

def check_grade():
    score = int(input("enter the score: "))

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

def leap_year():
    year = int(input("enter a year: "))

    if(year %  4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("leap year")
    else:
        print("Not a Leap Year")

check_number()
check_grade()
leap_year()