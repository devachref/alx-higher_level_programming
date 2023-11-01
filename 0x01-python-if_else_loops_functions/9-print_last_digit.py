#!/usr/bin/python3
def print_last_figit(number):
    number = abs(number) % 10
    print(number, end="")
    return number
