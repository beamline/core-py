import pytest


@pytest.mark.first
def test_miners(test_client):
    response = test_client.get('/api/v1/miners')
    pytest.miner_id = response.json[0]["id"]

    assert response.status_code == 200
    assert "configurationParameters" in str(response.data)
