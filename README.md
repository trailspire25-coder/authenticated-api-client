# Authenticated API Client

A reusable Python API client that communicates with REST APIs using
Bearer Token Authentication.

The client supports GET, POST, PUT, and DELETE requests, with
centralized response handling, input validation, timeout protection,
and exception handling.


## Features

- Supports GET, POST, PUT, and DELETE HTTP methods.
- Bearer Token Authentication.
- Environment variable configuration using python-dotenv.
- Persistent HTTP sessions using requests.Session().
- Centralized HTTP response handling.
- HTTP status code validation.
- JSON response processing.
- Input and endpoint validation.
- Request timeout protection.
- Exception handling for HTTP errors and invalid JSON responses.
- Handles empty responses and HTTP 204 (No Content).


## Technologies Used

- **Python 3** – Core programming language.
- **Requests** – Sending HTTP requests and managing API sessions.
- **python-dotenv** – Loading authentication credentials from environment variables.
- **HTTP/REST APIs** – Communication with external services.
- **httpbin.org** – Testing API requests and responses.


## Project Structure

```text
Authenticated_Api_Client/
│
├── api_client.py       # Reusable API client implementation
├── main.py             # Demonstrates API client functionality
├── .env                # Stores API authentication token (not committed)
├── .gitignore          # Excludes sensitive and unnecessary files
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```


## Installation and Setup

### 1. Clone the repository

git clone https://github.com/trailspire25-coder/authenticated-api-client.git

### 2. Navigate into the project directory

cd Authenticated_Api_Client

### 3. Create a virtual environment

python -m venv .venv

### 4. Activate the virtual environment

Windows:

.venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Configure environment variables

Create a `.env` file in the project root directory.

Add your API token:

API_TOKEN=your_api_token_here

### 7. Run the application

python main.py


## Usage

The API client supports GET, POST, PUT, and DELETE requests.

Example:

    from api_client import APIClient

    client = APIClient("https://api.example.com")

    response = client.get("/products")

    print(response)


## Security

API credentials are stored in environment variables
and are not hardcoded into the application.

The `.env` file is excluded from version control.


## Future Improvements

- Automated unit tests
- Support for additional authentication methods
- Improved logging
- Expanded API response handling