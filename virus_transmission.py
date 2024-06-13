"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""


def calculate_infections(starting_number_infections, reproduction_rate, num_days):
    current_infections = starting_number_infections
    for day in range(num_days):
        current_infections = round(current_infections * reproduction_rate)
    return current_infections


