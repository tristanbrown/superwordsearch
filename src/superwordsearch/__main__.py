import argparse

from superwordsearch import Solver

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Path of the input file")
args = parser.parse_args()

def run():
    solution = Solver(args.path)
    solution.solve()

if __name__ == "__main__":
    run()
