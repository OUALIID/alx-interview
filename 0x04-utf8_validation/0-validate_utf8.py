#!/usr/bin/python3
""" UTF-8 Validation."""


def validUTF8(data):
    """Validate whether a given data set represents a valid UTF-8 encoding."""
    try:
        bytes(byte & 0xFF for byte in data).decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False
