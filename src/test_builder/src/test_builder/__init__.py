"""Build project."""

import argparse
import os
import subprocess
from pathlib import Path
from typing import Optional

from pydantic import BaseModel

# 1 Create test input class
# 2 Verify test input class


class TestInput(BaseModel):
    """Test input."""

    # build_dir: Path
    build_dir: str
    target: str
    os_: str
    compiler: str
    core: str
    env: Optional[dict] = None


def build(test_input: TestInput):
    """Build project."""
    current_environment = os.environ.copy()
    if test_input.env is not None:
        current_environment.update(test_input.env)
    print(
        " ".join(
            [
                "make",
                f"os={test_input.os_}",
                f"compiler={test_input.compiler}",
                f"core={test_input.core}",
                test_input.target,
            ]
        )
    )
    subprocess.run(
        [
            "make",
            f"os={test_input.os_}",
            f"compiler={test_input.compiler}",
            f"core={test_input.core}",
            test_input.target,
        ],
        cwd=test_input.build_dir,
        env=current_environment,
        # shell=True, # TODO: analyze while this not run with shell=True
        check=True,
    )


def main():
    get_input = argparse.ArgumentParser()
    get_input.add_argument("--target", default="all", help="target project to build")
    get_input.add_argument("--os", default="freertos", help="os to build")
    get_input.add_argument("--compiler", default="gcc", help="compiler to build")
    get_input.add_argument("--core", default="M7", help="Core to build")

    args = get_input.parse_args()
    custom_env = {
        "PLUGINS_DIR": "/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/plugins",
        "BUILD_DIR": "/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/build",
        "GCC_DIR": "/usr/bin",
    }
    # TODO: store input to database, return build path with object_id in it. Example: /path/to/bin/<object_id>/binaries
    build(
        test_input=TestInput(
            build_dir="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1",
            target=args.target,
            os_=args.os,
            compiler=args.compiler,
            core=args.core,
            env=custom_env,
        )
    )


if __name__ == "__main__":
    main()
