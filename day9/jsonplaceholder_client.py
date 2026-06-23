import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    """Fetch a user by ID."""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return response.json()


def get_posts(user_id):
    """Fetch all posts for a user."""
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    response.raise_for_status()
    return response.json()


def create_post(title, body, user_id):
    """Create a new post."""
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    response.raise_for_status()
    return response.json()
