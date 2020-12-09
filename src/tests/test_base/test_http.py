import random

import pytest
import requests

from terraform_client.base import http_client


@pytest.fixture
def error_status_code():
    return random.randrange(400, 600)


class TestJSONClient:
    def test_initiate_connection(self):
        client = http_client.JSONClient("http://test_url")

        assert client._conn is None
        assert isinstance(client.conn, requests.Session)
        assert client._conn is not None


class TestCheckResponse:
    def test_bad_request_raises_error(self, error_status_code, mocker):
        response = requests.Response()
        mocker.patch.object(response, "status_code", error_status_code)

        with pytest.raises(http_client.HTTPError):
            http_client._check_response(response)

    def test_mismatched_code_raises_error(self, mocker):
        response = requests.Response()
        mocker.patch.object(response, "status_code", 201)

        with pytest.raises(http_client.HTTPError):
            http_client._check_response(response, statuses=(200,))


class TestDeserializeResponse:
    def test_no_json_content_raises_error(self, mocker):
        mocked_response = mocker.Mock()
        mocked_response.headers = {}
        mocked_response.status_code = 200

        with pytest.raises(http_client.ClientError):
            http_client._deserialize_response(mocked_response)

    def test_response_without_json_content(self, mocker):
        mocked_response = mocker.Mock()
        mocked_response.headers = {}
        mocked_response.status_code = 204

        assert http_client._deserialize_response(mocked_response) == {}

    def test_response_with_json_content(self, mocker):
        mocked_response = mocker.Mock()
        mocked_response.headers = {"content-type": "application/json"}
        mocked_response.status_code = 200

        http_client._deserialize_response(mocked_response)

        mocked_response.json.assert_called_once()
