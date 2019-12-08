"""Contains the class for solving the superwordsearch."""
import itertools
import logging
import numpy as np

from superwordsearch import util

class WordSearch():
    def __init__(self, path):
        self.shape = self.mode = self.grid = self.words = None
        self.load_inputs(path)

    def load_inputs(self, path):
        """Load the word search parameters from an input file at 'path'."""
        logging.debug(f"Loading wordsearch from {path}")
        with open(path, 'r') as f:
            lines = f.read().splitlines()
        self.shape = np.array([int(i) for i in lines[0].split()])
        self.grid = np.array([list(row) for row in lines[1:self.shape[0]+1]])
        self.mode = lines[self.shape[0]+1]
        self.words = lines[self.shape[0]+3:]
        logging.debug(f"Grid:\n{self.grid}")
        logging.debug(f"Shape:\n{self.shape}")
        logging.debug(f"Mode:\n{self.mode}")
        logging.debug(f"Words:\n{self.words}")

    def search_path(self, start, direction, word, lapped):
        """Search for the remainder of a word along a linear path.

        Returns either:
            end coordinates (tuple), if the full word is found; Or
            False
        """
        next_pos = np.array(start) + np.array(direction)
        logging.debug(f"Checking {next_pos} for {word}")
        if (self.mode == "NO_WRAP") and util.out_of_bounds(next_pos, self.shape):
            return False
        next_pos = tuple(util.wrap(next_pos, np.array(self.shape)))
        if next_pos == lapped:
            return False
        if self.grid[next_pos] == word[0]:
            if len(word) == 1:
                return next_pos
            else:
                return self.search_path(next_pos, direction, word[1:], lapped)
        return False

    def find_word(self, word):
        """Searches for a word in the grid.

        Returns either:
            the start and end coordinates of the word; Or
            "NOT FOUND"
        """
        starts = self.find_letter(word[0])
        logging.debug(f"First letter of {word} found at {starts}")
        directions = [[1, 0], [0, 1], [1, 1], [1, -1],
                      [-1, 0], [0, -1], [-1, -1], [-1, 1]]
        for start, direction in itertools.product(starts, directions):
            end = self.search_path(start, direction, word[1:], start)
            if end:
                return start, end
        return "NOT FOUND"

    def find_letter(self, letter):
        """Find all of the copies of a letter in the grid.

        Returns a list of tuples, representing coordinates.
        """
        coords = np.where(self.grid == letter)
        return util.tuple_coords(coords)

    def solve(self):
        """Find the loaded words in the loaded board, using the loaded mode."""
        logging.debug("Solving")
        for word in self.words:
            loc = self.find_word(word)
            print(loc)
