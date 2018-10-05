import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np


class Tile:
    def __init__(self, terrain=None, occupant=None):
        if terrain is None:
            self.terrain = 'Plains'
        else:
            self.terrain = terrain

        self.occupant = occupant

        self._init_dict = {
            'altitude': 0,
            'water': 0,
            'vegetation': 0
            }

        self.color = 'b'


class Map:
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height
        self.map = []

        if (width is not None) and (height is not None):
            self.init_map()

        self._directions = {
            'NE': [-1, 1],
            'NW': [-1, -1],
            'E':  [0, 2],
            'W':  [0, -2],
            'SE': [1, 1],
            'SW': [1, -1],
        }

    def clear_map(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if (y % 2 == 0) and (x % 2 == 0):
                    self.map[y][x] = None
                elif ((y+1) % 2 == 0) and ((x+1) % 2 == 0):
                    self.map[y][x] = None
                else:
                    self.map[y][x] = Tile()

    def init_map(self):
        self.map = np.zeros((self.height, (self.width*2)-1)).tolist()
        self.clear_map()

    def range_one(self, x, y):
        neighbors = []
        for key in self._directions:
            neighbors.append([a + b for a, b in zip([y, x], self._directions[key])])

        for neighbor in neighbors:
            print(neighbor)

    def render(self):
        fig, ax = plt.subplots(figsize=(5,5), dpi=300)
        ax.set_aspect('equal')
        # TODO: Figure out proper math for x multiplier
        for x in range((self.width*2)-1):
            for y in range(self.height):
                if self.map[y][x] is not None:
                    hex = RegularPolygon((x*0.58, y),
                                         numVertices=6,
                                         radius=2/3,
                                         orientation=0,
                                         facecolor=self.map[y][x].color,
                                         alpha=0.2,
                                         edgecolor='k')
                    ax.add_patch(hex)
        plt.xlim(-3/4, self.width*1.13)
        plt.ylim(-3/4, self.height)
        plt.show()


m = Map(width=13, height=9)
m.render()