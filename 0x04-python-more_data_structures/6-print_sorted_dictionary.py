#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for feature in sorted(a_dictionary):
        print(f"{feature}: {a_dictionary[feature]}")
