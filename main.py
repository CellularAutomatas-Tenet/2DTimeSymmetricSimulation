import pygame
import Visualization
import State
import AutomataConfig
from copy import deepcopy

Visualization.__init__()

automate = AutomataConfig.Automate()

field_size = int(input('Введите размер поля\n'))
automate.STATES_COUNT = int(input('Введите количество состояний\n'))
automate.SQUARE_SIZE = int(input('Введите размер квадрата'))
automate.PERMUTATION = [[(i, j) for j in range(automate.SQUARE_SIZE)] for i in range(automate.SQUARE_SIZE)]

field = [[State.State(0, (i % automate.SQUARE_SIZE, j % automate.SQUARE_SIZE)) for i in range(field_size)] for j in range(field_size)]

print('Теперь введите по очереди все состояния ячеек в формате "x y state"\n')
print('Когда закончите, напишите "-1"\n')
answer = list(map(int, input().split()))
while len(answer) != 1:
    field[answer[0]][answer[1]].reset_state(answer[2] % automate.STATES_COUNT)
    answer = list(map(int, input().split()))


print('Теперь введите правило перестановки в формате "x y x1 y1"')
for e in range(automate.SQUARE_SIZE ** 2):
    s = list(map(int, input().split()))
    automate.PERMUTATION[s[0]][s[1]] = (s[2], s[3])

automate.OFFSET = tuple(map(int, input('Введите сдвиг в формате "x y"\n').split()))

reversed_automate = automate.invert()
field_2 = deepcopy(field)
Visualization.draw(field, field_2, automate, reversed_automate)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                field = automate.apply_function(field)
                field_2 = automate.apply_function(field_2)
                Visualization.draw(field, field_2, automate, reversed_automate)
            if event.key == pygame.K_SPACE:
                tmp = deepcopy(field)
                field = field_2
                field_2 = deepcopy(tmp)

                field = automate.apply_function(field)
                field_2 = automate.apply_function(field_2)

                tmp1 = deepcopy(field)
                field = field_2
                field_2 = deepcopy(tmp)
                Visualization.draw(field, field_2, automate, reversed_automate)
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False


