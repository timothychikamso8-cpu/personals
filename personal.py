import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()


def find_worker(data):
    name = input("input users name here: ")
    found = False
    for worker in data:
        if worker["name"].lower() == name.lower():
            print(worker)
            found = True

    if not found :
        print("no worker found")

        

def find_domain(data):
    domain = input("input area of specialization: ")
    found = False
    for worker in data:
       if domain.lower() in worker["company"]["name"].lower():
            print(worker)
            found = True

    if not found:
        print("company name unavailable")
        


find_domain(data)