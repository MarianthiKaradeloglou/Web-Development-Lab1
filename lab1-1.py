import requests
import time

#Ask for URL from user
url = input ("Enter URL here: ")
#for example I used https://www.google.gr/

#Make the http request for the url
response = requests.get(url)

print("\n--------------------------------")
#Print headers
print("Headers of the http response:\n")
for name,value in response.headers.items():
    print("{:20s} {}".format(name,value))

print("--------------------------------")
#Find server software 
software = response.headers.get('Server')
#Print server software
print(f"\nThe server software is: {software}\n")

print("--------------------------------")
#Check for cookies and print
print("Cookies:")
cookies = response.cookies 
if cookies:
    for cookie, value in enumerate(cookies):
        print("Cookie Name: {}   Expires in {} days".format(value.name,round((value.expires-time.time())/86400)))
else:
    print("The page does not use cookies")
