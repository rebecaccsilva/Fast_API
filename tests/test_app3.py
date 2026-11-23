from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # Arrange(organização)
    response = client.get("/")  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Olá Mundo!"}  # assert


def test_creat_user(client):
    response = client.post(  # UserSchema
        "/users/",
        json={
            "username": "testusersname",
            "password": "password",
            "email": "tes@test.com",
        },
    )

    # Voltou o status code certo?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPUblic
    assert response.json() == {
        "username": "testusersname",
        "email": "tes@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testusersname",
                "email": "tes@test.com",
                "id": 1,
            }
        ]
    }
