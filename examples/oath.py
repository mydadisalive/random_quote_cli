import os
import requests
from requests_oauthlib import OAuth2Session
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import webbrowser

# Configuration
client_id = os.getenv('GITHUB_CLIENT_ID', 'your_client_id')
client_secret = os.getenv('GITHUB_CLIENT_SECRET', 'your_client_secret')
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'
redirect_uri = 'https://4f88-2a0d-6fc2-4200-a100-89b0-90ba-8e02-251a.ngrok-free.app'
scope = ['user']

# A simple HTTP server to handle the OAuth callback
class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        auth_code = self.path.split('code=')[-1]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Authorization complete. You can close this window.')
        return

def start_http_server():
    server = HTTPServer(('localhost', 8000), OAuthCallbackHandler)
    server.serve_forever()

# Start the HTTP server in a separate thread
server_thread = threading.Thread(target=start_http_server)
server_thread.daemon = True
server_thread.start()

# Step 1: User Authorization
github = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = github.authorization_url(authorization_base_url)

print('Please go to this URL and authorize access:', authorization_url)
webbrowser.open(authorization_url)

# Step 2: Wait for the Authorization Response
auth_code = ''
while not auth_code:
    pass

# Step 3: Fetch the Access Token
github.fetch_token(token_url, client_secret=client_secret, authorization_response=f'{redirect_uri}?code={auth_code}')

# Endpoint URL
url = 'https://api.github.com/user'
# Sending a GET request with authentication headers
response = github.get(url)

# Handling response
if response.status_code == 200:
    data = response.json()
    print(f"User data: {data}")
else:
    print(f"Failed to retrieve user data: {response.status_code}")
