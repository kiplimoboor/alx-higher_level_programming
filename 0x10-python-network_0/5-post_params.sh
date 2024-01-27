#!/bin/bash
# Send a POST with parameters
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
