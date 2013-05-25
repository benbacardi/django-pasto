"""Utilities for Pasto"""
import difflib

def get_diff(s1, s2):
    """
    Returns a friendly diff format for two provided strings.
    """
    output = []
    d = difflib.Differ()
    for line in d.compare(s1.splitlines(), s2.splitlines()):
        tag = None
        if line.startswith('?'): continue
        elif line.startswith('+'): tag = 1
        elif line.startswith('-'): tag = 0
        output.append((tag, line[2:]))
    return output
