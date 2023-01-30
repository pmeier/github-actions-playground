import json


def main():
    steps = [
        {
            "name": "Setup Python",
            "uses": "actions/setup-python@v4",
            "with": {"python-version": "${{ matrix.python-version }}"},
        },
        {
            "name": "Showcase Python shell",
            "shell": "python",
            "run": "\n".join(
                [
                    "|",
                    "import platform",
                    "import sys",
                    "",
                    "print(platform.platform())",
                    "print(sys.executable)",
                    "print(sys.version_info)",
                ]
            ),
        },
    ]
    print(json.dumps(steps))


if __name__ == "__main__":
    main()
