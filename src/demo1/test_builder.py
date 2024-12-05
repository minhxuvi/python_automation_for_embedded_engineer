import argparse
import os
import subprocess
from pathlib import Path
from typing import Optional


class TestInput: ...


def build_new(test_input: TestInput):
    pass


def build(build_dir: Path, target: str, os_: str, compiler: str, core: str, env: Optional[dict] = None):
    """Build project."""
    current_environment = os.environ.copy()
    if env is not None:
        current_environment.update(env)
    print(" ".join(["make", f"os={os_}", f"compiler={compiler}", f"core={core}", target]))
    subprocess.run(
        [
            "make",
            f"os={os_}",
            f"compiler={compiler}",
            f"core={core}",
            target,
        ],
        cwd=build_dir,
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
    build(
        build_dir="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1",
        target=args.target,
        os_=args.os,
        compiler=args.compiler,
        core=args.core,
        env=custom_env,
    )


if __name__ == "__main__":
    main()
