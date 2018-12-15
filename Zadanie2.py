#!/usr/bin/env python3


def check():
    number = input("Put your number: ")
    number2 = 0
    number = int(number)    # obie wartosci musza byc typu int dla operacji is
    if number is number2:
        print("Hero zero")
    else:
        print("Your number is {}.".format(number))


check()
