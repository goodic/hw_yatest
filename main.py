#import pytest
import requests


class YaDisc:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources?'
        url += 'path=' + folder_name
        headers = self.get_headers()
        response = requests.put(url, headers=headers)
        return response

    def check_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources?'
        url += 'path=' + folder_name
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response

    def delete_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources?'
        url += 'path=' + folder_name
        headers = self.get_headers()
        response = requests.delete(url, headers=headers)
        return response


if __name__ == '__main__':
    token = ''
    ya_disc = YaDisc(token)
    folder_name = input('Введите название папки: ')
    result = ya_disc.create_folder(folder_name)
    print(f'Результат создания папки {result.status_code}')
    result = ya_disc.check_folder(folder_name)
    print(f'Результат проверки папки {result.status_code}')
