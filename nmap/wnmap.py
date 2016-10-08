#!/usr/bin/env python
# coding=utf-8


import argparse
import sys

from typing import List, Text

import nmap


def print_results(n) -> None:
    for host in n.all_hosts():
        open_ports = [port for port in n[host]["tcp"] if n[host]["tcp"][port]['state'] == "open"]
        print("{}: {}".format(host, open_ports))


def _gather_open_http_ports(args):
    extra_args = ["--open", "-n", "-v", "-sT"]
    extra_args += ""
    if args.v:
        extra_args.extend(["-sV", "--version-intensity", "9", "-sS"])
    n = nmap.PortScanner()
    n.scan(args.cidr, ports="80,443", arguments=" ".join(extra_args), sudo=False)
    return n

def find_open_http_ports(args):
    print_results(_gather_open_http_ports(args))


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False, fromfile_prefix_chars='@')
    subparsers = parser.add_subparsers(help="commands", dest="command")
    subparsers.required = True
    fohp_parser = subparsers.add_parser("find-open-http-ports")
    fohp_parser.add_argument("--cidr", type=str, required=True)
    fohp_parser.add_argument("-v", help="get more information", action="store_true")
    fohp_parser.set_defaults(fn=find_open_http_ports)
    return parser


def main(argv: List[Text]) -> None:
    """
    main entry point for the program

    :param argv: args
    """
    parser = parse_args()
    args = parser.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main(sys.argv[1:])
