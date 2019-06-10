import importlib
import os
import sys
import types

import pytest

from constans import NAME_TESTS, DICT_IDCASE_NAMETEST
from testrailconf import get_tests_in_run, get_dict_case_test_in_run
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--run_id", default=25)
    return parser


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
RUN_ID = namespace.run_id
mode = "a" if os.path.exists("run_id") else "w"
with open("run_id", 'r+') as f:
    f.truncate()
    f.write(RUN_ID)
    f.close()

name_tests = get_tests_in_run(RUN_ID)
DICT_IDCASE_NAMETEST.update(get_dict_case_test_in_run(namespace.run_id))


module_tests = importlib.import_module("tests")
dict_module_tests = module_tests.__dict__
class_dict = [val for val in dict_module_tests.values() if isinstance(val, type)]
module_dict = [
    val for val in dict_module_tests.values() if isinstance(val, types.ModuleType)
]
for k in range(len(name_tests)):
    if name_tests[k] in NAME_TESTS:
        name_tests[k] = NAME_TESTS.get(name_tests[k])
    else:
        name_tests[k] = ""

if name_tests:
    pytest.main(name_tests)
else:
    print("Not found tests for run")