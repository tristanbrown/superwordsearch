"""Contains the class for solving the superwordsearch."""

import numpy as np

from superwordsearch import util

class WordSearch():
    def __init__(self, path):
        self.shape = self.mode = self.board = self.words = None
        self.load_inputs(path)

    def load_inputs(self, path):
        """Load the word search parameters from an input file at 'path'."""
        print(f"Loading board from {path}")
        with open(path, 'r') as f:
            lines = f.read().splitlines()
        self.shape = np.array([int(i) for i in lines[0].split()])
        self.board = np.array([list(row) for row in lines[1:self.shape[0]+1]])
        self.index = np.indices(self.shape)
        self.mode = lines[self.shape[0]+1]
        self.words = lines[self.shape[0]+3:]
        print(f"Board:\n{self.board}")
        print(f"Shape:\n{self.shape}")
        print(f"Mode:\n{self.mode}")
        print(f"Words:\n{self.words}")

    def search_path(self, direction):
        """Generate """
        all_coords = util.get_coordinates(self.shape)



    def solve(self):
        """Find the loaded words in the loaded board, using the loaded mode."""
        print("Solving")
        directions = [[1, 0], [0, 1], [1, 1], [1, -1]]
        search_paths = [self.search_path(direction) for direction in directions]
        print(search_paths)


        
