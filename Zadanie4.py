#!/usr/bin/env python3


class Triangle:
    def __init__(self, side_length, name):
        self.side_length = side_length
        self.name = name

    def __eq__(self, other):
        print("Comparision tAype: {} == {}".format(self.name, other.name))
        return self.side_length == other.side_length

    def __lt__(self, other):
        print("Comparision type: {} < {}".format(self.name, other.name))
        return self.side_length < other.side_length

    def __gt__(self, other):
        print("Comparision type: {} > {}".format(self.name, other.name))
        return self.side_length > other.side_length

    def __le__(self, other):
        print("Comparision type: {} <= {}".format(self.name, other.name))
        return self.side_length <= other.side_length

    def __ge__(self, other):
        print("Comparision type: {} >= {}".format(self.name, other.name))
        return self.side_length >= other.side_length

    def __ne__(self, other):
        print("Comparision type: {} != {}".format(self.name, other.name))
        return self.side_length != other.side_length


a = Triangle(1, "A")
b = Triangle(2, "B")
h = Triangle(3, "H")

print("")
print("A < B = {}".format(a < b))
print("")
print("A > B = {}".format(a > b))
print("")
print("A <= B = {}".format(a <= b))
print("")
print("A >= B = {}".format(a >= b))
print("")
print("A != B = {}".format(a != b))
print("")
print("A == B = {}".format(a == h))
print("")
print("A < H = {}".format(a < h))
print("")
print("A > H = {}".format(a > h))
print("")
print("A <= H = {}".format(a <= h))
print("")
print("A >= H = {}".format(a >= h))
print("")
print("A != H = {}".format(a != h))
print("")
print("B != H = {}".format(b != h))
print("")
print("B < H = {}".format(b < h))
print("")
print("B > H = {}".format(b > h))
print("")
print("B <= H = {}".format(b <= h))
print("")
print("B >= H = {}".format(b >= h))
print("")
print("B != H = {}".format(b != h))
