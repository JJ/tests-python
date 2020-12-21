from unittest import TestCase
from starlette.responses import JSONResponse
from starlette.testclient import TestClient
from HitosIV.starlitos import rutas

class StarletteTesting(TestCase):

    def __init__(self, *args, **kwargs):
        super(StarletteTesting, self).__init__(*args, **kwargs)
        self.client = TestClient(rutas)

    def test_should_return_all_items( self ):
        client = self.client
        response = client.get('/hitos')
        assert response.status_code == 200
        data = response.json()
        for i in ['hitos','comment']:
            assert data[i]

    def test_should_be_able_to_create_one( self ):
        client = self.client
        URI = '/hitos/5.REST'
        response = client.put(URI,
                              data = { 'title' : 'Trabajando con REST',
                                       'fecha' : '22/01/2021'}
        )
        assert response.status_code == 201
        data = response.json()
        for i in ['file','title','fecha']:
            assert data[i]
        new_location = response.headers['Location']
        assert new_location == URI
        response = client.get(new_location)
        assert response.status_code == 200
        data = response.json()
        for i in ['file','title','fecha']:
            assert data[i]

    def test_should_be_able_to_create_via_post( self ):
        client = self.client
        response = client.post("/hitos",
                               data = { 'title' : 'Trabajando con REST más',
                                        'fecha' : '24/01/2021'}
        )
        assert response.status_code == 201
        data = response.json()
        for i in ['file','title','fecha']:
            assert data[i]
        new_location = response.headers['Location']
        print(new_location)
        response = client.get(new_location)
        assert response.status_code == 200
        data = response.json()
        for i in ['file','title','fecha']:
            assert data[i]
