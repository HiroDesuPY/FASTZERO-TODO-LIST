from http import HTTPStatus


def test_root_deve_retornar_hello_world(client):

    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def testando_route_html(client):

    response = client.get('/lista')

    assert response.status_code == HTTPStatus.CREATED
    assert '<h1>Lista-1</h1>' in response.text


def test_create_user(client):

    response = client.post(
        '/users',
        json={
            'username': 'Alice',
            'email': 'alice@gmail.com',
            'senha': 'alicesenha',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Alice',
        'email': 'alice@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Alice',
                'email': 'alice@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_users(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }
