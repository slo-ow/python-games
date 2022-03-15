import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load(
    "/Volumes/Project/python-games/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
chracter = pygame.image.load(
    "/Volumes/Project/python-games/pygame_basic/chracter.png")
chracter_size = chracter.get_rect().size  # 이미지 크기를 구해옴
chracter_width = chracter_size[0]  # 캐릭터 가로 크기
chracter_heigth = chracter_size[1]  # 캐릭터 세로 크기
chracter_x_pos = (screen_width / 2) - (chracter_width / 2)  # 화면 가로의 절반 크기
chracter_y_pos = screen_height - chracter_heigth  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 속도
chracter_speed = 0.6

# 적 enenmy 캐릭터
enemy = pygame.image.load(
    "/Volumes/Project/python-games/pygame_basic/enemy.png")
enemy_size = chracter.get_rect().size  # 이미지 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터 가로 크기
enemy_heigth = enemy_size[1]  # 캐릭터 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면 가로의 절반 크기
# 화면 세로 크기 가장 아래에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - (enemy_heigth / 2)

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

# 캐릭터가 100 만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5 * 20 = 100

    #print("FPS : " + str(clock.get_fps()))

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창을 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= chracter_speed  # to_x = to_x -5
            if event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += chracter_speed
            if event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= chracter_speed
            if event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += chracter_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    chracter_x_pos += to_x * dt
    chracter_y_pos += to_y * dt
    # 가로 경계값 처리
    if chracter_x_pos < 0:
        chracter_x_pos = 0
    elif chracter_x_pos > screen_width - chracter_width:
        chracter_x_pos = screen_width - chracter_width

    # 세로 경계값 처리
    if chracter_y_pos < 0:
        chracter_y_pos = 0
    elif chracter_y_pos > screen_height - chracter_heigth:
        chracter_y_pos = screen_height - chracter_heigth

    # 충돌 처리
    chracter_rect = chracter.get_rect()
    chracter_rect.left = chracter_x_pos
    chracter_rect.top = chracter_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if chracter_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(chracter, (chracter_x_pos, chracter_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    pygame.display.update()  # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()
