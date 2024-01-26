#!/usr/bin/env bash
# Gets body size of text
curl -sI 0:5000 | grep Content-Length | awk '{ print $2 }'