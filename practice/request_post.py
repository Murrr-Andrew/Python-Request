import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/108.0.0.0 Safari/537.36'
}
data = {
    'custname': 'Andrew',
    'custtel': '+18888888888',
    'custemail': 'test@gmail.com'
}

response = requests.post('https://httpbin.org/post', headers=headers, data=data)

print(response.json())
