python3 src/main.py
cd public && lsof -ti:8888 | xargs kill -9 2>/dev/null || true
python3 -m http.server 8888
