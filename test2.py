#coding: UTF-8 
import pygame,sys,time,random,math
from pygame.locals import * 
from test1 import *  



def game_init():
	global backbuffer,screen,font

	pygame.init() 
	screen = pygame.display.set_mode((24*32,18*32))
	pygame.display.set_caption("Snake Game!")
	font = pygame.font.Font(None, 30)
	timer = pygame.time.Clock() 

	#draw surface
	backbuffer = pygame.Surface((screen.get_rect().width,screen.get_rect().height))

	#create snake 


	#create food 


#main program begins 
game_init() 
game_over = False 
last_time = 0 

auto_play = False   #you can add
step_time = 400    

#main loop 
while True :
	
	ticks = pygame.time.get_ticks() 

	#event 
	for event in pygame.event.get():
		if event.type == QUIT: 
			sys.exit() 
	keys = pygame.key.get_pressed() 
	if keys[K_ESCAPE]:
		sys.exit() 
	elif keys[K_UP] or keys[K_w]:
		pass 



	backbuffer.fill((10,50,10))

	screen.blit(backbuffer,(0,0))

	if not game_over:
		print_text(font,0,0,"Level :",color=(255,0,0))
		print_text(font,0,20,"Position :",color=(255,0,0))
	else:
		print_text(font, 0,0, "Game OVER")

	pygame.display.update() 



























