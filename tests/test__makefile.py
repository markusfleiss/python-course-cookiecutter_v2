import pytest
import subprocess
from pathlib import Path

def test__linting_passes(project_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)

def fest__tests_pass():
    ...

def test__install_succeeds():
    ...


"""
Setup:
1. geneate a project using cookiecutter
2. create a virtual environment and install project dependencies

Tests:
3. run tests
4. run linting

Cleanup/Teardown:
5. remove virtual environment
6. remove generated project
"""