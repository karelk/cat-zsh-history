#!/bin/python3

import os, sys, datetime

for f in sys.argv[1:]:
    try:
        with open(f, 'r') as f:

            content = '\n' + f.read().rstrip('\n')
            lines = content.split('\n: ')

            # skip first (empty) line
            for line in lines[1:]:

                tmp = line.split(';',1)
                date = int(tmp[0].split(':')[0])
                command = tmp[1].replace('\\\n', " ; ")
                print(' ' + datetime.datetime.fromtimestamp(date).strftime("(%a) %Y-%b-%d %H:%M") + '  ' + command )

    except FileNotFoundError as e:
        print(e)

