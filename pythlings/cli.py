from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from loguru import logger

ROOT = Path(__file__).resolve().parent.parent
EXERCISES_DIR = ROOT / "exercises"
SOLUTIONS_DIR = ROOT / "solutions"
STARTERS_DIR = ROOT / ".pythlings" / "starters"
VALIDATORS_DIR = ROOT / ".pythlings" / "validators"


@dataclass(frozen=True)
class Exercise:
    path: Path

    @property
    def relative_path(self) -> Path:
        return self.path.relative_to(ROOT)

    @property
    def starter_path(self) -> Path:
        return STARTERS_DIR / self.path.relative_to(EXERCISES_DIR)

    @property
    def solution_path(self) -> Path:
        return SOLUTIONS_DIR / self.path.relative_to(EXERCISES_DIR)

    @property
    def validator_path(self) -> Path:
        return VALIDATORS_DIR / self.path.relative_to(EXERCISES_DIR)


@dataclass(frozen=True)
class CheckResult:
    passed: bool
    stdout: str
    stderr: str
    returncode: int
    expected_stdout: str = ""
    expected_stderr: str = ""
    expected_returncode: int = 0
    mode: str = "output"


def configure_logger() -> None:
    logger.remove()
    logger.add(sys.stdout, colorize=True, format="{message}")


def escape_markup(text: str) -> str:
    return text.replace("<", "\\<").replace(">", "\\>")


def log_message(level: str, message: str) -> None:
    logger.opt(colors=True).log(level, message)


def log_blank() -> None:
    logger.info("")


def log_section(title: str, color: str = "blue") -> None:
    log_message("INFO", f"<{color}>{title}</{color}>")


def discover_exercises() -> list[Exercise]:
    if not EXERCISES_DIR.exists():
        return []

    paths = sorted(
        path
        for path in EXERCISES_DIR.rglob("*.py")
        if path.is_file() and not path.name.startswith("_")
    )
    return [Exercise(path=path) for path in paths]


def run_python_file(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


def run_validator(exercise: Exercise) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        str(ROOT) if not pythonpath else os.pathsep.join([str(ROOT), pythonpath])
    )
    return subprocess.run(
        [
            sys.executable,
            str(exercise.validator_path),
            str(exercise.path),
            str(exercise.solution_path),
        ],
        capture_output=True,
        text=True,
        cwd=ROOT,
        env=env,
    )


def check_exercise(exercise: Exercise) -> CheckResult:
    if exercise.validator_path.exists():
        validated = run_validator(exercise)
        return CheckResult(
            passed=validated.returncode == 0,
            stdout=validated.stdout,
            stderr=validated.stderr,
            returncode=validated.returncode,
            mode="validator",
        )

    learner = run_python_file(exercise.path)
    solution = run_python_file(exercise.solution_path)
    passed = (
        learner.returncode == solution.returncode
        and learner.stdout == solution.stdout
        and learner.stderr == solution.stderr
    )
    return CheckResult(
        passed=passed,
        stdout=learner.stdout,
        stderr=learner.stderr,
        returncode=learner.returncode,
        expected_stdout=solution.stdout,
        expected_stderr=solution.stderr,
        expected_returncode=solution.returncode,
        mode="output",
    )


def find_current_exercise(
    exercises: list[Exercise],
) -> tuple[int, Exercise | None, CheckResult | None]:
    completed = 0

    for exercise in exercises:
        check = check_exercise(exercise)
        if check.passed:
            completed += 1
            continue
        return completed, exercise, check

    return completed, None, None


def build_progress_bar(completed: int, total: int, width: int = 40) -> str:
    if total == 0:
        return "[no exercises]"

    filled = int((completed / total) * width)
    if filled >= width:
        return "[" + "#" * width + "]"
    return "[" + "#" * filled + ">" + "-" * (width - filled - 1) + "]"


def extract_hint(exercise: Exercise) -> str | None:
    for line in exercise.path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# hint:"):
            return line.removeprefix("# hint:").strip()
    return None


def validate_exercise_files(exercises: list[Exercise]) -> bool:
    valid = True
    for exercise in exercises:
        if not exercise.solution_path.exists():
            log_message(
                "ERROR",
                f"<red>Missing solution:</red> {escape_markup(exercise.solution_path.relative_to(ROOT).as_posix())}",
            )
            valid = False
        if not exercise.starter_path.exists():
            log_message(
                "ERROR",
                f"<red>Missing starter:</red> {escape_markup(exercise.starter_path.relative_to(ROOT).as_posix())}",
            )
            valid = False
        if exercise.validator_path.exists() and not exercise.validator_path.is_file():
            log_message(
                "ERROR",
                f"<red>Invalid validator:</red> {escape_markup(exercise.validator_path.relative_to(ROOT).as_posix())}",
            )
            valid = False
    return valid


def list_exercises(exercises: list[Exercise], current: Exercise | None = None) -> None:
    log_section("Exercise list", "blue")
    for exercise in exercises:
        path_text = escape_markup(exercise.relative_path.as_posix())
        if exercise == current:
            log_message("INFO", f"<magenta>current</magenta>  {path_text}")
        else:
            logger.info(f"         {path_text}")


def reset_exercise(exercise: Exercise) -> None:
    if not exercise.starter_path.exists():
        log_message(
            "WARNING", "<yellow>No starter template found for this exercise.</yellow>"
        )
        return

    exercise.path.write_text(
        exercise.starter_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    log_message(
        "INFO",
        f"<yellow>Reset:</yellow> {escape_markup(exercise.relative_path.as_posix())}",
    )


def _show_output_block(label: str, value: str, color: str) -> None:
    if not value:
        return
    log_message("INFO", f"<{color}>{label}</{color}>")
    for line in value.rstrip().splitlines():
        logger.info(f"  {line}")


def summarize_stderr(stderr: str) -> tuple[str | None, str | None]:
    lines = [line.rstrip() for line in stderr.splitlines() if line.strip()]
    if not lines:
        return None, None

    location = next(
        (line.strip() for line in lines if line.lstrip().startswith("File ")), None
    )
    return location, lines[-1].strip()


def print_failure(exercise: Exercise, check: CheckResult) -> None:
    log_section("Exercise needs a fix", "red")
    log_message(
        "INFO",
        f"File: <magenta>{escape_markup(exercise.relative_path.as_posix())}</magenta>",
    )

    if check.mode == "validator":
        if check.stderr.strip():
            location, summary = summarize_stderr(check.stderr)
            if location:
                log_message("ERROR", f"<red>{escape_markup(location)}</red>")
            if summary:
                log_message("ERROR", f"<red>{escape_markup(summary)}</red>")
            log_blank()
            _show_output_block("Validator details:", check.stderr, "yellow")
        elif check.stdout.strip():
            log_blank()
            _show_output_block("Validator details:", check.stdout, "yellow")
        else:
            log_message(
                "ERROR",
                "<red>Advanced validator failed, but it did not provide extra details.</red>",
            )
        return

    if check.stderr.strip():
        location, summary = summarize_stderr(check.stderr)
        if location:
            log_message("ERROR", f"<red>{escape_markup(location)}</red>")
        if summary:
            log_message("ERROR", f"<red>{escape_markup(summary)}</red>")

    if check.stdout != check.expected_stdout:
        log_blank()
        _show_output_block("Your output:", check.stdout, "yellow")
        _show_output_block("Expected output:", check.expected_stdout, "green")

    if check.returncode != check.expected_returncode and not check.stderr.strip():
        log_message(
            "ERROR",
            escape_markup(
                f"Program exited with {check.returncode}, expected {check.expected_returncode}."
            ),
        )


def log_progress(completed: int, total: int) -> None:
    log_message(
        "INFO",
        f"Progress: <cyan>{build_progress_bar(completed, total)}</cyan>  <white>{completed}/{total}</white>",
    )


def log_current_exercise(exercise: Exercise) -> None:
    log_message(
        "INFO",
        f"Stuck at: <magenta>{escape_markup(exercise.relative_path.as_posix())}</magenta>",
    )


def show_status_panel(current: Exercise, completed: int, total: int) -> None:
    log_blank()
    log_section("Current exercise", "magenta")
    log_current_exercise(current)
    log_progress(completed, total)


def announce_progress(
    previous: Exercise, previous_check: CheckResult, current: Exercise | None
) -> None:
    solved_path = escape_markup(previous.relative_path.as_posix())

    log_message("SUCCESS", f"<green>Solved:</green> {solved_path}")
    _show_output_block("Output:", previous_check.stdout, "green")
    if current is None:
        log_message("SUCCESS", "<green>You finished every exercise.</green>")
        return

    next_path = escape_markup(current.relative_path.as_posix())
    log_message("SUCCESS", f"<green>Next up:</green> {next_path}")


def ensure_layout() -> None:
    for directory in (EXERCISES_DIR, SOLUTIONS_DIR, STARTERS_DIR, VALIDATORS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


def run_all_checks(exercises: list[Exercise]) -> None:
    log_section("Checking all exercises...", "blue")
    log_blank()
    failures = 0
    for exercise in exercises:
        path_text = escape_markup(exercise.relative_path.as_posix())
        check = check_exercise(exercise)
        if check.passed:
            log_message("INFO", f"<green>ok</green>   {path_text}")
        else:
            log_message("ERROR", f"<red>fail</red> {path_text}")
            failures += 1
    log_blank()
    passed = len(exercises) - failures
    if failures == 0:
        log_message("SUCCESS", f"<green>{passed}/{len(exercises)} passing</green>")
    else:
        log_message("WARNING", f"<yellow>{passed}/{len(exercises)} passing</yellow>")


def prompt(current: Exercise) -> str:
    log_blank()
    log_section("What next?", "blue")
    log_message("INFO", "  <blue>[r]</blue> check current exercise")
    log_message("INFO", "  <blue>[h]</blue> hint")
    log_message("INFO", "  <blue>[l]</blue> list exercises")
    log_message("INFO", "  <blue>[c]</blue> check all")
    log_message("INFO", "  <blue>[x]</blue> reset current exercise")
    log_message("INFO", "  <blue>[q]</blue> quit")
    try:
        return input("? ").strip().lower()
    except EOFError:
        return "q"


def main() -> int:
    configure_logger()
    ensure_layout()
    exercises = discover_exercises()

    if not exercises:
        log_message("ERROR", "<red>No exercises found in exercises/.</red>")
        return 1

    if not validate_exercise_files(exercises):
        return 1

    completed, current, current_check = find_current_exercise(exercises)

    if current is None:
        log_message("SUCCESS", "<green>All exercises are passing.</green>")
        log_progress(len(exercises), len(exercises))
        return 0

    print_failure(current, current_check)
    show_status_panel(current, completed, len(exercises))

    if not sys.stdin.isatty():
        return 1

    while True:
        action = prompt(current)
        if action == "r":
            latest_check = check_exercise(current)
            if latest_check.passed:
                solved = current
                completed, current, current_check = find_current_exercise(exercises)
                log_blank()
                announce_progress(solved, latest_check, current)
                if current is None:
                    log_progress(len(exercises), len(exercises))
                    return 0
                show_status_panel(current, completed, len(exercises))
            else:
                current_check = latest_check
                log_blank()
                print_failure(current, current_check)
                show_status_panel(current, completed, len(exercises))
        elif action == "h":
            hint = extract_hint(current)
            log_message(
                "INFO",
                f"<yellow>{escape_markup(hint or 'No hint available yet.')}</yellow>",
            )
        elif action == "l":
            list_exercises(exercises, current=current)
        elif action == "c":
            run_all_checks(exercises)
        elif action == "x":
            reset_exercise(current)
        elif action == "q":
            return 0
        else:
            log_message("WARNING", "<yellow>Unknown command.</yellow>")


if __name__ == "__main__":
    raise SystemExit(main())
