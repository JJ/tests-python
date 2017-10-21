import hug
import hugitos


data = hug.test.get(hugitos, '/all')

def test_should_have_correct_API():
    assert data.status == "200 OK"
    assert data.data['hitos']['hitos'][0]['file'] == "0.Repositorio"
