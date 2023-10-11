#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    roman_string = roman_string.upper()
    value = 0
    current_value = 0
    next_value = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in list(roman_values):
            return 0
        current_value = roman_values[roman_string[i]]
        if i + 1 < len(roman_string):
            if roman_string[i + 1] not in list(roman_values):
                return 0
            next_value = roman_values[roman_string[i + 1]]
        if current_value >= next_value:
            value += current_value
        else:
            value -= current_value

    return value
