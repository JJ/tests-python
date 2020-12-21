from unittest import TestCase
from starlette.responses import JSONResponse
from starlette.testclient import TestClient
from HitosIV.starlitos import rutas

class StarletteTesting(TestCase):

    def __init__(self, *args, **kwargs):
        super(StarletteTesting, self).__init__(*args, **kwargs)
        self.client = TestClient(rutas)

    def test_should_have_correct_API( self ):
        client = self.client
        response = client.get('/hitos')
        assert response.status_code == 200
        data = response.json()
        print(data)
        for i in ['hitos','comment']:
            assert data[i]
