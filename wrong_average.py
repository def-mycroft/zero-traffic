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
        'test':'test 1 24Q17 ',
        'print-latest':'show timestamp of latest file',
    },
    'level2': {
        'main':'level 2',
        'third-thing':'docs for third thing',
        'fourth-thing':'docs for fourth thing',
    },
}


def main():
    parser = argparse.ArgumentParser(description=HELP_PARAGRAPHS['main'])
    subparsers = parser.add_subparsers(dest='command', help='')

    h = HELP_PARAGRAPHS['collect']
    parser_corpus = subparsers.add_parser('collect', help=h['main'])
    parser_corpus.add_argument('--test', '-t', required=False,
                               action='store_true', help=h['test'])
    parser_corpus.add_argument('--print-latest', '-l', required=False,
                               default=False, action='store_true',
                               help=h['print-latest'])

    h = HELP_PARAGRAPHS['level2']
    parser_summ = subparsers.add_parser('level2', help=h['main'])
    parser_summ.add_argument('--third-thing', '-t', required=False,
                             default=False, action='store_true',
                             help=h['third-thing'])
    parser_summ.add_argument('--fourth-thing', '-f', required=False,
                             default=False, action='store_true',
                             help=h['fourth-thing'])
    args = parser.parse_args()

    if args.command == 'collect':
        if args.test:
            from zero_wrong_average.main import get
            get()
        elif args.print_latest:
            from zero_wrong_average.main import latest
            latest()

    elif args.command == 'level2':
        if args.third_thing:
            print('3rd')
        elif args.fourth_thing:
            print('4th')

if __name__ == '__main__':
    main()
