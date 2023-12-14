import pygame

pygame.init()
pygame.mixer.music.load("./audio/pa.mp3")
pygame.mixer.music.play(-1)
n = int(input(": 1"))
while n == '1':
    pygame.event.wait()