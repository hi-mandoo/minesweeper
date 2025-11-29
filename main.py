import pygame
import sys
from const import *
import random


# 주변의 mine을 찾아서 개수를 return하는 함수
def calculate_mine_count(mine_field, x, y):
    result = 0  # mine의 개수

    for y_delta in [-1, 0, 1]:
        for x_delta in [-1, 0, 1]:
            try:
                value = mine_field[y + y_delta][x + x_delta]
                if value == FIELD_MINE: result += 1
            except IndexError:
                pass
    return result


def main():
    pygame.init()  # pygame 실행

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 화면 크기 설정

    fps = pygame.time.Clock()

    mine_field = [
        [None for x in range(9)] for y in range(9)
    ]

    max_mine_count = 10
    mine_count = 0

    while mine_count < max_mine_count:
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)

        if mine_field[y][x] is None:
            mine_field[y][x] = FIELD_MINE
            mine_count += 1

    for y in range(9):
        for x in range(9):
            if (mine_field[y][x] == None):
                mine_count = calculate_mine_count(mine_field, x, y)
                mine_field[y][x] = mine_count

    print(mine_field)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 게임 창을 닫는 등의 이벤트가 발생한 상황
                running = False
        surface.fill(BLACK)  # 스크린 검은색으로 초기화

        # 전체 픽셀 / 2 = 화면의 중간지점
        # (한 칸의 크기 * 전체 칸 수) / 2 = 보드의 중간 지점
        # 화면의 중간 지점 - 보드의 중간 지점 = 그리기 시작할 픽셀 위치(가운데 정렬)
        size = int(SCREEN_HEIGHT / 9)
        rect_width = 1

        start_x = SCREEN_WIDTH / 2 - (size * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (size * 9) / 2

        for x in range(9):
            for y in range(9):
                # size + width을 하는 이유는 rect가 맞닿은 선 때문에 굵게 보여서 겹쳐지게 그리기 위함
                rect = (start_x + x * size, start_y + y * size, size + rect_width, size + rect_width)
                pygame.draw.rect(surface, WHITE, rect, rect_width)
                value = mine_field[y][x]

                if value == FIELD_MINE:
                    pygame.draw.rect(surface, WHITE, rect, 10)
                else:
                    pygame.draw.rect(surface, (255, 255, 0), rect, value)  # 숫자 값 만큼 노란색 채우기, 0인 경우 가득 채워

        pygame.display.flip()  # 화면에 반영
        fps.tick(FPS)

    pygame.quit()
    sys.exit()


# 이 파일을 직접 실행할 때만 main()을 호출
if __name__ == "__main__":
    main()
