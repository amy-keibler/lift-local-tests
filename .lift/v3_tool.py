#!/usr/bin/env python3

import json
import os
from pathlib import Path
import sys

def emit_version():
    print(1)

def emit_version_json():
    print(json.dumps({
        "name": "v3_tool",
        "api-version": {
            "type": "per file",
            "version": 1
        }
    }))


def emit_name():
    print("v3_tool")


def emit_applicable():
    print("true")

def run(path):
    config = sys.stdin.read()
    run_info = json.loads(config)
    files = run_info["files"]

    tool_notes = []
    for filename in files:
        tool_notes.append(line_to_tool_note(f"{path}/{filename}", 1, "Testing"))

    print(json.dumps({
        "toolNotes": tool_notes,
        "warnings": [
            {
                "display_message": "Warning, not actually a tool",
                "detailed_message": "v5_tool.py IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT."
            }
        ],
        "pull_request": None
    }))

def line_to_tool_note(filename, line_number, message):
    return {
        "type": "Markdown Tool",
        "message": message,
        "file": filename,
        "line": line_number
    }

def main():
    command = None
    if len(sys.argv) > 1:
        command = sys.argv[1]

    path = os.getcwd()

    if command == "version":
        emit_version()
    elif command == "name":
        emit_name()
    elif command == "applicable":
        emit_applicable()
    elif command == "run":
        run(path)
    elif command == "finalize":
        finalize(path)
    else:
        emit_version_json()

if __name__ == "__main__":
    main()
