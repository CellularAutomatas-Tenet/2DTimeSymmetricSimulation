from copy import deepcopy


class Automate:
    SQUARE_SIZE = 1
    PERMUTATION = [[(i, j) for j in range(1)] for i in range(1)]
    OFFSET = (0, 0)
    STATES_COUNT = 1
    DELTA_COLOR = 50
    IS_REVERSED = False

    def invert(self):
        res = Automate()
        res.SQUARE_SIZE = self.SQUARE_SIZE
        res.OFFSET = (-self.OFFSET[0], -self.OFFSET[1])
        res.DELTA_COLOR = self.DELTA_COLOR
        res.STATES_COUNT = self.STATES_COUNT
        res.IS_REVERSED = not self.IS_REVERSED

        res.PERMUTATION = [[(0, 0) for j in range(self.SQUARE_SIZE)] for i in range(self.SQUARE_SIZE)]
        for i in range(self.SQUARE_SIZE):
            for j in range(self.SQUARE_SIZE):
                res.PERMUTATION[self.PERMUTATION[i][j][0]][self.PERMUTATION[i][j][1]] = (i, j)

        return res

    def state_to_color(self, state, forward):
        color = self.DELTA_COLOR + (255 - self.DELTA_COLOR) * state.state / self.STATES_COUNT
        if forward:
            return color, self.DELTA_COLOR, self.DELTA_COLOR
        else:
            return self.DELTA_COLOR, self.DELTA_COLOR, color

    def apply_function(self, field):
        if self.IS_REVERSED:
            self.apply_shift(field)
        new_field = deepcopy(field)
        #print('\n'.join([' '.join([str(y.state) + '--' + str(y.position) for y in x]) for x in field]))
        for x in range(len(field)):
            for y in range(len(field[x])):
                center_position = (x - field[x][y].position[0], y - field[x][y].position[1])
                source_position = self.PERMUTATION[field[x][y].position[0]][field[x][y].position[1]]
                source_position = (center_position[0] + source_position[0], center_position[1] + source_position[1])
                #print(center_position, end=' ')
                #print(source_position)

                if source_position[0] < 0 or source_position[0] >= len(field) \
                        or source_position[1] < 0 or source_position[1] >= len(field[x]):
                    new_field[x][y].reset_state(0)
                else:
                    new_field[x][y].reset_state(field[source_position[0]][source_position[1]].state)

        if not self.IS_REVERSED:
            self.apply_shift(new_field)
        return new_field

    def apply_shift(self, field):
        for x in range(len(field)):
            for y in range(len(field[x])):
                field[x][y].move(self.OFFSET, self.SQUARE_SIZE)


