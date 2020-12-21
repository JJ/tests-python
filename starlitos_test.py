from starlette.responses import JSONResponse
from starlette.testclient import TestClient
from HitosIV.starlitos import rutas

def test_should_have_correct_API():
    client = TestClient(rutas)
    response = client.get('/hitos')
    assert response.status_code == 200
    data = response.json()
    print(data)
    for i in ['hitos','comment']:
        assert data[i]
