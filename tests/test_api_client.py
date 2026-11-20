
import pytest
import requests
from unittest.mock import Mock

from api_client import APIClient


@pytest.fixture
def client(monkeypatch):
    """Create an API client with a test token."""
    monkeypatch.setenv("API_TOKEN", "test-token-123")
    return APIClient("https://api.example.com/")


def mock_response():
    """Create a simulated successful API response."""
    response = Mock()
    response.status_code = 200
    response.content = b'{"message": "success"}'
    response.json.return_value = {"message": "success"}
    return response


# -------------------------
# Successful request tests
# -------------------------

def test_get_request(client):
    response = mock_response()
    client.session.get = Mock(return_value=response)

    result = client.get("/products")

    assert result == {"message": "success"}
    client.session.get.assert_called_once_with(
        "https://api.example.com/products",
        timeout=10
    )


def test_post_request(client):
    response = mock_response()
    client.session.post = Mock(return_value=response)

    payload = {"name": "Laptop", "price": 1500}

    result = client.post("/products", payload)

    assert result == {"message": "success"}
    client.session.post.assert_called_once_with(
        "https://api.example.com/products",
        json=payload,
        timeout=10
    )


def test_put_request(client):
    response = mock_response()
    client.session.put = Mock(return_value=response)

    payload = {"name": "Updated Laptop", "price": 1800}

    result = client.put("/products/1", payload)

    assert result == {"message": "success"}
    client.session.put.assert_called_once_with(
        "https://api.example.com/products/1",
        json=payload,
        timeout=10
    )


def test_delete_request(client):
    response = mock_response()
    client.session.delete = Mock(return_value=response)

    result = client.delete("/products/1")

    assert result == {"message": "success"}
    client.session.delete.assert_called_once_with(
        "https://api.example.com/products/1",
        timeout=10
    )


# -------------------------
# Authentication tests
# -------------------------

def test_bearer_token_is_set_in_headers(client):
    assert client.session.headers["Authorization"] == "Bearer test-token-123"


def test_missing_api_token(monkeypatch):
    monkeypatch.delenv("API_TOKEN", raising=False)

    with pytest.raises(ValueError, match="API_TOKEN is missing or empty"):
        APIClient("https://api.example.com")


# -------------------------
# Input validation tests
# -------------------------

@pytest.mark.parametrize("endpoint", ["", "   ", None, 123])
def test_invalid_endpoint(client, endpoint):
    with pytest.raises(ValueError):
        client.get(endpoint)


@pytest.mark.parametrize("payload", ["invalid", None, 123, []])
def test_invalid_post_payload(client, payload):
    with pytest.raises(TypeError):
        client.post("/products", payload)


@pytest.mark.parametrize("payload", ["invalid", None, 123, []])
def test_invalid_put_payload(client, payload):
    with pytest.raises(TypeError):
        client.put("/products/1", payload)


# -------------------------
# Error handling tests
# -------------------------

def test_http_error(client):
    response = mock_response()
    response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "500 Server Error"
    )

    with pytest.raises(requests.exceptions.HTTPError):
        client._handle_response(response)


def test_invalid_json_response(client):
    response = mock_response()
    response.json.side_effect = requests.exceptions.JSONDecodeError(
        "Invalid JSON", "not-json", 0
    )

    with pytest.raises(ValueError, match="API returned an invalid JSON response"):
        client._handle_response(response)


# -------------------------
# Empty response tests
# -------------------------

def test_empty_response(client):
    response = mock_response()
    response.content = b""

    result = client._handle_response(response)

    assert result is None


def test_no_content_response(client):
    response = mock_response()
    response.status_code = 204

    result = client._handle_response(response)

    assert result is None
