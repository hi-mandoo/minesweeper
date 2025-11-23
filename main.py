import pygame
import sys

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
    start_x = 320 / 2 - (26 * 9) / 2
    start_y = 240 / 2 - (26 * 9) / 2

    for x in range(9):
        for y in range(9):
            pygame.draw.rect(surface, (255, 255, 255),
                             (start_x + x * 26, start_y + y * 26, 27, 27), 1)

    pygame.display.flip() # 화면에 반영
    fps.tick(60)

pygame.quit()
sys.exit()