### Class GameState
class GameState:
    # !!! ADJUST !!!
    def __init__(self, spot=1, orientation=1, map_size=(9, 4)):
        self.spot = spot
        self.orientation = orientation
        self.map_size = map_size    
        self.connections = {
            1: {'left': 2, 'right': 9},
            2: {'left': 3, 'right': 1},
            3: {'up': 4, 'right': 2},
            4: {'right': 5, 'down': 3},
            5: {'left': 4, 'right': 6},
            6: {'left': 5, 'down': 7},
            7: {'up': 6, 'down': 8},
            8: {'left': 9, 'up': 7},
            9: {'left': 1, 'right': 8}
        }

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
        directions = {1: 'up', 2: 'right', 3: 'down', 4: 'left'}
        return directions[self.orientation]