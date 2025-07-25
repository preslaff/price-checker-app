import http.server
import socketserver
import os

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            pass

with socketserver.TCPServer(("", PORT), QuietHTTPRequestHandler) as httpd:
    print(f"Serving simple HTTP frontend on port {PORT}")
    httpd.serve_forever()