import pytest
from invoke import context

from noos_tf import cli


@pytest.fixture
def ctx():
    return context.Context()


class TestUpdate:
    @pytest.mark.parametrize(
        "organisation,token",
        [
            (None, "test_token"),
            ("test_organisation", None),
        ],
    )
    def test_invalid_credentials_raise_error(self, ctx, organisation, token):
        with pytest.raises(AssertionError):
            cli.update(ctx, organisation=organisation, token=token)


class TestRun:
    @pytest.mark.parametrize(
        "organisation,token",
        [
            (None, "test_token"),
            ("test_organisation", None),
        ],
    )
    def test_invalid_credentials_raise_error(self, ctx, organisation, token):
        with pytest.raises(AssertionError):
            cli.run(ctx, organisation=organisation, token=token)
