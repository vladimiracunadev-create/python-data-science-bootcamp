from app.app import app


def test_index_loads():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'Entorno Interactivo del Bootcamp Python' in response.get_data(as_text=True)


def test_execute_api_runs_code():
    client = app.test_client()
    response = client.post('/api/execute', json={'notebook_id': 'api-test', 'code': '2 + 3'})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == '5'
