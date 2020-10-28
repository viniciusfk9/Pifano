def test_login_success(client):
    user = {"email": "test@test", "password": "test"}
    r = client.post('/login', json=user, follow_redirects=True)

    assert b"User successfully logged in" in r.data


def test_login_invalid(client):
    user = {"email": "test@test", "password": "123456"}
    r = client.post('/login', json=user, follow_redirects=True)

    assert b"Username or password is invalid" in r.data


def test_logout(client):
    r = client.post('/logout')

    assert b"User successfully logged out" in r.data
