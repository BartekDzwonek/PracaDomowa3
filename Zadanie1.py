#!/usr/bin/env python3


def greetings():
    name = input("Put your name here: ")
    name2 = input("Put your name here: ")
    if name == name2:
        print("Oh i am {} too WOW!".format(name), end="")
    else:
        print("Hello {}".format(name2))
        print("Oh hi {}".format(name))


greetings()

//abcd
