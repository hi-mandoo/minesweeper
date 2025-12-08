import random
import pygame
from const import *


class Board:
    def __init__(self):
        self.mine_field = [
            [None for _ in range(9)] for _ in range(9)
        ]

        self.state_field = [
            [STATE_HIDDEN for _ in range(9)] for _ in range(9)
        ]

        self.font = pygame.font.Font(None, 17)

        max_mine_count = 10
        mine_count = 0

        while mine_count < max_mine_count:
            x = random.randrange(0, 9)
            y = random.randrange(0, 9)

            if self.mine_field[y][x] is None:
                self.mine_field[y][x] = FIELD_MINE
                mine_count += 1

        for y in range(9):
            for x in range(9):
                if (self.mine_field[y][x] == None):
                    mine_count = self.calculate_mine_count(x, y)
                    self.mine_field[y][x] = mine_count

        print(self.mine_field)

    def draw(self, surface):
        # 전체 픽셀 / 2 = 화면의 중간지점
        # (한 칸의 크기 * 전체 칸 수) / 2 = 보드의 중간 지점
        # 화면의 중간 지점 - 보드의 중간 지점 = 그리기 시작할 픽셀 위치(가운데 정렬)
        size = int(SCREEN_HEIGHT / 9)

        start_x = SCREEN_WIDTH / 2 - (size * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (size * 9) / 2

        for x in range(9):
            for y in range(9):
                # size + width을 하는 이유는 rect가 맞닿은 선 때문에 굵게 보여서 겹쳐지게 그리기 위함
                rect = (start_x + x * size, start_y + y * size, size + 1, size + 1)
                pygame.draw.rect(surface, WHITE, rect, 1)

                fill_rect = (start_x + x * size + 2, start_y + y * size + 2, size + 1 - 3, size + 1 - 3)
                state = self.state_field[y][x]
                if state == STATE_HIDDEN:
                    pygame.draw.rect(surface, GREY, fill_rect, 0)
                elif state == STATE_OPEN:
                    mine = self.mine_field[y][x]
                    text = self.font.render(f"{mine}", True, WHITE, None)
                    text_rect = text.get_rect(center=(start_x + x * size + size / 2, start_y + y * size + size / 2))
                    surface.blit(text, text_rect)

    # 주변의 mine을 찾아서 개수를 return하는 함수
    def calculate_mine_count(self, x, y):
        result = 0  # mine의 개수

        for y_delta in [-1, 0, 1]:
            for x_delta in [-1, 0, 1]:
                try:
                    value = self.mine_field[y + y_delta][x + x_delta]
                    if value == FIELD_MINE: result += 1
                except IndexError:
                    pass
        return result

    def on_click(self, pos, button):
        print(f"pos: {pos}, button: {button}")
        size = int(SCREEN_HEIGHT / 9)
        start_x = SCREEN_WIDTH / 2 - (size * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (size * 9) / 2
        relative_pos = (pos[0] - start_x, pos[1] - start_y)

        # board를 벗어난 경우
        if relative_pos[0] < 0: return
        if relative_pos[1] < 0: return

        if size * 9 < relative_pos[0]: return
        if size * 9 < relative_pos[1]: return

        # index 좌표 계산
        index_pos = (int(relative_pos[0] / size), int(relative_pos[1] / size))
        print("index_pos: ", index_pos)

        self.state_field[index_pos[1]][index_pos[0]] = STATE_OPEN
