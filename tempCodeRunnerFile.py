import requests


response =requests.get("https://npiregistry.cms.hhs.gov/api", params = {"version" :"2.1","state" : "TX","taxonomy_description":"geriatric medicine", "limit":5})
data = response.json()
