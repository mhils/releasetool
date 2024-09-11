#!/usr/bin/env -S python3 -u
import logging
import subprocess

from releasetool.common import branch
from releasetool.common import get_tag_names

logger = logging.getLogger(__name__)


def git_push(*identifiers: str):
    logger.info("➡️ Git push...")
    if not identifiers:
        identifiers = [
            branch,
            *get_tag_names(),
        ]
    subprocess.check_call(["git", "push", "-f", "--atomic", "origin", *identifiers])


if __name__ == "__main__":
    git_push()
