import requests


def get_ip():
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    return(ip)

print(get_ip())
