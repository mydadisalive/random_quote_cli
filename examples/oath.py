import requests
from requests_oauthlib import OAuth2Session

# Replace these with your values
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://localhost/callback'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

# Step 1: User Authorization
github = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = github.authorization_url(authorization_base_url)

print('Please go to this URL and authorize access:', authorization_url)

# Step 2: Get the Authorization Response URL
redirect_response = input('Paste the full redirect URL here: ')

# Step 3: Fetch the Access Token
github.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

# Step 4: Make Authorized API Requests
response = github.get('https://api.github.com/user')
print(response.json())
