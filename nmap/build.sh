#!/bin/sh
cd "$(git rev-parse --show-toplevel)/nmap"
pex . -v --not-zip-safe --no-use-wheel -r requirements.txt --script wnmap.py -o ../wnmap
