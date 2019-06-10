from constans import *
from testrail import APIClient


def get_testrail_client():
    client = APIClient(TESTRAIL_URL)
    client.user = TESTRAIL_USER
    client.password = TESTRAIL_PASSWORD

    return client


def get_tests_in_run(run_id):
    client = get_testrail_client()
    data_in_run = client.send_get("get_tests/%s" % run_id)
    in_run_name_test = []
    for d in data_in_run:
        if d["status_id"] == STATUS_FOR_TESTS_AUTO or d["status_id"] == 7:
            case_id = d["case_id"]
            test_name_in_data = d["custom_automated_test_name"]
            in_run_name_test.append(test_name_in_data)
    return in_run_name_test


def get_dict_case_test_in_run(run_id):
    client = get_testrail_client()
    data_in_run = client.send_get("get_tests/%s" % run_id)
    dict_id_case_in_run_name_test = {}
    for d in data_in_run:
        if d["status_id"] == STATUS_FOR_TESTS_AUTO or d["status_id"] == 7:
            case_id = d["case_id"]
            test_name_in_data = d["custom_automated_test_name"]
            dict_id_case_in_run_name_test.update({case_id: test_name_in_data})
    return dict_id_case_in_run_name_test


def update_testrail(case_id, run_id, result, excinfo = "", log="", duration = None):
    client = get_testrail_client()
    if result == "failed":
        status_id = 7
        n1 = '\n'
        msg = f' Ошибка: {excinfo} {n1}  лог: {n1} {str(log)}'
    if result == "passed":
        status_id = 1
        msg = "Test passed"
    if result == "skipped":
        status_id = 4
        msg = str(log)

    if run_id is not None:
        try:
            client.send_post(
                "add_result_for_case/%s/%s" % (run_id, case_id),
                {"status_id": status_id, "comment": msg},
            )
        except Exception as e:
            print("Exception in update_testrail() updating TestRail.")
        else:
            print(
                "Updated test result for case: %s in test run: %s with msg:%s"
                % (case_id, run_id, msg)
            )

