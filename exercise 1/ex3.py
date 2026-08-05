def greeting():
    name = input("enter your name: ")
    age = int(input("enter your age: "))

    print("hello", name, "you are", age, "year old")

def greeting_percent():
    name = input("enter your name: ")
    age = int(input("enter your age: "))

    print("hello %s you are %d year old" % (name, age))

def greeting_format():
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    
    print("hello {} you are {} year old" .format(name, age))

def greeting_fstring():
    name = input("enter your name: ")
    age = int(input("enter your age: "))

    print(f"hello {name} you are {age} year old")

def float_formatting():
    price = float(input("enter price: "))

    print("%.2f" % price)

greeting()
greeting_percent()
greeting_format()
greeting_fstring()
float_formatting()