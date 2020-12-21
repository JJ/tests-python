from starlette.responses import HTMLResponse
from starlette.testclient import TestClient
from HitosIV.starlitos import rutas

def test_should_have_correct_API():
    client = TestClient(rutas)
    response = client.get('/hitos')
    assert response.status_code == 200
