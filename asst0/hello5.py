#!/usr/bin/env python3
# Maxwell Richard Tamer Mahoney ID #: 201804029
# Recursively print "Hello, World" 5 times because why not

def hello5(i=0):
    if i < 5:
        print("Hello, World!")
        hello5(i + 1)

hello5()
