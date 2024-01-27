#!/bin/bash
# Allowed Methods
curl -sILX OPTIONS $1 | grep Allow | awk -F': ' '{ print $2 }'
