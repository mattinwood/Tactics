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

    # def neighbors(self, map_object):


class Map:
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height


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

    def clear_hex_coordinates(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if (y % 2 == 0) and (x % 2 == 0):
                    self.map[y][x] = None
                elif ((y+1) % 2 == 0) and ((x+1) % 2 == 0):
                    self.map[y][x] = None
                else:
                    self.map[y][x] = Tile()

    def init_map(self):
        self.map = np.zeros((self.height, self.width)).tolist()
        self.clear_hex_coordinates()

    # Generates a horizontal stacked hex map
    def generate(self, shape='square'):
        if shape == 'square':
            for y in range(self.height):
                for x in range(self.width):
                    if (y % 2 == 0):
                        self.map.append(Tile(coordinates=(x, y/2)))
                    else:
                        self.map.append(Tile(coordinates=(x+0.5, y/2)))
        elif shape == 'hex':
            pass
        else:
            raise NameError('No shape with name "{0}"'.format(shape))

    def range_one(self, x, y):
        neighbors = []
        for key in self._directions:
            neighbors.append([a + b for a, b in zip([y, x], self._directions[key])])

        for neighbor in neighbors:
            print(neighbor)