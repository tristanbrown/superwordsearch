import argparse
import logging

from superwordsearch import WordSearch

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path of the input file")
parser.add_argument("--debug", help="Turn on debug mode", action="store_true")
args = parser.parse_args()

def run():
    if args.debug:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    logging.basicConfig(level=loglevel)
    solution = WordSearch(args.path)
    solution.solve()

if __name__ == "__main__":
    run()
