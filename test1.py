#coding: UTF-8 



'''向实现MyLibrary库  ，自己写一个简易游戏引擎'''

import sys
import pygame 
from pygame.locals import * 

#用来绘制文本图形的函数  
def print_text(font, x,y, text, color=(55,55,55)):
	imgText = font.render(text, True, color)
	screen = pygame.display.get_surface() 
	screen.blit(imgText, (x,y))  
	

text = "hello" 


pygame.init() 

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Test") 

font = pygame.font.Font(None,32)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.fill((255,255,255))
	print_text(font,20,20,text) 
	
	pygame.display.update() 

