### Class GameState
class GameState:
    # !!! ADJUST !!!
    def __init__(self, spot=1, orientation=1, map_size=(25, 4)):
        self.spot = spot
        self.orientation = orientation
        self.map_size = map_size    
        self.connections = {
            1: {'l': 2, 'r': 9},
            2: {'l': 3, 'r': 1},
            3: {'u': 4, 'r': 2, 'l': 20},
            4: {'r': 5, 'd': 3},
            5: {'l': 4, 'r': 6},
            6: {'l': 5, 'd': 7},
            7: {'u': 6, 'd': 8, 'r': 10},
            8: {'l': 9, 'u': 7},
            9: {'l': 1, 'r': 8},
            10: {'l': 7, 'r': 11},
            11: {'l': 10, 'r': 12},
            12: {'l': 11, 'r': 13},
            13: {'l': 12, 'r': 14},
            14: {'l': 13, 'u': 15, 'd': 18},
            15: {'d': 14, 'l': 16},
            16: {'u': 17, 'r': 15},
            17: {'d': 16},
            18: {'u': 14, 'l': 19},
            19: {'r': 18},
            20: {'l': 21, 'r': 3},
            21: {'u': 22, 'r': 20},
            22: {'d': 21, 'l': 23},
            23: {'l': 24, 'r': 22},
            24: {'r': 23, 'd': 25},
            25: {'u': 24}
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