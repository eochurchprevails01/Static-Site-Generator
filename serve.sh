#!/bin/bash

# Kill any existing server on port 8888
lsof -ti:8888 | xargs kill -9 2>/dev/null || true

# Build the site
echo "Building static site..."
python3 src/main.py

# Start server in background
echo "Starting server on port 8888..."
cd docs
python3 -m http.server 8888 &
SERVER_PID=$!

# Wait a moment for server to start
sleep 2

# Open browser (works in WSL)
echo "Opening browser..."
if command -v xdg-open >/dev/null 2>&1; then
    xdg-open http://localhost:8888
elif command -v wslview >/dev/null 2>&1; then
    wslview http://localhost:8888
else
    echo "Browser not automatically opened. Please visit: http://localhost:8888"
fi

echo "Server running on http://localhost:8888"
echo "Press Ctrl+C to stop the server"

# Wait for user to stop
wait $SERVER_PID
