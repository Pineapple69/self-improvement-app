USERNAME = "username"
PASSWORD = "password"


def test_user_signup_login_logout(api_client, app_url):
    res = api_client.post(
        f"{app_url}/users/signup",
        json=dict(
            username=USERNAME, password=PASSWORD, first_name="", last_name=""
        ),
    )
    assert res.status_code == 200
    assert res.json["message"] == f"{USERNAME} signed up successfully"

    res = api_client.post(
        f"{app_url}/users/login",
        json=dict(username=USERNAME, password=PASSWORD),
    )
    assert res.status_code == 200
    assert res.json["message"] == f"{USERNAME} successfully logged in"

    res = api_client.post(
        f"{app_url}/users/logout",
        json=dict(username=USERNAME, password=PASSWORD),
    )
    assert res.status_code == 200
    assert res.json["message"] == "User logged out successfully"
