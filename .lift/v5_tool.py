#!/usr/bin/env python3

import json
import os
from pathlib import Path
import sys

def emit_version():
    print(5)

def emit_version_json():
    print(json.dumps({
        "name": "v5_tool",
        "api-version": {
            "type": "bulk",
            "version": 2
        }
    }))

def emit_name():
    print("v5_tool")


def emit_applicable():
    print("true")

def run(path):
    pathlist = Path(path).glob('**/*.md')

    tool_notes = []
    for filename in pathlist:
        tool_notes.extend(process_file(filename))

    print(json.dumps({
        "tool_notes": tool_notes,
        "warnings": [
            {
                "display_message": "Warning, not actually a tool",
                "detailed_message": "v5_tool.py IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT."
            }
        ],
        "pull_request": None
    }))

def process_file(filename):
    file_display = str(filename)
    tool_notes = []
    with open(filename, 'r') as f:
        current_line = 0
        for line in f:
            current_line += 1
            if("markdown comment" in line):
                tool_notes.append(line_to_tool_note(file_display, current_line, "# Markdown Header\n\nMarkdown Body"))
            if("markdown code snippet" in line):
                tool_notes.append(line_to_tool_note(file_display, current_line, "```rust\nlet best_programming_language = \"🦀\";\n```"))
    
    return tool_notes

def line_to_tool_note(filename, line_number, message):
    return {
        "type": "V5 Markdown Tool",
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
    else:
        emit_version_json()

if __name__ == "__main__":
    main()
