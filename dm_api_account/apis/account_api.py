import allure
from requests import Response
# from apis.dm_api_account.models import userenvelop
from dm_api_account.models import *
from restclient.restclient import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def get_v1_account(self, status_code: int = 200, **kwargs) -> UserEnvelope | Response:
        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        validate_status_code(response, status_code)
        return response

    def post_v1_account(self, json: Registration, status_code=201, **kwargs) -> Response:

        with allure.step("Register of new user"):
            response = self.client.post(
                path=f"/v1/account",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, status_code)
        return response

    def post_account_password_change(self, json: Registration, status_code: int, **kwargs) -> UserEnvelope | Response:
        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        return response

    def put_v1_account_token(self, token: str, status_code=200, **kwargs):
        with allure.step("Activate of register user"):
            response = self.client.put(
                path=f"/v1/account/{token}",
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_account_email(self, json: ChangeEmail, status_code: int, **kwargs) -> Response:
        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        return response

    def post_account_password_reset(self, json: ResetPassword, status_code=200, **kwargs) -> UserEnvelope | Response:
        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response
