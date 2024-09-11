#!/usr/bin/env -S python3 -u
import logging
import subprocess

from .common import get_tag_names

logger = logging.getLogger(__name__)


def git_tag(*names: str):
    logger.info("➡️ Git tag...")
    tags = names or get_tag_names()
    for i, tag in enumerate(tags):
        subprocess.check_call(["git", "tag", *(["-f"] if i > 0 else []), tag])


if __name__ == "__main__":
    git_tag()
