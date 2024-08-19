#!/usr/bin/env python

import os
import argparse
import sys
import json
from os.path import exists, dirname, basename, join, expanduser
from glob import glob
import pandas as pd
import numpy as np


HELP_PARAGRAPHS = {
    'main':'an example cli tool',
    'collect': {
        'main':'collect data',
        'collect-all':'execute all queued API calls, based on config.',
    },
    'inspect': {
        'main':'inspect data',
        'print-latest':'show timestamp of latest file',
        'retrieve-kml':'dump kml path files for all collected places',
        'update-data-archive':'process all xml files and write csv file.',
    },
}


def main():
    parser = argparse.ArgumentParser(description=HELP_PARAGRAPHS['main'])
    subparsers = parser.add_subparsers(dest='command', help='')

    h = HELP_PARAGRAPHS['collect']
    parser_collect = subparsers.add_parser('collect', help=h['main'])
    parser_collect.add_argument('--collect-all', '-a', required=False,
                                action='store_true', help=h['collect-all'])

    h = HELP_PARAGRAPHS['inspect']
    parser_inspect = subparsers.add_parser('inspect', help=h['main'])
    parser_inspect.add_argument('--print-latest', '-l', required=False,
                                default=False, action='store_true',
                                help=h['print-latest'])
    parser_inspect.add_argument('--retrieve-kml', required=False, default=False,
                                action='store_true', help=h['retrieve-kml'])
    parser_inspect.add_argument('--update-data-archive', required=False,
                                default=False, action='store_true',
                                help=h['update-data-archive'])
    args = parser.parse_args()

    if args.command == 'collect':
        if args.collect_all:
            from zero_wrong_average.main import get_all
            get_all()

    elif args.command == 'inspect':
        if args.print_latest:
            from zero_wrong_average.main import latest
            latest()
        if args.retrieve_kml:
            from zero_wrong_average import convert_to_kml as kml
            kml.write_kml_files()
        if args.update_data_archive:
            from zero_wrong_average.proc_data import collect
            collect()


if __name__ == '__main__':
    main()
