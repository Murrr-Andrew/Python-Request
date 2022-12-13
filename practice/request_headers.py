import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get('https://httpbin.org/headers', headers=headers)

# Using response.json - due to the httpbin.org site settings
print(response.json())
