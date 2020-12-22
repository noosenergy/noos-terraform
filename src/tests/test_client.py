import pytest

from noos_tf import client


@pytest.fixture
def mocked_request(mocker):
    mocker.patch.object(client.TerraformClient, "_check")
    mocker.patch.object(client.TerraformClient, "_deserialize")
    return mocker.patch.object(client.TerraformClient, "_send")


@pytest.fixture
def tf_client():
    return client.TerraformClient(base_url="http://localhost/")


def test_get_workspace_id_endpoint(tf_client, mocked_request):
    tf_client.get_workspace_id("test_organisation", "test_workspace")

    mocked_request.assert_called_once()

    args, kwargs = mocked_request.call_args

    assert args[0] == "GET"
    assert args[1] == (
        "http://localhost/v2/organizations/test_organisation/workspaces/test_workspace"
    )
    assert kwargs["data"] is None
    assert kwargs["params"] is None


def test_get_variable_ids_endpoint(tf_client, mocked_request):
    tf_client.get_variable_ids("test_organisation", "test_workspace")

    mocked_request.assert_called_once()

    args, kwargs = mocked_request.call_args

    assert args[0] == "GET"
    assert args[1] == "http://localhost/v2/vars"
    assert kwargs["data"] is None
    assert kwargs["params"] == {
        "filter[organization][name]": "test_organisation",
        "filter[workspace][name]": "test_workspace",
    }


def test_update_variable_endpoint(tf_client, mocked_request):
    tf_client.update_variable("var-id", "new_value")

    mocked_request.assert_called_once()

    args, kwargs = mocked_request.call_args

    assert args[0] == "PATCH"
    assert args[1] == "http://localhost/v2/vars/var-id"
    assert kwargs["data"] == {
        "data": {"type": "vars", "id": "var-id", "attributes": {"value": "new_value"}}
    }
    assert kwargs["params"] is None


def test_run_plan_endpoint(tf_client, mocked_request):
    tf_client.run_plan("wkr-id", "msg")

    mocked_request.assert_called_once()

    args, kwargs = mocked_request.call_args

    assert args[0] == "POST"
    assert args[1] == "http://localhost/v2/runs"
    assert kwargs["data"] == {
        "data": {
            "type": "runs",
            "attributes": {"is-destroy": False, "message": "msg"},
            "relationships": {"workspace": {"data": {"type": "workspaces", "id": "wkr-id"}}},
        }
    }
    assert kwargs["params"] is None
