#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        print(-(number) % 10, end='')
    else:
        print((number) % 10, end='')
    return abs(number)
print_last_digit(98)
print_last_digit(0)
print_last_digit(-1024)
