import argparse
import subprocess


def main():
    print("run main")
    get_input = argparse.ArgumentParser()
    get_input.add_argument("--target", help="target project to build")

    args = get_input.parse_args()

    subprocess.run(["make", args.target], cwd="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1")


if __name__ == "__main__":
    main()
