#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Summer 2026
Program: assignment2.py
Author: Kiera Solomon

The python code in this file is original work written by
Kiera Solomon. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: Displays system and process memory usage.

Date: 2026-07-17
'''

import argparse
import os
import sys


def parse_command_args() -> object:
    """Set up argparse here. Call this function inside main."""
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )
    # Human-readable option will be completed during Milestone 2.
    parser.add_argument(
        "program",
        type=str,
        nargs="?",
        help="if a program is specified, show memory use of all associated "
             "processes. Show only total use if not."
    )
    args = parser.parse_args()
    return args


def percent_to_graph(percent: float, length: int = 20) -> str:
    """Turn a percentage from 0.0 to 1.0 into a bar graph."""
    filled_length = int(percent * length)
    empty_length = length - filled_length
    return "#" * filled_length + " " * empty_length


def get_sys_mem() -> int:
    """Return the total system memory from /proc/meminfo in kB."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])
    return 0


def get_avail_mem() -> int:
    """Return the available system memory from /proc/meminfo in kB."""
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])
    return 0


def pids_of_prog(app_name: str) -> list:
    """Given an application name, return its process IDs."""
    # This function will be completed during Milestone 2.
    pass


def rss_mem_of_pid(proc_id: str) -> int:
    """Given a process ID, return the resident memory used."""
    # This function will be completed during Milestone 2.
    pass


def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """Turn 1,024 KiB into 1 MiB, for example."""
    suffixes = ["KiB", "MiB", "GiB", "TiB", "PiB"]
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f"{result:.{decimal_places}f} "
    str_result += suffixes[suf_count]
    return str_result


if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        # Final program output will be completed later.
        pass
    else:
        # Process output will be completed later.
        pass
