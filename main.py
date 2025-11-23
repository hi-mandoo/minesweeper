import pygame
import sys

def main():
    pygame.init() # pygame 실행

    surface = pygame.display.set_mode((320, 240)) # 화면 크기 설정

    fps = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 게임 창을 닫는 등의 이벤트가 발생한 상황
                running = False
        surface.fill((0, 0, 0)) # 스크린 검은색으로 초기화

        # 전체 픽셀 / 2 = 화면의 중간지점
        # (한 칸의 크기 * 전체 칸 수) / 2 = 보드의 중간 지점
        # 화면의 중간 지점 - 보드의 중간 지점 = 그리기 시작할 픽셀 위치(가운데 정렬)
        size = 26
        width = 1

        start_x = 320 / 2 - (size * 9) / 2
        start_y = 240 / 2 - (size * 9) / 2
        COLOR_WHITE = (255, 255, 255)

        for x in range(9):
            for y in range(9):
                # size + width을 하는 이유는 rect가 맞닿은 선 때문에 굵게 보여서 겹쳐지게 그리기 위함
                rect = (start_x + x * size, start_y + y * size, size + width, size + width)
                pygame.draw.rect(surface, COLOR_WHITE, rect, width)

        pygame.display.flip() # 화면에 반영
        fps.tick(60)

    pygame.quit()
    sys.exit()

# 이 파일을 직접 실행할 때만 main()을 호출
if __name__ == "__main__":
    main()