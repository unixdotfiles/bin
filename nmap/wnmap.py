#!/usr/bin/env python3
# coding=utf-8


import argparse
import sys

from typing import List, Text

import nmap


_HTTP_PORTS="80,443,8000,8443"


def print_results(n) -> None:
    for host in n.all_hosts():
        open_ports = [port for port in n[host]["tcp"] if n[host]["tcp"][port]['state'] == "open"]
        print("{}: {}".format(host, open_ports))


def _gather_open_ports(cidr: Text, ports=_HTTP_PORTS, verbose=False):
    extra_args = ["--open", "-n", "-v", "-sT"]
    if verbose:
        extra_args.extend(["-sV", "--version-intensity", "9"])
    n = nmap.PortScanner()
    n.scan(cidr, ports=ports, arguments=" ".join(extra_args), sudo=False)
    return n


def find_open_http_ports(args):
    print_results(_gather_open_ports(args.cidr, verbose=args.verbose))


def find_open_ports_on_host(args):
    print_results(_gather_open_ports(args.addr, verbose=True))


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(allow_abbrev=False, fromfile_prefix_chars='@')
    subparsers = parser.add_subparsers(help="commands", dest="command")
    subparsers.required = True

    fohp_parser = subparsers.add_parser("find-open-http-ports")
    fohp_parser.add_argument("--cidr", type=str, required=True)
    fohp_parser.add_argument("-v", help="get more information", action="store_true")
    fohp_parser.set_defaults(fn=find_open_http_ports)

    foph_parser = subparsers.add_parser("find-open-ports-on-host")
    foph_parser.add_argument("--addr", type=str, required=True)
    foph_parser.set_defaults(fn=find_open_ports_on_host)

    return parser


def main() -> None:
    """
    main entry point for the program

    :param argv: args
    """
    parser = parse_args()
    args = parser.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
