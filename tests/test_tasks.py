import json
import time

import pytest

from conftest import app


def test_ping(app):
    client = app.test_client()
    resp = client.get('/')
    time.sleep(30)
    assert resp.status_code == 200

@pytest.mark.parametrize(
        "title, description, status_code",
        [
("Title1", "Description", 201),
("Title2", "Description"*10, 201),
("Title2", "", 201),
("", "", 201),
        ]
)
def test_create(app, title, description, status_code):
    client = app.test_client()
    dct = {'title': title, 'description':description}
    resp = client.post('/api/tasks', data=json.dumps(dct), headers={'Content-Type': 'application/json'})
    assert resp.status_code == status_code


# @pytest.mark.parametrize(
#         "task, status_code",
#         [
# (1, 200),
#         ]
# )
# def test_get(app, task, status_code):
#     resp = client.get(f'/api/tasks/{task}')
#     assert resp.status_code == status_code
# def test_all_tasks(app):
#     client = app.test_client()
#     resp = client.get('/api/tasks')
#     assert resp.status_code == 200