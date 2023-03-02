import requests
import time

#Ask for URL from user
url = input ("Enter URL here: ")

#Make the http request for the url
response = requests.get(url)

#Print headers
print("Headers of the http response:\n")
for name,value in response.headers.items():
    print("{:20s} {}".format(name,value))

#Find server software 
software = response.headers.get('Server')
#Print server software
print(f"\nThe server software is: {software}\n")

#Check for cookies and print
print("Cookies:")
cookies = response.cookies 
for cookie, value in enumerate(cookies):
    print("Cookie Name: {}   Expires in {} days".format(value.name,round((value.expires-time.time())/86400)))
