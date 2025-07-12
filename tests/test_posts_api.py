import requests
import pytest
import json
import os

with open(os.path.join("config", "config.json")) as f:
    config = json.load(f)
BASE_URL = config["base_url"]

headers = {'Content-type': 'application/json; charset=UTF-8'}

def test_create_post():
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data, headers=headers)
    assert response.status_code == 201
    resp_json = response.json()
    assert resp_json["title"] == "foo"
    assert "id" in resp_json



def test_get_posts_list():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)



def test_get_post_by_id():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == post_id



def test_update_post():
    post_id = 1
    updated_data = {"id": post_id, "title": "updated", "body": "new body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "updated"




def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200





# ----------------- Negative Tests ----------------- #

def test_get_invalid_post():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404 or response.status_code == 200  # jsonplaceholder returns empty object for invalid id
    assert response.json() == {}

def test_create_post_invalid_payload():
    response = requests.post(f"{BASE_URL}/posts", data="invalid-json", headers=headers)
    assert response.status_code in (400, 500)
