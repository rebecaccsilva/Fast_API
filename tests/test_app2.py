from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app2 import app


def test_exerc_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo! </h1>' in response.text
