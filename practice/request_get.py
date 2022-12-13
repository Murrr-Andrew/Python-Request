import requests

params = {
    'q': 'funny cats'
}

response = requests.get('https://www.google.com/search', params=params)

# response.status_code
# response.headers
# response.content
