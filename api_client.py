import os
import requests
from dotenv import load_dotenv

load_dotenv()

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.token = os.getenv("API_TOKEN")
        self.session = requests.Session()

        if not self.token or not self.token.strip():
            raise ValueError("API_TOKEN is missing or empty.")

        self.session.headers.update({
            "Authorization": f"Bearer {self.token.strip()}",
            "Accept": "application/json"
        })

    
    def _handle_response(self, response):
        response.raise_for_status()

        if response.status_code == 204 or not response.content:
            return None

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as error:
            raise ValueError("API returned an invalid JSON response.") from error
        

    def get(self, endpoint):
        if not isinstance(endpoint, str) or not endpoint.strip():
            raise ValueError("Endpoint must not be an empty string.")
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        response = self.session.get(url, timeout=10)
        
        return self._handle_response(response)
 

    def post(self, endpoint, payload):
        if not isinstance(endpoint, str) or not endpoint.strip():
            raise ValueError("Endpoint must not be an empty string.")
        if not isinstance(payload, dict):
            raise TypeError("Payload must be a dictionary.")
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = self.session.post(
            url,
            json=payload,
            timeout=10
        )

        return self._handle_response(response)


    def put(self, endpoint, payload):
        if not isinstance(endpoint, str) or not endpoint.strip():
            raise ValueError("Endpoint must not be an empty string.")
        if not isinstance(payload, dict):
            raise TypeError("Payload must be a dictionary.")
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = self.session.put(
            url,
            json=payload,
            timeout=10
        )

        return self._handle_response(response)


    def delete(self, endpoint):
        if not isinstance(endpoint, str) or not endpoint.strip():
            raise ValueError("Endpoint must not be an empty string.")
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = self.session.delete(url, timeout=10)

        return self._handle_response(response)


    