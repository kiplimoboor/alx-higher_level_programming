#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv) - 1

    if (args == 0):
        print("0 arguments.")
    else:
        if (args == 1):
            print("1 argument:")
        else:
            print(f"{args} arguments:")
        for i in range(1, args + 1):
            print(f"{i}: {argv[i]}")
