#!/bin/bash
# Send a POST with parameters
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
