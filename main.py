import pygame
from pygame import mixer
from player import Player
from player import Ball
import os
import time

pygame.font.init()

WIDTH = 1000
HEIGHT = 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "field.png")), (WIDTH, HEIGHT))

num_games = 0


def redrawWindow(win, player1, player2, ball, current_score):
    win.blit(BG, (0, 0))
    main_font = pygame.font.SysFont("comicsans", 50)
    score_label = main_font.render(f"{current_score[0]}     -     {current_score[1]}", 1, (255, 255, 255))
    win.blit(score_label, (WIDTH / 2 - score_label.get_width() / 2, HEIGHT - score_label.get_height()))

    player1.draw(win)
    player2.draw(win)
    ball.draw(win)
    pygame.display.update()


ball = Ball(WIDTH / 2 - 15, HEIGHT / 2 - 15)
player1 = Player(0, 250, 10, 100, (255, 0, 0), 1)
player2 = Player(WIDTH - 10, 250, 10, 100, (0, 0, 255), 2)


def main():
    run = True
    clock = pygame.time.Clock()

    current_score = [0, 0]

    while run:
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        ball.collision(player1)
        ball.collision(player2)
        player1.move()
        player2.move()
        score = ball.move()
        if score == 1:
            current_score[1] += 1
        if score == 2:
            current_score[0] += 1
        if current_score[0] >= 5 or current_score[1] >= 5:
            run = False
            global num_games
            num_games += 1

        redrawWindow(win, player1, player2, ball, current_score)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.blit(BG, (0, 0))
        font = pygame.font.SysFont("comicsans", 80)
        if num_games > 0:
            text = font.render("Press to Play Again!", 1, (255, 255, 255))
        else:
            text = font.render("Press to Start Game!", 1, (255, 255, 255))
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                mixer.init()
                mixer.music.load('assets/crowd.aiff')
                pygame.mixer.music.set_volume(0.3)
                mixer.music.play(-1)

    main()


while True:
    menu_screen()
