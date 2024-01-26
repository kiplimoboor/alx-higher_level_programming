#!/bin/bash
# Gets body size of text
curl -sI $1 | grep Content-Length | awk '{ print $2 }'
