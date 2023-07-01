import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏窗口的大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 赛车的大小
CAR_WIDTH = 50
CAR_HEIGHT = 100

# 颜色定义
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('赛车游戏')

clock = pygame.time.Clock()

def draw_car(x, y):
    pygame.draw.rect(window, RED, (x, y, CAR_WIDTH, CAR_HEIGHT))

def draw_obstacle(x, y, width, height):
    pygame.draw.rect(window, WHITE, (x, y, width, height))

def display_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score), True, WHITE)
    window.blit(text, (10, 10))

def game_over():
    font = pygame.font.Font(None, 50)
    text = font.render("Game Over", True, WHITE)
    window.blit(text, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 25))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    car_x = WINDOW_WIDTH // 2 - CAR_WIDTH // 2
    car_y = WINDOW_HEIGHT - CAR_HEIGHT - 10
    car_speed = 5

    obstacle_width = random.randint(50, 200)
    obstacle_height = 30
    obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    obstacle_speed = 5

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < WINDOW_WIDTH - CAR_WIDTH:
            car_x += car_speed

        obstacle_y += obstacle_speed
        if obstacle_y > WINDOW_HEIGHT:
            obstacle_width = random.randint(50, 200)
            obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            score += 1

        if car_y < obstacle_y + obstacle_height and car_y + CAR_HEIGHT > obstacle_y:
            if car_x + CAR_WIDTH > obstacle_x and car_x < obstacle_x + obstacle_width:
                game_over()

        window.fill((0, 0, 0))
        draw_car(car_x, car_y)
        draw_obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        display_score(score)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
