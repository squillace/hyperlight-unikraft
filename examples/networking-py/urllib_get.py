"""High-level HTTP GET using urllib (Python stdlib).

Demonstrates that Python's standard urllib.request module works
over the host-proxied socket layer — no raw sockets needed.

Uses a raw IP with Host header to avoid DNS dependency (glibc's
getaddrinfo doesn't yet work over host-proxied UDP sockets).
"""
import urllib.request
import sys

URL = "http://172.66.147.243/"

print(f"Fetching {URL} ...")
req = urllib.request.Request(URL, headers={"Host": "example.com"})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        print(f"Status: {resp.status}")
        print(f"Body length: {len(body)} bytes")
        if "Example Domain" in body:
            print("SUCCESS: urllib GET worked!")
        else:
            print("WARNING: unexpected body content")
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
