#!/usr/bin/python3
"""This module has a script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv

try:
    arguments = load_from_json_file("add_item.json")
except FileNotFoundError:
    arguments = []

arguments.extend(args[1:])
save_to_json_file(arguments, "add_item.json")
