#!/usr/bin/env python3
"""
URL Encoder Utility
Helper script for encoding JSON content for OpenClaw API requests.
"""

import urllib.parse
import json
import sys

def encode_json_content(content_dict):
    """Encode a dictionary as JSON for URL parameters."""
    json_str = json.dumps(content_dict, separators=(',', ':'))
    return urllib.parse.quote(json_str)

def decode_json_content(encoded_content):
    """Decode URL-encoded JSON content."""
    decoded = urllib.parse.unquote(encoded_content)
    return json.loads(decoded)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            # Try to decode first
            if sys.argv[1].startswith('%'):
                result = decode_json_content(sys.argv[1])
                print(json.dumps(result, indent=2))
            else:
                # Try to parse as JSON and encode
                content = json.loads(sys.argv[1])
                result = encode_json_content(content)
                print(result)
        except Exception as e:
            print(f"Error: {e}")
            print("Usage: python url_encoder.py '{\"key\":\"value\"}' or python url_encoder.py '%7B%22key%22%3A%22value%22%7D'")
    else:
        print("Usage: python url_encoder.py '{\"key\":\"value\"}' or python url_encoder.py '%7B%22key%22%3A%22value%22%7D'")