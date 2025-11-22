import pygame
import sys

pygame.init() # pygame 실행

surface = pygame.display.set_mode((320, 235)) # 화면 크기 설정

fps = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 게임 창을 닫는 등의 이벤트가 발생한 상황
            running = False
    surface.fill((0, 0, 0)) # 스크린 검은색으로 초기화

    pygame.display.flip() # 화면에 반영
    fps.tick(60)

pygame.quit()
sys.exit()