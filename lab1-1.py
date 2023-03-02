import requests

#Ask for URL from user
url = input ("Enter URL here: ")

#Make the http request for the url
response = requests.get(url)

#Print headers
print("Headers of the http response:\n")
for name,value in response.headers.items():
    print("{:20s} {}".format(name,value))
    
#print(response.headers)

#Find server software 
software = response.headers.get('Server')
#Print server software
print(f"\nThe server software is: {software}")

#Check for cookies and print
#cookies = response.cookies 
