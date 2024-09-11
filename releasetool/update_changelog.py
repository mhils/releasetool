#!/usr/bin/env -S python3 -u
import datetime
import logging
import re
from pathlib import Path

from .common import project, get_version

logger = logging.getLogger(__name__)


def update_changelog():
    logger.info("➡️ Updating CHANGELOG.md...")
    path = Path("CHANGELOG.md")
    cl = path.read_text("utf8")
    if re.match(r"^## \d+-\d+-\d+: ", cl, re.MULTILINE):
        date = datetime.date.today().strftime("%d %B %Y")
    else:
        date = datetime.date.today().strftime("%d %B %Y")
    title = f"## {date}: {project} {get_version()}"
    assert title not in cl, f"Version {get_version()} is already present in {path}."
    cl, ok = re.subn(rf"(?<=## Unreleased: {project} next)", f"\n\n\n{title}", cl)
    assert ok == 1
    path.write_text(cl, "utf8")


if __name__ == "__main__":
    update_changelog()
