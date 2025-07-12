# API Test Automation – JSONPlaceholder API

This project tests the fake REST API endpoints from https://jsonplaceholder.typicode.com using `pytest` and `requests`.

## 📁 Folder Structure

api_test_automation/
├── tests/ # Test cases
├── config/ # Config file with base URL
├── reports/ # HTML test reports
├── requirements.txt # Python dependencies
└── README.md # Project instructions


## ✅ Tested Endpoints

- `POST /posts` – Create a post
- `GET /posts` – Get all posts
- `GET /posts/:id` – Get post by ID
- `PUT /posts/:id` – Update a post
- `DELETE /posts/:id` – Delete a post

## ❌ Negative Tests

- Fetching invalid post ID
- Sending invalid payload

## 🧪 How to Run Tests

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run tests and generate HTML report:
    ```bash
    pytest --html=reports/report.html --self-contained-html
    ```

3. Open the report:
    - Navigate to `reports/report.html`

## 📄 Output

Each test validates:
- Status codes (200, 201, 404, etc.)
- JSON structure and keys
- Correct error behavior for negative scenarios

---
🔗 API Endpoints Covered
Method	Endpoint	Description
GET	/posts	Get all posts
GET	/posts/{id}	Get post by ID
POST	/posts	Create a new post
PUT	/posts/{id}	Update a post
DELETE	/posts/{id}	Delete a post

✅ Test Cases
🟢 Positive Test Scenarios
ID	Test Case Title	Method & Endpoint	Expected Outcome
TC_001	Create a Post	POST /posts	201 Created; returns new post with ID
TC_002	Get All Posts	GET /posts	200 OK; returns list of posts
TC_003	Get Post by Valid ID	GET /posts/1	200 OK; returns post with id=1
TC_004	Update Post	PUT /posts/1	200 OK; title/body updated in response
TC_005	Delete Post	DELETE /posts/1	200 OK; empty response {}

🔴 Negative Test Scenarios
ID	Test Case Title	Method & Endpoint	Input	Expected Outcome
TC_006	Get Post with Invalid ID	GET /posts/999999	-	404 Not Found or {}
TC_007	Create Post with Invalid Payload	POST /posts	"invalid-json"	400/500 error
TC_008	Update Non-existent Post	PUT /posts/999999	id=999999, new data	200 OK (API accepts all PUTs)
TC_009	Delete Non-existent Post	DELETE /posts/999999	-	200 OK (API deletes any ID)
TC_010	Create Post Without Fields	POST /posts	{ "title": "missing" }	201 Created (API allows it)

📊 Sample Output Summary (pytest)
Test	Status
test_create_post	✅ Passed
test_get_posts_list	✅ Passed
test_get_post_by_id	✅ Passed
test_update_post	✅ Passed
test_delete_post	✅ Passed
test_get_invalid_post	✅ Passed
test_create_post_invalid_payload	✅ Passed