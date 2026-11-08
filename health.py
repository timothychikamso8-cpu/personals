import requests
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start =time.time()
        result = func(*args,**kwargs)
        stop = time.time()
        result["time_ms"] = round((stop - start) * 1000)
        return result
    return wrapper


@timer
def check_url(url,params = None,timeout = 5):
    try: 
        response = requests.get(url, params=params, timeout=timeout)

        if response.status_code == 200:
            return {"url":url,"status":"up"}

        else:
            return{"url":url,"status": "down"}



    except requests.exceptions.Timeout:
        return {"url": url, "status": "down", "reason": "timeout"}
    
    except requests.exceptions.ConnectionError:
        return {"url": url, "status": "down", "reason": "connection error"}

    except requests.exceptions.RequestException as e:
        return{"url" : url, "status" : "down", "reason": str(e)}    
    
url = "https://npiregistry.cms.hhs.gov/api"
params = {"version": "2.1", "state": "TX", "taxonomy_description": "geriatric medicine", "limit": 5} 
bad_url = "https://thisdomaindoesnotexist12345.com"


if __name__ == "__main__":
    print(check_url(bad_url, {}, timeout=5))
 
    print(check_url(url,params,timeout = 5))

    print(check_url("https://api.github.com", {}))

    print(check_url("htp://oops"))


