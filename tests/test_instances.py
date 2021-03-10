import pytest


def test_instance_create_failure(test_client):
    response = test_client.post('/api/v1/instances/RND', json={
        "name": "string",
        "stream": {
            "processName": "string",
            "brokerHost": "string",
            "topicBase": "string"
        },
        "parameterValues": []
    })
    assert response.status_code == 404


@pytest.mark.run(after='test_miners')
def test_instance_create(test_client):
    response = test_client.post('/api/v1/instances/' + pytest.miner_id, json={
        "name": "instance1",
        "stream": {
            "processName": "string",
            "brokerHost": "string",
            "topicBase": "string"
        },
        "parameterValues": []
    })
    pytest.instance_id = response.json["id"]
    assert response.status_code == 200


@pytest.mark.run(after='test_instance_create')
def test_instance_list(test_client):
    response = test_client.get('/api/v1/instances')
    assert pytest.instance_id in response.get_data(as_text=True)
    assert response.status_code == 200


@pytest.mark.run(before='test_instance_start')
def test_instance_not_mining(test_client):
    response = test_client.get('/api/v1/instances/' + pytest.instance_id + '/status')
    assert response.get_data(as_text=True) == "not_mining"
    assert response.status_code == 200


def test_instance_start(test_client):
    response = test_client.get('/api/v1/instances/' + pytest.instance_id + '/start')
    assert response.get_data(as_text=True) == "true"
    assert response.status_code == 200


@pytest.mark.run(after='test_instance_start')
def test_instance_mining(test_client):
    response = test_client.get('/api/v1/instances/' + pytest.instance_id + '/status')
    assert response.get_data(as_text=True) == "mining"
    assert response.status_code == 200


@pytest.mark.run(after='test_instance_mining')
def test_instance_stop(test_client):
    response = test_client.get('/api/v1/instances/' + pytest.instance_id + '/stop')
    assert response.get_data(as_text=True) == "true"
    assert response.status_code == 200


@pytest.mark.run(after='test_instance_stop')
def test_instance_not_mining2(test_client):
    response = test_client.get('/api/v1/instances/' + pytest.instance_id + '/status')
    assert response.get_data(as_text=True) == "not_mining"
    assert response.status_code == 200


@pytest.mark.run(after='test_instance_not_mining2')
def test_instance_delete(test_client):
    response = test_client.delete('/api/v1/instances/' + pytest.instance_id + '/delete')
    assert response.status_code == 200


@pytest.mark.run(after='test_instance_delete')
def test_instance_list2(test_client):
    response = test_client.get('/api/v1/instances')
    assert pytest.instance_id not in response.get_data(as_text=True)
    assert response.status_code == 200