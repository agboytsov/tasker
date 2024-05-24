import json

import pytest

from conftest import client


def test_ping(client):
    """Тест, работает ли сервер"""
    resp = client.get('/')
    assert resp.status_code == 200


class TestTasks:

    @pytest.mark.parametrize(
        "title, description, status_code",
        [
            ("Title1", "Description", 201),  # Обычный случай
            ("Title2", "Description" * 10, 201),  # Случай с длинным описанием
            ("Title2", "", 201),  # Случай без описания
            ("", "", 201)  # Тоже пройдет, т.к. в api нет проверки данных
        ]
    )
    def test_create(self, client, title, description, status_code):
        dct = {'title': title, 'description': description}
        resp = client.post('/api/tasks', data=json.dumps(dct), headers={'Content-Type': 'application/json'})
        assert resp.status_code == status_code

    @pytest.mark.parametrize(
        "add_all, status_code",
        [
            (False, 404),  # Проверяем случай, когда нет статей
            (True, 200)  # Проверяем случай, когда есть статьи
        ]
    )
    def test_get_all(self, client, add_all, status_code):
        if not add_all:
            resp = client.get('/api/tasks')
            assert resp.status_code == status_code
        else:
            dct = {'title': 'SampleTitle', 'description': 'Sample Description'}
            client.post('/api/tasks', data=json.dumps(dct), headers={'Content-Type': 'application/json'})
            resp = client.get('/api/tasks')
            assert resp.status_code == status_code

    @pytest.mark.parametrize(
        "article, status_code",
        [
            (1, 200),
            (2, 404),
            (0, 404)
        ]
    )
    def test_get_article(self, client, article, status_code):
        dct = {'title': 'SampleTitle', 'description': 'Sample Description'}
        client.post('/api/tasks', data=json.dumps(dct), headers={'Content-Type': 'application/json'})
        resp = client.get(f'/api/tasks/{article}')
        assert resp.status_code == status_code


    @pytest.mark.parametrize(
        "article, status_code, new_title, new_description",
        [
            (1, 201, 'NEWTITLE', "IT IS NOT A DESCRIPTION"),
            (2, 404, "", "")
        ]
    )
    def test_update_article(self, client, article, status_code, new_title, new_description):
        dct = {'title': 'SampleTitle', 'description': 'Sample Description'}
        client.post('/api/tasks', data=json.dumps(dct), headers={'Content-Type': 'application/json'})
        new_dct = {'title': new_title, 'description': new_description}
        resp = client.put(f'/api/tasks/{article}',
                          headers={'Content-Type': 'application/json'},
                          data=json.dumps(new_dct))
        if new_title and new_description:
            assert resp.json['title'] == new_title and resp.json['description'] == new_description and status_code == status_code
        assert resp.status_code == status_code


    @pytest.mark.parametrize(
        "article, status_code",
        [
            (1, 204),
            (2, 404),
            (0, 404)
        ]
    )
    def test_get_article(self, client, article, status_code):
        dct = {'title': 'SampleTitle', 'description': 'Sample Description'}
        client.post('/api/tasks', data=json.dumps(dct), headers={'Content-Type': 'application/json'})
        resp = client.delete(f'/api/tasks/{article}')
        assert resp.status_code == status_code
