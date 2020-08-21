import pygame
import os
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
GAME_BALL = pygame.image.load(os.path.join("assets", "ball.png"))

class Player():
    def __init__(self, x, y, width, height, color, player):
        self.player = player
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 10

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if self.player == 1:
            if keys[pygame.K_w]:
                self.y -= self.vel
            if keys[pygame.K_s]:
                self.y += self.vel

        if self.player == 2:
            if keys[pygame.K_UP]:
                self.y -= self.vel
            if keys[pygame.K_DOWN]:
                self.y += self.vel



        if self.y <= 0:
            self.y = 0
        if self.y >= SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def get_x(self):
        return self.x

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = GAME_BALL.convert_alpha()
        self.rect = self.img.get_rect(topleft=(x, y))
        self.velX = 12
        self.velY = 12



    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.x += self.velX
        self.y += self.velY

        if self.y <= 0 or self.y >= SCREEN_HEIGHT - 40:
            self.velY *= -1
            os.system("afplay assets/ball_bounce.wav&")
        if self.x < 0:
            os.system("afplay assets/goal1.wav&")
            self.x = SCREEN_WIDTH / 2 - 15
            self.y = SCREEN_HEIGHT / 2 - 15
            self.velX *= -1
            return 1
        if self.x + self.img.get_width() > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH / 2 - 15
            self.y = SCREEN_HEIGHT / 2 - 15
            os.system("afplay assets/goal1.wav&")
            self.velX *= -1
            return 2

        self.rect.y = self.y
        self.rect.x = self.x
        return 0


    def collision(self, obj):
        if self.rect.colliderect(obj.rect):
            os.system("afplay assets/ball_bounce.wav&")
            self.velX *= -1

