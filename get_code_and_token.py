from urllib.parse import urlencode
import webbrowser
import time
import datetime

timestamp = datetime.datetime.now().timestamp()



print("Don't have any 'localhost' running in order to get the 'code' param value that will be generated\n\n")
print("The browser will open and get the value of 'code' from the url bar")


client_id = input('CLIENT ID: ')

redirect_url = "http://localhost"


#scope = "https://www.googleapis.com/auth/blogger"
scope = input('SCOPE[eg:calendar, blogger, email]: ')
scope = f"https://www.googleapis.com/auth/{scope}"

query_params = {

        "response_type" : "code", 
        "client_id" : client_id,
        "redirect_uri" : redirect_url,
        "scope" : scope
}




url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(query_params)}"


print('Get Ready... Browser will open, COPY the code value quickly')
time.sleep(5) 

webbrowser.open(url)

print('Open')

time.sleep(3)

import requests

token_endpoint = "https://oauth2.googleapis.com/token"


time.sleep(5)

code  = input('YOUR CODE: ')

client_secret = input("YOUR CLIENT SECRET: ")



data  = {

        "grant_type" : "authorization_code",
        "code" : code,
        "redirect_uri" : redirect_url,
        "client_id" : client_id,
        "client_secret" : client_secret,
        "scope" : "https://www.googleapis.com/auth/blogger"
}

response = requests.post(token_endpoint, data=data)
token = response.json()["access_token"]

#create a new text file and add 'token' in it

filename = "NEW_TOKEN_"+str(timestamp)+".txt"
with open(filename, "w") as file:
    file.write(token)

print("\n\n\n")

print("New file created: ", filename)

print("\n\n\n")

print("--------------------TOKEN-----------------\n")
print(token, "\n")
print("--------------------------------------------")


