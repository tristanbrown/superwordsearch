import argparse

from superwordsearch import WordSearch

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path of the input file")
args = parser.parse_args()

def run():
    solution = WordSearch(args.path)
    solution.solve()

if __name__ == "__main__":
    run()
