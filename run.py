
#!/usr/bin/env python

import adsputils
import argparse

from adsdata import memory_cache, process, tasks

app = tasks.app


def main():
    parser = argparse.ArgumentParser(description='Process user input.')
    parser.add_argument('-b', '--bibcodes', dest='bibcodes', action='store',
                        help='A list of bibcodes separated by spaces')
    parser.add_argument('--no-metrics', dest='compute_metrics', action='store_false',
                        help='after cache init user can enter bibcodes')
    parser.add_argument('-i', '--interactive', dest='interactive', action='store_true',
                        help='after cache init user can enter bibcodes')
    args = parser.parse_args()

    if args.bibcodes:
        args.bibcodes = args.bibcodes.split(' ')
        args.bibcodes.sort()

    if args.compute_metrics is True:
        c = memory_cache.init()    
        print 'cache created'

    if args.bibcodes:
        process.process_bibcodes(args.bibcodes, compute_metrics=args.compute_metrics)
    elif args.interactive:
        while True:
            i = raw_input('enter bibcode: ')
            process.process_bibcodes([i.strip()], compute_metrics=args.compute_metrics)
    else:
        process.process(compute_metrics=args.compute_metrics)
    

if __name__ == '__main__':
    main()
