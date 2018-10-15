# Maxwell Richard Tamer-Mahoney ID #: 201804029
""" Check whether a given password is a "good" password, meeting these criteria:
    1) at least 8 characters long
    2) contains at least one digit 0-9
    3) contains at least one uppercase letter
    4) contains at least one lower case letter
    5) contains at least one non-alphanumeric character
"""
import sys, string

given_password = sys.argv[1]

def is_long_enough(s):
    return len(s) >= 8

def contains_digit(s):
    return len([x for x in range(10) if str(x) in s]) > 0

def contains_uppercase(s):
    return len([x for x in string.ascii_uppercase if x in s]) > 0

def contains_lowercase(s):
    return len([x for x in string.ascii_lowercase if x in s]) > 0

def contains_non_alphanumeric(s):
    return len([x for x in s if not x.isalnum()]) > 0

def is_good_password(s):
    return is_long_enough(s) and contains_digit(s) and contains_uppercase(s) and contains_lowercase(s) and contains_non_alphanumeric(s)

print(is_good_password(given_password))
