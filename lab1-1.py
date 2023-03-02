import requests

url = input ("Enter URL here: ")

response = requests.get(url)

print("Headers of the http response:\n")
print(response.headers)