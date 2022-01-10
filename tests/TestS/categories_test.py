from urllib.parse import urljoin

import requests


class TestSuiteOne:
    @staticmethod
    def get_olx_categories(access_token, category: str = None):
        url = "https://www.olx.ua/api/partner/categories"
        if category:
            url = urljoin('https://www.olx.ua/api/partner/categories/', category)

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Version': '2.0'
        }
        response = requests.get(url=url, headers=headers)
        content = response.json()
        return content

    def test_how_many_categories(self, get_access_token):
        access_token = get_access_token
        categories = self.get_olx_categories(access_token)

        actual_count_of_categories = len(categories['data'])
        expected_count_of_categories = 514
        assert actual_count_of_categories == expected_count_of_categories

    def test_check_id_of_category(self, get_access_token):
        access_token = get_access_token
        some_category = self.get_olx_categories(access_token, '6')

        actual_name_of_categories = some_category['data']['name']
        expected_name_of_categories = "Работа"
        assert actual_name_of_categories == expected_name_of_categories
