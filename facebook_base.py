import requests
import time
import random

token = "token-is-given-to-you-according-to-your-subscription"


def facebook_req(req):
	r = requests.get("https://graph.facebook.com/v2.12/"+ req, {'access_token':token})
	return r 

data = ['id','username','posts']
half_url = "me?fields={}".format(data)
print(half_url)
response = facebook_req(half_url)

print(response.json())
