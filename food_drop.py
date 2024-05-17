import pygame
import random

pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 화면 크기 설정
size = (400, 600)
screen = pygame.display.set_mode(size)

# Pygame Clock 객체 생성
clock = pygame.time.Clock()

# 이미지 로드 및 크기 조정
person = pygame.image.load('images/plane.png')
person = pygame.transform.scale(person, (60, 45))
heart = pygame.image.load('images/heart.png')
heart = pygame.transform.scale(heart, (30, 30))

# 폰트 설정
font = pygame.font.SysFont(None, 36)

# 장애물 클래스 정의
class Obstacle:
    def __init__(self, x, y, image, speed):  # 장애물의 초기 위치, 이미지, 속도를 설정하는 생성자
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed

    def move(self):  # 장애물을 아래로 이동시키는 메서드
        self.y += self.speed

    def draw(self):  # 장애물을 화면에 그리는 메서드
        screen.blit(self.image, (self.x, self.y))

    def reset_pos(self):  # 장애물이 화면을 벗어나면 위치를 재설정하는 메서드
        self.x = random.randint(0, size[0] - self.image.get_width())
        self.y = -self.image.get_height()
        self.speed = random.randint(3, 6)

# 게임 실행 함수 정의
def runGame():
    x = 20
    y = size[1] - 45
    speed = 5
    score = 0
    lives = 3  # 초기 하트 개수

    obstacles = []  # 장애물 객체를 저장하는 리스트

    obstacle_timer = 0  # 장애물 생성 타이머
    poo_spawn_interval = 2000  # 똥 생성 간격 초기값 (밀리초)
    difficulty_timer = pygame.time.get_ticks()  # 난이도 증가 타이머

    done = False

    while not done:
        clock.tick(30)  # 초당 30 프레임으로 설정
        screen.fill(WHITE)  # 화면을 흰색으로 지움

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed

        if x < 0:
            x = 0
        elif x > size[0] - 60:
            x = size[0] - 60

        # 난이도 증가: 5초마다 똥 생성 간격을 줄임
        if pygame.time.get_ticks() - difficulty_timer > 1000:  # 5초마다
            poo_spawn_interval = max(100, poo_spawn_interval - 100)  # 최소 500ms까지 감소
            difficulty_timer = pygame.time.get_ticks()

        # 장애물 생성 타이머 업데이트
        if pygame.time.get_ticks() - obstacle_timer > poo_spawn_interval:
            obstacle_type = random.choice(['apple', 'poo', 'heart'])
            if obstacle_type == 'apple':
                image = pygame.image.load('images/apple_1.png')
            elif obstacle_type == 'poo':
                image = pygame.image.load('images/poop_2.png')
            else:
                image = pygame.image.load('images/heart.png')
            
            # 장애물 크기 랜덤 설정
            if obstacle_type in ['apple', 'poo']:
                width = random.randint(20, 50)
                height = width  # 정사각형 형태로 만들기 위해 동일한 값을 사용
            else:
                width = 30
                height = 30

            image = pygame.transform.scale(image, (width, height))
            obstacle = Obstacle(random.randint(0, size[0] - width), -height, image, random.randint(3, 6))
            obstacles.append(obstacle)
            obstacle_timer = pygame.time.get_ticks()

        # 장애물 이동 및 충돌 처리
        for obstacle in obstacles:
            obstacle.move()
            if obstacle.y > size[1]:
                obstacles.remove(obstacle)

            if x < obstacle.x < x + 60 and y < obstacle.y < y + 45:
                if obstacle.image == image:
                    if obstacle_type == 'apple':
                        score += 10
                    elif obstacle_type == 'poo':
                        lives -= 1 # 하트 개수 감소
                        score += 10
                        if lives == 0:  # 하트가 0개가 되면 게임 종료
                            done = True
                    elif obstacle_type == 'heart':
                        lives = min(3, lives + 1)  # 하트 개수 최대 3개로 제한
                obstacles.remove(obstacle)

            obstacle.draw()

        screen.blit(person, (x, y))

        # 점수와 하트를 화면에 표시
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        for i in range(lives):
            screen.blit(heart, (10 + i * 40, 50))

        pygame.display.update()

runGame()
pygame.quit()
