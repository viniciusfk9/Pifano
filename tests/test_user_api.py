def test_cannot_add_user_if_exists(client):
    """Asserts an user cannot be created if already exists"""
    user = {"name": "test", "email": "test@test", "password": "test"}
    r = client.post('/users', json=user)

    assert r.json['message'] == "Email already registered."


def test_can_add_user(client):
    """Asserts an user can be created"""

    user = {"name": "Teste", "email": "teste@teste.com", "password": "123456"}
    r = client.post('/users', json=user)

    assert r.json['message'] == "User Teste has been created successfully."


def test_can_list_users(client):
    """Asserts users can be listed"""
    users = client.get('/users')

    assert users.status_code == 200
    assert 'users' in users.json
