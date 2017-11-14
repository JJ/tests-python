import hug
import hugitos

def test_status_should_return_OK():
    data = hug.test.get(hugitos, '/')
    assert data.status == "200 OK"
    assert data.data['status']== "OK"
    data = hug.test.get(hugitos, '/status')
    assert data.status == "200 OK"
    assert data.data['status']== "OK"

def test_should_have_correct_API():
    data = hug.test.get(hugitos, '/all')
    assert data.status == "200 OK"
    assert data.data['hitos']['hitos'][0]['file'] == "0.Repositorio"

def test_should_return_at_least_one_element():
    data = hug.test.get(hugitos, '/one/0')
    assert data.status == "200 OK"
    assert data.data['hito']['file'] == "0.Repositorio"
