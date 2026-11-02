### Class GameState
class GameState:
    # !!! ADJUST !!!
    def __init__(self, spot=1, orientation=1, map_size=(55, 4)):
        self.spot = spot
        self.orientation = orientation
        self.map_size = map_size    
        self.connections = {
            1: {'u': 2, 'd': 7},
            2: {'u': 3, 'd': 1},
            3: {'l': 11, 'r': 4, 'd': 2},
            4: {'r': 5, 'l': 3},
            5: {'l': 4, 'd': 6, 'r': 21},
            6: {'u': 5, 'l': 7},
            7: {'l': 8, 'r': 6, 'u': 1},
            8: {'l': 9, 'r': 7},
            9: {'r': 8, 'u': 10, 'd': 81},
            10: {'l': 51, 'r': 11, 'd': 9},
            11: {'l': 10, 'r': 3},
            21: {'l': 5, 'r': 22},
            22: {'l': 21, 'r': 31},
            31: {'l': 22, 'r': 32, 'd': 40},
            32: {'l': 31, 'r': 33},
            33: {'l': 32, 'r': 34},
            34: {'l': 33, 'd': 35},
            35: {'u': 34, 'd': 36},
            36: {'u': 35, 'd': 37},
            37: {'u': 36, 'd': 38},
            38: {'u': 37, 'l': 39},
            39: {'u': 40, 'r': 38},
            40: {'u': 31, 'd': 39},
            51: {'r': 10, 'l': 52},
            52: {'r': 51, 'l': 53},
            53: {'r': 52, 'l': 54},
            54: {'r': 53, 'l': 61, 'd': 79},
            61: {'r': 54, 'l': 62, 'd': 66},
            62: {'r': 61, 'u': 63, 'd': 71},
            63: {'d': 62, 'u': 64},
            64: {'d': 63, 'l': 67, 'r': 65},
            65: {'d': 66, 'l': 64},
            66: {'u': 65, 'd': 61},
            67: {'l': 68, 'r': 64},
            68: {'r': 67},
            71: {'u': 62, 'r': 72, 'd': 74},
            72: {'d': 73, 'l': 71},  # was 'l': 72 (dead end looping on itself)
            73: {'u': 72, 'l': 74, 'r': 76},
            74: {'u': 71, 'r': 73, 'd': 75},
            75: {'u': 74},
            76: {'l': 73, 'r': 77},
            77: {'l': 76, 'u': 78},
            78: {'d': 77, 'u': 79},
            79: {'d': 78, 'u': 54},
            81: {'u': 9, 'l': 82, 'r': 86},
            82: {'r': 81, 'l': 83, 'd': 91},
            83: {'r': 82, 'l': 85, 'd': 84},
            84: {'u': 83},
            85: {'r': 83},
            86: {'l': 81, 'd': 87},
            87: {'u': 86, 'd': 88},
            88: {'u': 87, 'l': 89},
            89: {'r': 88, 'l': 90},
            90: {'r': 89, 'l': 91},
            91: {'u': 82, 'r': 90}
        }

    def can_go_forward(self):
        next_spot = self.connections.get(self.spot, {}).get(self._orientation_to_direction(), None)
        return next_spot


    def turn_right(self):
        self.orientation = (self.orientation % 4) + 1
    
    def turn_left(self):
        self.orientation = (self.orientation - 2) % 4 + 1
    
    def u_turn(self):
        self.orientation = (self.orientation + 1) % 4 + 1
    
    def go_straight(self):
        next_spot = self.connections.get(self.spot, {}).get(self._orientation_to_direction(), None)
        if next_spot:
            self.spot = next_spot

    def _orientation_to_direction(self):
        directions = {1: 'u', 2: 'r', 3: 'd', 4: 'l'}
        return directions[self.orientation]