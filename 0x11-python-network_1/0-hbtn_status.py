#!/usr/bin/python3
"""
    Fetches from alx
"""

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")
