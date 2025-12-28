import json
import re
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

import pytest

from tests.utils.project import generate_project
from tests.utils.project import initialize_git_repo


@pytest.fixture(scope="function")
def project_dir() -> Path:
    template_values = {
        "repo_name": "test_repo"
    }
    generated_repo_dir: Path = generate_project(template_values=template_values)
    initialize_git_repo(repo_dir=generated_repo_dir)
    subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)