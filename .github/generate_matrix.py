import itertools
import json


def main():
    matrix = {"include": list(generate_entries())}
    print(json.dumps(matrix))


OSS = [
    "windows-2022",
    "windows-2019",
    "ubuntu-22.04",
    "ubuntu-20.04",
    "macos-12",
    "macos-11",
]
PYTHON_VERSIONS = [f"3.{minor}" for minor in range(7, 12)]


def generate_entries():
    for os, python_version in itertools.product(OSS, PYTHON_VERSIONS):
        if python_version in {"3.7", "3.11"} and os != "ubuntu-22.04":
            continue

        if python_version in {"3.7", "3.8"} and os == "macos-12":
            continue

        yield {"os": os, "python-version": python_version}


if __name__ == "__main__":
    main()
