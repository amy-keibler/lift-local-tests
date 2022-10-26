#!/usr/bin/env python3

import argparse
import json
import os
from pathlib import Path

def emit_version():
    print(4)


def emit_name():
    print("bom_tool")


def emit_applicable():
    print("true")

def run(path):

    data = {
        "cyclone-dx-sbom": {
            "bomFormat": "CycloneDX",
            "specVersion": "1.4",
            "version": 1,
            "metadata": {},
            "components": [
                {
                    "name": "Vulnerable Component",
                    "version": "3",
                    "bom-ref": "vulnerable-component",
                }
            ],
            "dependencies": [],
            "vulnerabilities": [
                {
                    "bom-ref": "vulnerable-component"
                }
            ],
        }
    }

    print(json.dumps(data))

def main():
    parser = argparse.ArgumentParser(description='Bom Tool')
    parser.add_argument('path', metavar='PATH', help='Path to code')
    parser.add_argument('commit_hash', metavar='HASH', help='Commit hash')
    parser.add_argument('command', metavar='COMMAND', help='Command')

    args = parser.parse_args()

    path = args.path

    command = args.command

    if command == "version":
        emit_version()
    elif command == "name":
        emit_name()
    elif command == "applicable":
        emit_applicable()
    elif command == "run":
        run(path)

if __name__ == "__main__":
    main()
