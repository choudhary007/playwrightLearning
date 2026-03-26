from utils.api_client import APIClient

def test_get_users():
    client = APIClient()

    response = client.get("https://jsonplaceholder.typicode.com/users")
    print(response.status_code)
    assert response.status_code == 200

def test_post_users():
    client = APIClient()
    payload = {
        "name": "Deepak",
        "job": "QA Automation"
    }

    response = client.post("https://jsonplaceholder.typicode.com/users", payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == "Deepak"
    