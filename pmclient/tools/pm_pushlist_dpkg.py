#!/usr/bin/python3

from sys import exit, path
path.insert(0, '.')

import logging

from argparse import ArgumentParser

from pmclient.system.system_types import get_system_imps, SYS_UBUNTU
from pmclient.system.repo_types import get_repo_imps, SYS_DPKG
from pmclient.client import Client

if __name__ == '__main__':
    parser = ArgumentParser(description='Package-list push for DPKG.')
    parser.add_argument('-v', '--verbose', action='store_true', help="Show logging.")

    result = parser.parse_args()

    if result.verbose:
        from pmclient import logging_config

    system_profiler = get_system_imps(SYS_UBUNTU)
    package_list_getter = get_repo_imps(SYS_DPKG)

    # Gather data.

    package_list = package_list_getter().get_package_list()

    try:
        Client(system_profiler).list_push(package_list)
    except Exception as e:
        logging.exception("There was a problem pushing.")
        exit(1)

    print("Push successful.")
    exit(0)
