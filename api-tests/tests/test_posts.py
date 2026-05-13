import requests
import jsonschema

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"}
    },
    "required": ["id", "title", "body", "userId"]
}

def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_get_single_post_valid_id(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    post = response.json()
    jsonschema.validate(instance=post, schema=POST_SCHEMA)
    assert post["id"] == 1

def test_get_single_post_not_found(base_url):
    response = requests.get(f"{base_url}/posts/99999")
    assert response.status_code == 404

def test_create_post(base_url):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 101
    assert data["title"] == "foo"

def test_update_post(base_url):
    payload = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    response = requests.put(f"{base_url}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"

def test_patch_post(base_url):
    response = requests.patch(f"{base_url}/posts/1", json={"title": "patched"})
    assert response.status_code == 200
    assert response.json()["title"] == "patched"

def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}

def test_response_content_type(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert "application/json" in response.headers["Content-Type"]
