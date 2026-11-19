from api_client import APIClient
import requests

client = APIClient("https://httpbin.org")

def main_get():
   
    try: 
        
        result = client.get(f"/bearer")

        if result is not None:
            if result.get("authenticated") is True:
                print("API client test passed.")

            else:
                print("The API returned an unexpected result.")
        else:
            print("The request could not be completed.")

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return None
    except ValueError as error:
        print(f"Invalid JSON response: {error}")
        return None
    
def main_post():
    try:     
        payload = {
            "name": "Sample Product",
            "price": 25.50
        }

    
        result = client.post("/post", payload)

        if result is not None:
            print("Post request successful.")
            print("Submitted data:", result.get("json"))
        else:
            print("POST request failed.")
    
    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return None
    except TypeError as error:
        print(f"Invalid payload: {error}")
        return None
    except  ValueError as error:
            print("Invalid input:", error)

def main_put():
    try:    
        payload = {
            "name": "Updated Product",
            "price": 30.00
        }

    
        result = client.put("/put", payload)

        if result is not None:
            print("PUT request successful.")
            print("Submitted data:", result.get("json"))
        else:
            print("PUT request failed.")
    
    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return None
    except TypeError as error:
        print(f"Invalid payload: {error}")
        return None
    except ValueError as error:
            print("Invalid input:", error)

def main_delete():
    try:
        result = client.delete("/delete")

        print("DELETE request successful.")
        print("Response:", result)
    
    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return None
    except ValueError as error:
        print(f"Invalid input: {error}")
        return None

if __name__ == "__main__":
    main_get()
    main_post()
    main_put()
    main_delete()
