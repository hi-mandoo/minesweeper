import pygame
import sys

from board import Board
from const import *


def main():
    pygame.init()  # pygame 실행

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 화면 크기 설정

    fps = pygame.time.Clock()

    board = Board()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 게임 창을 닫는 등의 이벤트가 발생한 상황
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.on_click(event.pos, event.button)

        surface.fill(BLACK)  # 스크린 검은색으로 초기화

        board.draw(surface)

        pygame.display.flip()  # 화면에 반영
        fps.tick(FPS)

    pygame.quit()
    sys.exit()


# 이 파일을 직접 실행할 때만 main()을 호출
if __name__ == "__main__":
    main()
