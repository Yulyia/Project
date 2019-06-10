import pytest

from constans import DICT_IDCASE_NAMETEST
from testrailconf import update_testrail


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    log = ""
    excinfo = ""
    if rep.when == "call":
        duration = rep.duration
        if call.excinfo:
            excinfo = call.excinfo
        if rep.longreprtext:
            log = rep.longreprtext
        for (case, name,) in (DICT_IDCASE_NAMETEST.items()):
            if name == item.name:
                print(case)
                with open("run_id", 'r+') as f:
                    RUN_ID = f.read()

                update_testrail(case, RUN_ID, rep.outcome, excinfo, log, duration)



