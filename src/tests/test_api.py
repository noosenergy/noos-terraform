import pytest

from noos_tf import api, client


class TestUpdateWorkspaceVariable:
    def test_unknown_variable_raises_error(self, mocker):
        mocked_vars = {"test_variable": "var-id"}
        mocker.patch.object(client.TerraformClient, "get_variable_ids", return_value=mocked_vars)

        with pytest.raises(api.TerraformError):
            api.update_workspace_variable("", "", "", "bad_variable", "new_value")

    def test_update_correctly_plan_variable(self, mocker):
        mocked_vars = {"test_variable": "var-id"}
        mocker.patch.object(client.TerraformClient, "get_variable_ids", return_value=mocked_vars)
        mocked_update = mocker.patch.object(
            client.TerraformClient, "update_variable", return_value="run-id"
        )

        api.update_workspace_variable("", "", "", "test_variable", "new_value")

        mocked_update.assert_called_with("var-id", "new_value")


class TestRunWorkspacePlan:
    def test_return_correctly_formatted_plan_url(self, mocker):
        expected_url = (
            "https://app.terraform.io/app/test_organization/"
            "workspaces/test_workspace/runs/run-id"
        )
        mocker.patch.object(client.TerraformClient, "get_workspace_id", return_value="wkr-id")
        mocked_run = mocker.patch.object(client.TerraformClient, "run_plan", return_value="run-id")

        url = api.run_workspace_plan("test_organization", "test_workspace", "", "test message")

        mocked_run.assert_called_with("wkr-id", "test message")
        assert url == expected_url
