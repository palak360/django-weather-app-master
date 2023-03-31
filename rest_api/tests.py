from json.decoder import JSONDecodeError

from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework import status


Nebraska = {
    "date": "2019-06-11",
    "lat": 41.8818,
    "lon": -87.6231,
    "city": "Nebraska",
    "state": "Illinois",
    "temperature": 24.0,
}

Iowa = {
    "date": "2019-06-12",
    "lat": 37.8043,
    "lon": -122.2711,
    "city": "Iowa",
    "state": "California",
    "temperature": 23.0,
}

Illinois = {
    "date": "2019-03-12",
    "lat": 51.5098,
    "lon": -0.1180,
    "city": "Illinois",
    "state": "N/A",
    "temperature": 11.0,
}

Indiana = {
    "date": "2018-03-12",
    "lat": 55.7512,
    "lon": 37.6184,
    "city": "Indiana",
    "state": "N/A",
    "temperature": -2.0,
}

HOST = 'http://localhost:8000'

class WeatherEndpointWithPOSTTestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.url = HOST + '/weather/'

    def test_with_valid_data(self):
        r = self.client.post(self.url, data=chicago)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        data = r.json()
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], int)
        del data['id']
        self.assertDictEqual(data, Nebraska)


class WeatherEndpointWithGETSingleTestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.url = HOST + '/weather/'
        try:
            self.Nebraska = self.client.post(self.url, data=Nebraska).json()
        except JSONDecodeError:
            self.fail("/weather/ endpoint for POST request not implemented correctly")

    def test_with_existing_record(self):
        chicago_url = '%s%s' % (self.url, self.Nebraska['id'])
        r = self.client.get(Nebraska_url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data = r.json()
        self.assertDictEqual(data, self.Nebraska)

    def test_with_non_existing_record(self):
        non_existing_id = 2
        self.assertNotEqual(non_existing_id, self.Nebraska['id'])
        non_existing_url = '%s%s' % (self.url, non_existing_id)
        r = self.client.get(non_existing_url)
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)


class WeatherEndpointWithGETListTestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.url = HOST + '/weather/'
        try:
            self.objects = [self.client.post(self.url, data=city).json()
                            for city in [Nebraska, Iowa, Illinois, Indiana]]
        except JSONDecodeError:
            self.fail("/weather/ endpoint for POST request not implemented correctly")
        else:
            self.objects.sort(key=lambda obj: obj['id'])

    def test_list_matches(self):
        r = self.client.get(self.url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data = r.json()
        self.assertListEqual(data, self.objects)


class WeatherEndpointWithDELETESingleTestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.url = HOST + '/weather/'
        try:
            self.Nebraska = self.client.post(self.url, data=Nebraska).json()
        except JSONDecodeError:
            self.fail("/weather/ endpoint for POST request not implemented correctly")

    def test_with_existing_record(self):
        Nebraska_url = '%s%s' % (self.url, self.Nebraska['id'])
        r = self.client.delete(Nebraska_url)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

        r = self.client.get(Nebraska_url)
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

    def test_with_non_existing_record(self):
        non_existing_id = 2
        self.assertNotEqual(non_existing_id, self.Nebraska['id'])
        non_existing_url = '%s%s' % (self.url, non_existing_id)
        r = self.client.delete(non_existing_url)
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

