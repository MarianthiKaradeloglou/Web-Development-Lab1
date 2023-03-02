import requests

#Ask for URL from user
url = input ("Enter URL here: ")

#Make the http request for the url
response = requests.get(url)

#Print headers
print("Headers of the http response:\n")
print(response.headers)

