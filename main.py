import sys

try:
    from pythlings.cli import main
except ModuleNotFoundError as exc:
    if exc.name == "loguru":
        print(
            "Missing dependency: loguru. Run the project with the virtual environment, for example `.\\.venv\\Scripts\\python.exe main.py`, or install the project dependencies first.",
            file=sys.stderr,
        )
        raise SystemExit(1)
    raise


if __name__ == "__main__":
    raise SystemExit(main())
