#!/usr/bin/env python

import argparse
import datetime
import os
import random
import subprocess


def setup_arguments():

    parser = argparse.ArgumentParser(description='''
    Git Timemachine - the nostalgic git plguin.
    Git timemachine will show you a random commit from your git repository. When given no arguments it selects a commit
    from the whole history of your project, but you can narrow down the date range it looks at by providing the 'start'
    and 'end' flags.''')

    parser.add_argument("directory", nargs='?', default=os.getcwd(),
                        help="The path to the directory containing your git repository")

    parser.add_argument('--start', help="The start date to limit commits by. Must be in the form of YYYY-mm-dd",
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date())

    parser.add_argument('--end', help="The end date to limit commits by. Must be in the form of YYYY-mm-dd",
                        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date())

    args = parser.parse_args()

    if args.start or args.end:
        assert args.start is not None and args.end is not None, "Must provide both start and end parameters"
        assert args.start < args.end, "The start date must be earlier than the end date"

    return args


def main():

    args = setup_arguments()

    os.chdir(args.directory)

    if args.start:
        command = ["git", "rev-list", "HEAD", "--since", args.start.isoformat(), "--before", args.end.isoformat()]
    else:
        command = ["git", "rev-list", "HEAD"]

    # decode() gives us python3 compatability, since check_output() returns bytes under python3
    commit_list = subprocess.check_output(command).decode().split('\n')
    # get rid of the extra blank line
    commit_list.pop()

    commit = random.choice(commit_list)

    # don't ask me why but subprocess.call() needs git rev-list to have the command as a list
    # but git show has to be a single string
    subprocess.call(["git show %s" % commit], shell=True)


if __name__ == "__main__":
    main()
