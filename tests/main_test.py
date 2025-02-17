"""Test cases for the main module."""
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client  = TestClient(app)


def test_main_index():
    """Test that the index endpoint returns the correct response."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
