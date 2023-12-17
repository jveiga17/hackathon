from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from database import save_user_data

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/frontend/html/index.html"
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/user":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            user_data = parse_qs(post_data.decode('utf-8'))

            # Extract individual values from user_data dictionary
            username = user_data.get('username', [''])[0]
            password = user_data.get('password', [''])[0]
            email = user_data.get('email', [''])[0]

            # Save user data to the database
            save_user_data(username, password, email)

            # Send a response back to the client
            self.send_response(201)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"User registered successfully\n")
        else:
            # Serve static files using the parent class
            return super().do_GET()

if __name__ == "__main__":
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 5000")
    httpd.serve_forever()
