import json
import requests


class TestSuiteOne:
    def test_how_many_categories(self, get_access_token):
        access_token = get_access_token
        response = requests.get(
            url="https://www.olx.ua/api/partner/categories",
            headers={
                'Authorization': 'Bearer ' + access_token,
                'Version': '2.0'
            }
        )
        categories = json.loads(response.content.decode())

        actual_count_of_categories = len(categories['data'])
        expected_count_of_categories = 514
        assert actual_count_of_categories == expected_count_of_categories

    def test_check_id_of_category(self, get_access_token):
        access_token = get_access_token
        response = requests.get(
            url="https://www.olx.ua/api/partner/categories/6",
            headers={
                'Authorization': 'Bearer ' + access_token,
                'Version': '2.0'
            }
        )
        some_category = json.loads(response.content.decode())

        actual_name_of_categories = some_category['data']['name']
        expected_name_of_categories = "Работа"
        assert actual_name_of_categories == expected_name_of_categories
