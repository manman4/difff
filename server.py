#!/usr/bin/env python3
import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('difff.pl') as f:
    content = f.read().replace("'https://difff.jp/'", "'http://localhost:8080/'")
with open('index.cgi', 'w') as f:
    f.write(content)
os.chmod('index.cgi', 0o755)

class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/']

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.cgi'
        super().do_GET()

    def do_POST(self):
        if self.path == '/':
            self.path = '/index.cgi'
        super().do_POST()

server = http.server.HTTPServer(('localhost', 8080), Handler)
print('http://localhost:8080/ で起動中 (Ctrl+C で終了)')
server.serve_forever()
