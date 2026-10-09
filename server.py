#!/usr/bin/env python3
"""
Emergency Alert Packet Integrity Simulator
Local Development & Presentation Server
Zero external dependencies. Uses Python 3 standard library.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORTS_TO_TRY = [8000, 8080, 8088, 8888, 5000, 3000, 0]
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class TacticalHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        sys.stdout.write(f"[TELEMETRY SERVER] {self.address_string()} - {format%args}\n")
        sys.stdout.flush()

def open_in_browser(url):
    """Safely open URL on Windows using multiple methods"""
    try:
        if os.name == 'nt' and hasattr(os, 'startfile'):
            os.startfile(url)
            return True
    except Exception:
        pass

    try:
        return webbrowser.open(url)
    except Exception:
        return False

def main():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    
    httpd = None
    active_port = 8000

    for port in PORTS_TO_TRY:
        try:
            httpd = socketserver.TCPServer(("127.0.0.1", port), TacticalHTTPHandler)
            active_port = httpd.server_address[1]
            break
        except OSError:
            continue

    if not httpd:
        print("[ERROR] Could not bind to any available network port.")
        index_file = os.path.join(DIRECTORY, "index.html")
        print(f"[+] Opening local file directly: {index_file}")
        open_in_browser(index_file)
        sys.exit(1)

    url = f"http://127.0.0.1:{active_port}/"
    print("=" * 68, flush=True)
    print("  EMERGENCY ALERT PACKET INTEGRITY SIMULATOR - LOCAL SERVER", flush=True)
    print("=" * 68, flush=True)
    print(f"  [+] Serving files from : {DIRECTORY}", flush=True)
    print(f"  [+] Simulator URL      : {url}", flush=True)
    print("  [+] Launching browser automatically...", flush=True)
    print("  [+] Press Ctrl+C in this window to stop the server", flush=True)
    print("=" * 68, flush=True)

    # Launch browser
    open_in_browser(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  [!] Server shutting down safely...", flush=True)
        httpd.server_close()

if __name__ == "__main__":
    main()
