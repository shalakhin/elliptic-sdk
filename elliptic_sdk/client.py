"""Elliptic SDK elliptic_sdk/client.py."""
from httpx import Client
from .settings import settings


def get_client():
    """Get HTTPX client.

    Returns:
        HTTPX Client instance with predefined headers.
    """
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
    }
    return Client(headers=headers, timeout=settings.timeout)
