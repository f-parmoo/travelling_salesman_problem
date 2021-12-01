from unittest import TestCase
from server import app
import json
import sys


def parse_response(response):
    return json.loads(response.get_data().decode(sys.getdefaultencoding()))


location_list = [[176, 253], [136, 208], [86, 221], [209, 305], [131, 167], [36, 372], [293, 195], [115, 357],
                 [174, 162], [118, 20]]
distance = [
    [0.0, 40.0, 90.0, 33.0, 45.0, 140.0, 117.0, 61.0, 2.0, 58.0],
    [40.0, 0.0, 50.0, 73.0, 5.0, 100.0, 157.0, 21.0, 38.0, 18.0],
    [90.0, 50.0, 0.0, 123.0, 45.0, 50.0, 207.0, 29.0, 88.0, 32.0],
    [33.0, 73.0, 123.0, 0.0, 78.0, 173.0, 84.0, 94.0, 35.0, 91.0],
    [45.0, 5.0, 45.0, 78.0, 0.0, 95.0, 162.0, 16.0, 43.0, 13.0],
    [140.0, 100.0, 50.0, 173.0, 95.0, 0.0, 257.0, 79.0, 138.0, 82.0],
    [117.0, 157.0, 207.0, 84.0, 162.0, 257.0, 0.0, 178.0, 119.0, 175.0],
    [61.0, 21.0, 29.0, 94.0, 16.0, 79.0, 178.0, 0.0, 59.0, 3.0],
    [2.0, 38.0, 88.0, 35.0, 43.0, 138.0, 119.0, 59.0, 0.0, 56.0],
    [58.0, 18.0, 32.0, 91.0, 13.0, 82.0, 175.0, 3.0, 56.0, 0.0]
]

solution = "     Route VehicleID(0) 0 -> 6 -> 3 -> 0   Route distance: 234miles     Route VehicleID(1) 0 -> 8 -> 1 -> 4 -> 9 -> 7 -> 2 -> 5 -> 0   Route distance: 280miles"


class ApiTest(TestCase):
    def setUp(self):
        self.app = app.test_client()


    def create_problem(self):
        json_response = self.app.post('/api/create_problems', data=json.dumps({"location_list": location_list}),
                                      content_type='application/json')
        return parse_response(json_response)


    def subscribe(self):
        json_response = self.app.get("/api/subscribe")
        return parse_response(json_response)


    def publish(self):
        json_response = self.app.post("/api/publish", data=json.dumps({
            "problem_id": 1,
            "num_vehicles" :2
        }), content_type='application/json')
        return parse_response(json_response)


    def test_create_problem(self):
        response = self.create_problem()
        self.assertEqual(response['locations'], location_list)
        self.assertEqual(response['distance_matrix'], distance)
        self.assertEqual(response['solution'], "Poblish Problem for Getting the Solution")


    def test_subscribe(self):
        self.create_problem()
        response = self.subscribe()
        self.assertEqual(response['locations'], location_list)
        self.assertEqual(response['distance_matrix'], distance)
        self.assertEqual(response['solution'], "Poblish Problem for Getting the Solution")


    def test_publish(self):
        self.create_problem()
        self.subscribe()
        response = self.publish()
        self.assertEqual(response['problem_id'], 1)
        self.assertEqual(response['locations'], location_list)
        self.assertEqual(response['distance_matrix'], distance)
        self.assertEqual(response['solution'], solution)
