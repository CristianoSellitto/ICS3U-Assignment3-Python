#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if function f is quadratic and calculates the roots

import math


def main():
    # Finds if function f is quadratic and calculates the roots

    print("f(x) = ax² + bx + c")
    a_value = int(input("\nEnter the value of a: "))
    b_value = int(input("Enter the value of b: "))
    c_value = int(input("Enter the value of c: "))
    if a_value != 0:
        print("\nThis is a quadratic function.")
        discriminant = b_value**2 - 4 * a_value * c_value
        if discriminant == 0:
            root_one = (-b_value + math.sqrt(b_value**2 - 4 * a_value * c_value)) / (
                2 * a_value
            )
            print("Function f's root is ({}, 0)".format(root_one))
        elif discriminant > 0:
            root_one = (-b_value + math.sqrt(b_value**2 - 4 * a_value * c_value)) / (
                2 * a_value
            )
            root_two = (-b_value - math.sqrt(b_value**2 - 4 * a_value * c_value)) / (
                2 * a_value
            )
            print(
                "Function f's roots are ({0}, 0) and ({1}, 0)".format(
                    root_one, root_two
                )
            )
        else:
            print("Function f has no roots")
    else:
        print("\nThis is not a quadratic function.")

    print("\nDone.")


if __name__ == "__main__":
    main()
