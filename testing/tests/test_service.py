import pytest,source.service as service
import unittest.mock as mock
import requests


@mock.patch("source.service.get_user_from_db")
def test_get_user(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user = service.get_user_from_db(1)
    assert user == "Mocked Alice"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Mocked User"}]
    mock_get.return_value = mock_response

    users = service.get_users()
    assert users == [{"id": 1, "name": "Mocked User"}]

@mock.patch("requests.get")
def test_get_users_http_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users()