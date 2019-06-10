import re
from base64 import b64decode

import requests

header = {"PRIVATE-TOKEN": "CZMU4xfQHzar2x-AA1xK"}
url_get_scripts = "https://gitlab.osinit.com/api/v4/projects/346/repository/files/Scripts%2Fapp%2FSmoke"
url_get_test_cases = "https://gitlab.osinit.com/api/v4/projects/346/repository/files/Test Cases%2Fapp%2FSmoke"
url_update_file = (
    "https://gitlab.osinit.com/api/v4/projects/{id}/repository/files/{file_path}"
)
ID_PROJECT = "320"
FILE_PATH = "README%2Emd"


class GitlabApiHelper:
    @staticmethod
    def get_id_test_case_from_repository():
        url = (
            url_get_scripts
            + "%2FBalanceTestcase%2FScript1548239256562%2Egroovy?ref=master"
        )
        resp = requests.request(method="GET", url=url, headers=header)
        response = resp.json()
        content = b64decode(response["content"]).decode("utf-8")
        id_test_case = re.findall(r"\d+", content, flags=re.MULTILINE)
        return id_test_case

    @staticmethod
    def get_id_test_from_repository():
        url = url_get_test_cases + "%2FBalanceTestcase%2Etc?ref=master"
        resp = requests.request(method="GET", url=url, headers=header)
        response = resp.json()
        content = b64decode(response["content"]).decode("utf-8")
        id = re.search("<id>(.*)</id>", content, flags=re.MULTILINE).group(1)
        return id

    @staticmethod
    def update_file_in_gitlab():
        url = (
            "https://gitlab.osinit.com/api/v4/projects/320/repository/files/README%2Emd"
        )
        headers = {
            "PRIVATE-TOKEN": "CZMU4xfQHzar2x-AA1xK",
            "Content-Type": "application/json",
        }
        data = {
            "branch": "test/runing_tests",
            "author_email": "julia.artyukhina@osinit.com",
            "author_name": "Юлия Артюхина",
            "content": "12345",
            "commit_message": "update file",
        }
        resp = requests.request(method="PUT", url=url, headers=headers, json=data)
        response = resp.json()
        code = response["status_code"]
        return code
