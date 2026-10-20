from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RevivalServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "project": "RecRoom2019Revival",
                "status": "running",
                "message": "Revival server prototype is alive!"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <body>
                    <h1>Rec Room 2019 Revival</h1>
                    <p>Server prototype</p>
                    <p>More development needed!</p>
                </body>
                </html>
            """)

server = HTTPServer(("0.0.0.0", 8000), RevivalServer)
print("Revival server started on port 8000")
server.serve_forever()
