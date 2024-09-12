import requests

# making a GET request
response = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(response)

# print content of request
print(response.content)