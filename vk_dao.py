import json
import requests


class VkDao():
    @staticmethod
    def json_reader(filename):
        with open(filename, 'r', encoding='utf-8') as data:
            return json.load(data)

    @staticmethod
    def json_loader():
            settings = VkDao.json_reader('settings.json')
            token = settings['token']
            group_ids = settings['group_ids']
            return "https://api.vk.com/method/groups.getById?" \
                            "group_ids={0}&fields=members_count&v=5.92&" \
                            "access_token={1}&v=5.92"\
                .format(','.join(map(str, group_ids)), token)

    # Convertion of the response
    @staticmethod
    def convert(response):
        settings = VkDao.json_reader('settings.json')
        col = settings['columns']
        res = []
        for y in response['response']:
            a = []
            for x in col:
                a.append(y[x])
                if len(a) == len(col):
                    res.append(tuple(a))
        return res

    def get_data(self):
        response = requests.get(VkDao.json_loader())
        if 'error' in response.json().keys():
            raise ErrorInVKResponse(response.json())
        elif response.status_code == 200:
            print('API REQUEST HAS BEEN SUCCEED!')
            return self.convert(response.json())


# Exeption class in case of getting problems with API request
class ErrorInVKResponse(Exception):
    def __init__(self, response):
        print('ERROR CODE:', response['error']['error_code'],
              'ERROR MESSAGE:', response['error']['error_msg'])
