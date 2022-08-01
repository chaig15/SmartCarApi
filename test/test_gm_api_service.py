import unittest

from SmartCar.GmApiUtils.GmApiService import GmApiService
from SmartCar.error import SmartCarApiException


class TestGmApiService(unittest.TestCase):
    """
    Test Class for GMApiService
    """

    def test_engine_exception(self):
        test_service = GmApiService(id=1234)
        json_body = {
            'action': "bad_value"
        }
        self.assertRaises(SmartCarApiException, test_service.start_stop_engine, json_body)

    def test_start_engine(self):
        test_service = GmApiService(id=1234)
        json_body = {
            'action': 'START'
        }
        outputs = [{'status': 'success'}, {'status': 'error'}]
        self.assertIn(test_service.start_stop_engine(json_body=json_body), outputs)

    def test_stop_engine(self):
        test_service = GmApiService(id=1234)
        json_body = {
            'action': 'STOP'
        }
        outputs = [{'status': 'success'}, {'status': 'error'}]
        self.assertIn(test_service.start_stop_engine(json_body=json_body), outputs)

    def test_get_vehicle_info(self):
        test_service = GmApiService(id=1234)
        expected_response = {
            "color": "Metallic Silver",
            "doorCount": 4,
            "driveTrain": "v8",
            "vin:": "123123412412"
        }
        self.assertEqual(test_service.get_vehicle_info(), expected_response)

    def test_get_vehicle_door(self):
        test_service = GmApiService(id=1234)
        expected_response = [
            {
                "location": "frontLeft",
                "locked": True
            },
            {
                "location": "frontRight",
                "locked": True
            },
            {
                "location": "backLeft",
                "locked": True
            },
            {
                "location": "backRight",
                "locked": True
            }
        ]
        self.assertCountEqual(test_service.get_door_info(), expected_response)

    def test_get_fuel_info(self):
        test_service = GmApiService(id=1234)
        self.assertIsInstance(test_service.get_battery_fuel_info(fuel_type='tankLevel')["percent"], float)

    def test_get_battery_info(self):
        test_service = GmApiService(id=1235)
        self.assertIsInstance(test_service.get_battery_fuel_info(fuel_type='batteryLevel')["percent"], float)

    def test_get_fuel_info_none(self):
        test_service = GmApiService(id=1235)
        self.assertIsNone(test_service.get_battery_fuel_info(fuel_type='tankLevel')["percent"])

    def test_get_battery_info_none(self):
        test_service = GmApiService(id=1234)
        self.assertIsNone(test_service.get_battery_fuel_info(fuel_type='batteryLevel')["percent"])

        self.assertIs
