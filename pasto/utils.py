"""Utilities for Pasto"""
import difflib

from django.contrib.auth.decorators import login_required

from .app_settings import ALLOW_ANONYMOUS_POSTS

def enum(**enums):
    return type('Enum', (), enums)

DiffLineTypes = enum(NO_CHANGE=None, LINE_REMOVED=0, LINE_ADDED=1)

def get_diff(s1, s2):
    """
    Returns a friendly diff format for two provided strings.
    """
    output = []
    d = difflib.Differ()
    for line in d.compare(s1.splitlines(), s2.splitlines()):
        tag = DiffLineTypes.NO_CHANGE
        if line.startswith('?'): continue
        elif line.startswith('-'): tag = DiffLineTypes.LINE_REMOVED
        elif line.startswith('+'): tag = DiffLineTypes.LINE_ADDED
        output.append((tag, line[2:]))
    return output

def login_possibly_required(function=None, *args, **kwargs):
    if not ALLOW_ANONYMOUS_POSTS:
        return login_required(function, *args, **kwargs)
    return function
