#!/usr/bin/python3
def print_last_digit(number):
    number %= 10
    print('{}'.format(number), end='\n')
    return number
