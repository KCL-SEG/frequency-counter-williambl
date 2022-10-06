"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items_str = [str(i) for i in items]
    frequencies = {k: items_str.count(k) for k in items_str}
    return frequencies
