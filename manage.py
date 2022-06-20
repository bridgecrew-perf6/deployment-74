#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    settings_module = 'quickstartproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'quickstartproject.settings'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CNX_Protect.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print("Execution Started2")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    print("Execution Started1")
    main()
