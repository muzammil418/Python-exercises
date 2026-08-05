def square_root():
    k = float(input("Enter a number to find its square root: "))
    guess = k / 2
    epsillon = 0.01

    while abs(guess ** 2  - k) >= epsillon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
        print(guess)

def cube_root():
    k = float(input("Enter a number to find its square root: "))
    guess = k / 2
    epsillon = 0.01
    
    while abs(guess ** 3  - k) >= epsillon:
        guess = guess - (guess ** 3 - k) / (3 * guess ** 2)
        print(guess)

square_root()
cube_root()