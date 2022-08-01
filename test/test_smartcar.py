import pytest
from SmartCar.app import app


@pytest.fixture()
def client():
    return app.test_client()


class TestSmartCarApi:

    def test_vehicle_info(self, client):
        response = client.get('/vehicles/1234')
        print(response.json)
        expected_response = {
            "color": "Metallic Silver",
            "doorCount": 4,
            "driveTrain": "v8",
            "vin:": "123123412412"
        }
        assert response.status_code == 200
        assert response.json == expected_response

    def test_fuel_info(self, client):
        response = client.get('vehicles/1234/fuel')
        assert response.status_code == 200

    def test_battery_info(self, client):
        response = client.get('vehicles/1234/battery')
        assert response.status_code == 200

    def test_door_info(self, client):
        response = client.get('vehicles/1234/doors')
        assert response.status_code == 200

    def test_start_engine(self, client):
        json_body = {"action": "START"}
        response = client.post('vehicles/1234/engine', json=json_body)
        assert response.status_code == 200

    def test_stop_engine(self, client):
        json_body = {"action": "STOP"}
        response = client.post('vehicles/1234/engine', json=json_body)
        assert response.status_code == 200

