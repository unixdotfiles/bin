#!/bin/sh
cd "$(git rev-parse --show-toplevel)"
pex nmap -v --not-zip-safe --no-use-wheel -r nmap/requirements.txt --script wnmap.py -o wnmap
