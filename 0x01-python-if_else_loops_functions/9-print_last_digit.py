#!/usr/bin/python3
def print_last_digit(number):
    """A function that prints the last digit of a number and return its value"""
    last = abs(number) % 10
    print("{}".format(last), end='')
    return last
