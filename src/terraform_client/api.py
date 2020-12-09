import logging

from . import client


logger = logging.getLogger(__name__)


RUN_URL_TEMPLATE = "https://app.terraform.io/app/{organization}/workspaces/{workspace}/runs/{id}"


def update_workspace_variable(
    organization: str,
    workspace: str,
    token: str,
    variable: str,
    value: str,
) -> None:
    # Authenticate client
    tf_client = client.TerraformClient()
    tf_client.set_auth_header(token)

    # Retrieve variables IDs
    tf_vars = tf_client.get_variable_ids(organization, workspace)

    # Update variable with the new value
    tf_client.update_variable(tf_vars[variable], value)
    logger.info(f"Updated Terraform {variable!r} value to {value!r}")


def create_workspace_run(organization: str, workspace: str, token: str, message: str) -> None:
    # Authenticate client
    tf_client = client.TerraformClient()
    tf_client.set_auth_header(token)

    # Retrieve workspace ID and vairables IDs
    workspace_id = tf_client.get_workspace_id(organization, workspace)

    # Create and apply a new plan
    run_id = tf_client.create_run(workspace_id, message)
    run_url = RUN_URL_TEMPLATE.format(organization=organization, workspace=workspace, id=run_id)
    logger.info(f"Running Terraform plan for {workspace}: {run_url}")
