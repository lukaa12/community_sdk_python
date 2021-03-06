from http import HTTPStatus

from kentik_api.api_calls.api_call import APICallMethods
from kentik_api.public.user import User


def test_create_user_success(client, connector) -> None:
    # given
    create_response_payload = """
    {
        "user": {
                    "id":"145985",
                    "username":"test@user.example",
                    "user_full_name":"Test User",
                    "user_email":"test@user.example",
                    "role":"Member",
                    "email_service":"true",
                    "email_product":"true",
                    "last_login":null,
                    "created_date":"2020-12-09T14:33:28.330Z",
                    "updated_date":"2020-12-09T14:33:28.369Z",
                    "company_id":"74333",
                    "user_api_token":null,
                    "filters":{},
                    "saved_filters":[]
                }
    }"""
    connector.response_text = create_response_payload
    connector.response_code = HTTPStatus.CREATED

    # when
    user = User(full_name="Test User", email="test@user.example", role="Member", email_service=True, email_product=True)
    created = client.users.create(user)

    # then request properly formed
    assert connector.last_url == "/user"
    assert connector.last_method == APICallMethods.POST
    assert connector.last_payload is not None
    assert "user" in connector.last_payload
    assert connector.last_payload["user"]["user_full_name"] == "Test User"
    assert connector.last_payload["user"]["user_email"] == "test@user.example"
    assert connector.last_payload["user"]["role"] == "Member"
    assert connector.last_payload["user"]["email_service"] is True
    assert connector.last_payload["user"]["email_product"] is True

    # and response properly parsed
    assert created.id == 145985
    assert created.username == "test@user.example"
    assert created.full_name == "Test User"
    assert created.email == "test@user.example"
    assert created.company_id == 74333
    assert created.role == "Member"
    assert created.password is None
    assert created.email_service is True
    assert created.email_product is True
    assert created.api_token is None


def test_get_user_success(client, connector) -> None:
    # given
    get_response_payload = """
        {
            "user": {
                        "id":"145999",
                        "username":"test@user.example",
                        "user_full_name":"Test User",
                        "user_email":"test@user.example",
                        "role":"Member",
                        "email_service":true,
                        "email_product":true,
                        "last_login":null,
                        "created_date":"2020-12-09T14:48:42.187Z",
                        "updated_date":"2020-12-09T14:48:43.243Z",
                        "company_id":"74333",
                        "user_api_token":"****************************a997",
                        "filters":{},
                        "saved_filters":[]
                    }
        }"""
    connector.response_text = get_response_payload
    connector.response_code = HTTPStatus.OK

    # when
    user_id = 145999
    user = client.users.get(user_id)

    # then request properly formed
    assert connector.last_url == f"/user/{user_id}"
    assert connector.last_method == APICallMethods.GET
    assert connector.last_payload is None

    # then response properly parsed
    assert int(user.id) == 145999
    assert user.username == "test@user.example"
    assert user.full_name == "Test User"
    assert user.email == "test@user.example"
    assert user.company_id == 74333
    assert user.role == "Member"
    assert user.password is None
    assert user.email_service is True
    assert user.email_product is True
    assert user.api_token == "****************************a997"


def test_update_user_success(client, connector) -> None:
    # given
    update_response_payload = """
    {
        "user":{
                "id":"146034",
                "username":"test@user.example",
                "user_full_name":"User Testing",
                "user_email":"test@user.example",
                "role":"Member",
                "email_service":true,
                "email_product":true,
                "last_login":null,
                "created_date":"2020-12-09T15:23:29.768Z",
                "updated_date":"2020-12-09T15:23:31.108Z",
                "company_id":"74333",
                "user_api_token":null,
                "filters":{},
                "saved_filters":[]
               }
    }"""
    connector.response_text = update_response_payload
    connector.response_code = HTTPStatus.OK

    # when
    user_id = 146034
    user = User(
        id=user_id,
        full_name="User Testing",
    )
    updated = client.users.update(user)

    # then request properly formed
    assert connector.last_url == f"/user/{user_id}"
    assert connector.last_method == APICallMethods.PUT
    assert connector.last_payload is not None
    assert "user" in connector.last_payload
    assert connector.last_payload["user"]["user_full_name"] == "User Testing"

    # then response properly parsed
    assert updated.id == 146034
    assert updated.full_name == "User Testing"
    assert updated.email == "test@user.example"


def test_delete_user_success(client, connector) -> None:
    # given
    delete_response_payload = ""  # deleting user responds with empty body
    connector.response_text = delete_response_payload
    connector.response_code = HTTPStatus.NO_CONTENT

    # when
    user_id = 146034
    delete_successful = client.users.delete(user_id)

    # then request properly formed
    assert connector.last_url == f"/user/{user_id}"
    assert connector.last_method == APICallMethods.DELETE
    assert connector.last_payload is None

    # then response properly parsed
    assert delete_successful
