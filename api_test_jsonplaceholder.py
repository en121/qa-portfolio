import requests

# 測試 GET 請求
def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    data = response.json()
    print("GET Post Title:", data['title'])

# 測試 POST 請求
def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    print("Created Post ID:", data['id'])

if __name__ == "__main__":
    test_get_post()
    test_create_post()
