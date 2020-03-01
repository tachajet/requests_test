#import the module
import requests
#create a new variable, cat_requests, that uses the requests.get function to pull a cat fact
cat_response=requests.get('https://cat-fact.herokuapp.com/facts/random')
#print the cat fact as text after parsing the JSON of cat_request using the .json() method
print(cat_response.json()['text'])
