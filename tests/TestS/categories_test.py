import json
import requests
from olx_authorization import Authorization
from tests.conftest import GlobalClassToken


class TestSuiteOne:
    def test_setup(self, client_id, client_secret):
        """
        Get 'client_id', 'client_secret' parameters from test run command.
        Set authorization.
        """
        GlobalClassToken.access_token = Authorization(
            client_id=client_id,
            client_secret=client_secret
        ).get_token()

    def test_how_many_categories(self):
        response = requests.get(
            url="https://www.olx.ua/api/partner/categories",
            headers={
                'Authorization': 'Bearer ' + GlobalClassToken.access_token,
                'Version': '2.0'
            }
        )
        categories = json.loads(response.content.decode())

        actual_count_of_categories = len(categories['data'])
        expected_count_of_categories = 514
        assert actual_count_of_categories == expected_count_of_categories

    def test_check_id_of_category(self):
        response = requests.get(
            url="https://www.olx.ua/api/partner/categories/6",
            headers={
                'Authorization': 'Bearer ' + GlobalClassToken.access_token,
                'Version': '2.0'
            }
        )
        some_category = json.loads(response.content.decode())

        actual_name_of_categories = some_category['data']['name']
        expected_name_of_categories = "Работа"
        assert actual_name_of_categories == expected_name_of_categories
