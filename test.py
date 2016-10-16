#coding: UTF-8

import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,750))
pygame.display.set_caption("Test Demo")

#加载图形
BackGround = pygame.image.load("1.png").convert()  # 加载背景
Heart = pygame.image.load("heart.png").convert_alpha()
width,height = Heart.get_size()  #获得长 宽
Heart = pygame.transform.smoothscale(Heart,(width//2,height//2))

Cloud = pygame.image.load("cloud.png").convert_alpha()
width,height = Cloud.get_size()
Cloud = pygame.transform.smoothscale(Cloud, (width//5,height//5))


while True:
    for event in pygame.event.get():  #事件遍历
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()



    screen.blit(BackGround,(0,0))
    screen.blit(Heart, (200, 300))
    screen.blit(Cloud, (200,600))


    pygame.display.update()