# part (a)   Create variables of type int, float, bool, and NoneType, and print their types using type().
def variable_type():
    int_var = 10
    float_var = 11.5
    bool_var = True
    none_var  = None
    
    print(int_var)
    print(float_var)
    print(bool_var)
    print(none_var)

# part (b) Cast a float to an int and an int to a float; print results before and after casting.
def cast():
    num1 = 6
    num2 = 5.0

    print("before")
    print(num1, type(num1))
    print(num2, type(num2))

    num1_float = float(num1)
    num2_int = int(num2)

    print("after")
    print(num1, type(num1))
    print(num2, type(num2))

# part (c)  Given two numbers a = 17, b = 5, print the results of a + b, a - b, a * b, a / b, a // b, a % b, a ** b.
def airthmetic_operators():
    a = 17
    b = 16

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(a // b)
    print(a ** b)

# part (c) Predict (in a comment) the type of each result in (c) before running the code, then verify.
def verify_result_types():
    a = 17
    b = 16

    # a + b -> int
    print(a + b, type(a + b))

    # a - b -> int
    print(a - b, type(a - b))

    # a * b -> int
    print(a * b, type(a * b))

    # a / b -> float
    print(a / b, type(a / b))

    # a // b -> int
    print(a // b, type(a // b))

    # a % b -> int
    print(a % b, type(a % b))

    # a ** b -> int
    print(a ** b, type(a ** b))

def main():
    variable_type()
    cast()
    airthmetic_operators()
    verify_result_types()


if __name__ == "__main__":
    main()