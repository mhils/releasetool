#!/usr/bin/env -S python3 -u
import logging
import re
import sys
from pathlib import Path

from .common import project
from .common import get_version

logger = logging.getLogger(__name__)


def update_python_version(
    path: Path | str = f"{project}/__init__.py",
    version: str = "",
):
  logger.info(f"➡️ Updating {path}...")
  path = Path(path)
  cl = path.read_text("utf8")
  cl, ok = re.subn(
      r"""
  (
      ^__version__[ \t]*=[ \t]*["']
  )
  [^"']+
  """,
      rf"\g<1>{version or get_version()}",
      cl,
      flags=re.VERBOSE | re.MULTILINE,
  )
  assert ok == 1, f"{ok=}"
  path.write_text(cl, "utf8")


if __name__ == "__main__":
  update_python_version(
      Path(sys.argv[1]),
      sys.argv[2] if len(sys.argv) > 2 else ""
  )
