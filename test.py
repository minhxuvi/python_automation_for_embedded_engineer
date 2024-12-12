# from test_builder.test_builder import (
#     TestInput,
#     build,
# )

import os
import sys

sys.path.append(
    os.path.abspath("/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/src/test_builder")
)
from test_builder import (
    TestInput,
    build,
)

test_input = TestInput(
    build_dir="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/_data",
    target="clean",
    os_="autosar",
    compiler="iar",
    core="R52",
)
build(test_input=test_input)
