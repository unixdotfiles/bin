#!/usr/bin/env python
# coding=utf-8


import argparse
import sys

from typing import List

import nmap


def print_results(n, results) -> None:
    for host in n.all_hosts():
        open_ports = [ port for port in n[host]["tcp"] if n[host]["tcp"][port]['state'] == "open"]
        print("{}: {}".format(host, open_ports))


def find_open_http_ports(args):
    extra_args = ["--open", "-n", "-v", "-sT"]
    extra_args += ""
    if args.v:
        extra_args.extend(["-sV", "--version-intensity", "9", "-sS"])
    n = nmap.PortScanner()
    results = n.scan(args.cidr, ports="80,443", arguments=" ".join(extra_args), sudo=False)
    return n, results


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False, fromfile_prefix_chars='@')
    subparsers = parser.add_subparsers(help="commands", dest="command")
    subparsers.required = True
    fohp_parser = subparsers.add_parser("find-open-http-ports")
    fohp_parser.add_argument("--cidr", type=str, required=True)
    fohp_parser.add_argument("-v", help="get more information", action="store_true")
    return parser


def main(argv: List[str]) -> None:
    """
    main entry point for the program

    :param argv: args
    """
    parser = parse_args()
    args = parser.parse_args(argv)
    if args.command == "find-open-http-ports":
        n, r = find_open_http_ports(args)
        print_results(n, r)

if __name__ == "__main__":
    main(sys.argv[1:])
