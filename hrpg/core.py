#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

hrpg: commandline interface for http://habitrpg.com
http://github.com/philadams/hrpg
"""


from docopt import docopt


def cli():
    """HabitRPG command-line interface.

    usage:
      hrpg status
      hrpg user [<uid>]
      hrpg tasks (--habit | --daily | --todo | --reward) [<uid>]
      hrpg task <tid> [<uid>]
      hrpg
      hrpg --version

    options:
      -h --help     Show this screen.
      --version     Show version.

    Subcommands:
      status        Get status of HabitRPG service
      user          Get user <uid> status
      tasks         Get user <uid> tasks
      task          Get task <tid> details
      <none>        Get user status for this user (convenience)
    """
    args = docopt(cli.__doc__, version='hrpg version 0.0.2')


if __name__ == '__main__':
    cli()