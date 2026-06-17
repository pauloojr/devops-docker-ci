from app.main import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_products_endpoint():
    client = app.test_client()
    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.get_json()) == 2