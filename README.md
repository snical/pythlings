<a href=".">
  <img src="./public/pythlings.png" width="460" alt="pythlings logo">
</a>

# pythlings

`pythlings` is a Rustlings-style Python course and CLI for people who want to learn Python by fixing small, focused exercises. It starts with absolute beginner Python basics and gradually moves into real intermediate topics like files, classes, decorators, typing, testing, asyncio, and architecture.

If you are searching for Python exercises, Python practice projects, a Python CLI tutorial, or a Rustlings alternative for Python, this repo is built for that exact workflow.

## Why People Star It

- beginner-friendly Python learning path with obvious next steps
- hands-on Python exercises instead of long theory lessons
- Rustlings-style feedback loop that keeps momentum high
- covers both Python fundamentals and more advanced topics
- simple local CLI with hints, reset support, and reference solutions

Run the CLI, fix the first broken file it points you to, check your work, and keep going. The whole point is to keep the next step obvious so you can focus on learning Python instead of deciding what to do next.

## Quick Start

We recommend `uv`, but use whatever is normal for your setup.

```powershell
git clone <your-repo-url>
cd pythlings
uv sync
uv run pythlings
```

If you would rather use plain `pip`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe main.py
```

## Who It Is For

- people learning Python from scratch
- developers coming from JavaScript, Rust, or another language
- teachers who want a structured Python practice repo
- maintainers looking for a Python version of the Rustlings experience

## Topics Covered

- variables
- functions
- conditionals
- loops
- strings, lists, tuples, and dictionaries
- modules and exceptions
- file handling
- classes and comprehensions
- iterators and decorators
- dataclasses and typing
- testing and asyncio
- architecture-focused exercises

## How It Works

- checks exercises in order
- stops at the first one that fails
- shows you exactly which file you are on
- lets you re-check, ask for a hint, list exercises, reset the current file, or quit
- only moves forward once the current exercise is fixed

Work in `exercises/` and try not to open `solutions/` unless you want spoilers.

Typical output includes `Stuck at: exercises/00_intro/intro1.py`.

## CLI Commands

- `r` checks the current exercise and advances when it passes
- `h` shows the hint embedded in the current exercise
- `l` lists every exercise
- `c` checks the full course
- `x` resets the current exercise from its starter copy
- `q` quits

## Validation

Early exercises compare output directly. Later exercises can use validators in `.pythlings/validators/` so the harder parts of the course can check behavior, not just one printed line.

## Project Layout

```text
exercises/
solutions/
.pythlings/starters/
.pythlings/validators/
```

- `exercises/` is the learner-facing course
- `solutions/` contains reference answers
- `.pythlings/starters/` stores the broken reset copies
- `.pythlings/validators/` stores advanced behavior-based checks

## License

This project is licensed under the [MIT License](./LICENSE).

## Links

- Repository: [github.com/snical/pythlings](https://github.com/snical/pythlings)
- Issues: [github.com/snical/pythlings/issues](https://github.com/snical/pythlings/issues)
- Changelog: [CHANGELOG.md](./CHANGELOG.md)
- Contributing: [CONTRIBUTING.md](./CONTRIBUTING.md)
