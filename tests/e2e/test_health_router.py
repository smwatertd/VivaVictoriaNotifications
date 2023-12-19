from fastapi.testclient import TestClient


class TestHealthRouter:
    def test_check_health_status_code(self, client: TestClient) -> None:
        response = client.get('/health')
        assert response.status_code == 200

    def test_check_health(self, client: TestClient) -> None:
        response = client.get('/health')
        assert response.json() == {'status': 'ok'}
