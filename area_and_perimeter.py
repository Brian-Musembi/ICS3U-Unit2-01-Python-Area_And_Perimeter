#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 26 April 2021
# This program calculates the area and perimeter of a circle

import math

def main():
    print("If a circle has a radius of:")
    print("15 mm")
    print("")
    print("The area of the circle is {} mm².".format(math.pi * 15 ** 2))
    print("And the perimeter of the circle is {} mm.".format(2 *(math.pi * 15)))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
