from terraform_client.base import auth_client


class TestCredentials:
    def test_token_auth(self):
        token = "test_token"
        client = auth_client.AuthClient("http://localhost/")

        client.set_auth_header(token)
        headers = client.conn.headers

        assert auth_client.HTTPTokenAuth.default_header in headers
        assert headers[auth_client.HTTPTokenAuth.default_header] == f"Token {token}"
