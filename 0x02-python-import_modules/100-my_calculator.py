#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    left = int(argv[1])
    right = int(argv[3])
    if (operator == '+'):
        print(f"{left} + {right} = {add(left, right)}")
    elif (operator == '-'):
        print(f"{left} - {right} = {sub(left, right)}")
    elif (operator == '*'):
        print(f"{left} * {right} = {mul(left, right)}")
    elif (operator == '/'):
        print(f"{left} / {right} = {div(left, right)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
