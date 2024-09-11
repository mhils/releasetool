#!/usr/bin/env -S python3 -u
import logging
import subprocess

from .common import get_tag_name

logger = logging.getLogger(__name__)


def git_tag(name: str = ""):
    logger.info("➡️ Git tag...")
    tag = name or get_tag_name()
    subprocess.check_call(["git", "tag", tag])

    # Refresh major and minor version tags.
    if not name:
        while True:
            tag = tag.rpartition(".")[0]
            if not tag:
                break
            subprocess.check_call(["git", "tag", "-f", tag])


if __name__ == "__main__":
    git_tag()
