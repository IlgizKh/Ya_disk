from pprint import pprint

import requests


TOKEN = ""


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        pprint(data)
        url = data.get('href')
        response2 = requests.put(url, data=open(file_path, 'rb'))
        response2.raise_for_status()
        if response2.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "test.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
