#!/bin/bash

# Kill any existing server
lsof -ti:8888 | xargs kill -9 2>/dev/null || true

# Build the site
echo "Building static site..."
python3 src/main.py

# Start server with auto-reload capability
echo "Starting live server on port 8888..."
cd docs

# Use Python's http.server with auto-reload
python3 -c "
import http.server
import socketserver
import webbrowser
import threading
import time

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    time.sleep(1)
    webbrowser.open('http://localhost:8888')

threading.Thread(target=open_browser).start()

with socketserver.TCPServer(('', 8888), Handler) as httpd:
    print('Live server running at http://localhost:8888')
    print('Press Ctrl+C to stop')
    httpd.serve_forever()
"
