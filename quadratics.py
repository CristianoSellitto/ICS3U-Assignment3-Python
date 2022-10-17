#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if function f is quadratic or linear


def main():
    # Finds if function f is quadratic or linear and prints basic info about function f

    print("f(x) = ax² + bx + c")
    a_value = int(input("\nEnter the value of a: "))
    b_value = int(input("Enter the value of b: "))
    c_value = int(input("Enter the value of c: "))
    if a_value == 0:
        print("\nThis is a linear function.")
        print("\nThe slope of function f is {}".format(b_value))
    else:
        print("\nThis is a quadratic function.")
        print("\nThe vertical stretch of function f is {}".format(a_value))
    print("The y-intercept of function f is (0, {})".format(c_value))

    print("\nDone.")


if __name__ == "__main__":
    main()
