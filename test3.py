#coding: UTF-8 
'''
Snake Game 
'''


import pygame,sys,time,random,math
from pygame.locals import * 
from MyLibrary import *  

#creat food class 
class Food(MySprite):
	def __init__(self):
		MySprite.__init__(self)
		image = pygame.Surface((32,32)).convert_alpha()
		image.fill((255,255,255,0))
		pygame.draw.circle(image,(250,250,50),(16,16),16,0)
		self.set_image(image)
		MySprite.update(self,0,30)
		self.X = random.randint(0,23)
		self.Y = random.randint(0,17)

#creat snake segment class 
class SnakeSegment(MySprite):
	def __init__(self,color=(20,200,20)):
		MySprite.__init__(self)
		image = pygame.Surface((32,32)).convert_alpha()
		image.fill((255,255,255,0))
		pygame.draw.circle(image, color, (16,16), 16, 0)
		self.set_image(image)
		MySprite.update(self, 0, 30) #create frame image






def game_init():
	global backbuffer,screen,font,food_group,timer,snake 

	pygame.init() 
	screen = pygame.display.set_mode((24*32,18*32))
	pygame.display.set_caption("Snake Game!")
	font = pygame.font.Font(None, 30)
	timer = pygame.time.Clock() 

	#draw surface
	backbuffer = pygame.Surface((screen.get_rect().width,screen.get_rect().height))

	#create snake 


	#create food 
	food_group = pygame.sprite.Group() 
	food = Food() 
	food_group.add(food) 

#main program begins 
game_init() 
game_over = False 
last_time = 0 

auto_paly = False 
step_time = 400 

#main loop 
while True :
	timer.tick(30)
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
	food_group.draw(backbuffer)
	screen.blit(backbuffer,(0,0))

	if not game_over:
		print_text(font,0,0,"Level :",color=(255,0,0))
		print_text(font,0,20,"Position :",color=(255,0,0))
	else:
		print_text(font, 0,0, "Game OVER")

	pygame.display.update() 



























