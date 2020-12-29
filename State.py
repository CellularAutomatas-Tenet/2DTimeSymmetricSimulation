class State:
    position = (0, 0)
    state = 1

    def __init__(self, s, p):
        self.position = p
        self.state = s

    def reset_state(self, new_state):
        self.state = new_state

    def move(self, direction, square_size):
        self.position = ((self.position[0] + direction[0]) % square_size,
                         (self.position[1] + direction[1]) % square_size)


