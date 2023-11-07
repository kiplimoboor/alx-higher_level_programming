#!/usr/bin/python3
"""Writes JSON string to file"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
