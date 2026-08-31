#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.insert(0, Path(__file__).resolve())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
