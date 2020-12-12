import pytest
from invoke import context

from noos_tf import cli


@pytest.fixture
def ctx():
    return context.Context()


@pytest.fixture(
    params=[
        (None, "test_token"),
        ("test_organisation", None),
    ]
)
def secrets(request):
    return request.param


class TestUpdate:
    def test_invalid_credentials_raise_error(self, ctx, secrets):
        with pytest.raises(AssertionError):
            cli.update(ctx, organisation=secrets[0], token=secrets[1])


class TestRun:
    def test_invalid_credentials_raise_error(self, ctx, secrets):
        with pytest.raises(AssertionError):
            cli.run(ctx, organisation=secrets[0], token=secrets[1])
