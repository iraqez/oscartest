#!/usr/bin/env python

import sys
from osenv import osenv

if __name__ == "__main__":
    osenv

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
