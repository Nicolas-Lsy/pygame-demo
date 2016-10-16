
#coding: UTF-8 




#Ball-Game V1.0
import pygame
from pygame.locals import *
import sys,time,random

#输出文本图形在屏幕转换
def print_text(font,x,y,text,color = (255,255,255)):
	imgText = font.render(text,True,color) #字体转为图形
	screen.blit(imgText,(x,y))  #屏幕位置绘制
#OK********************************************************
#初始指标
pygame.init()

screen = pygame.display.set_mode((650,1000))
font1 = pygame.font.Font(None, 30)
white = 255,255,255
blue = 0,0,255 
pink = 255,0,255 
yellow = 255,255,0
black = 0,0,0
game_over = True 
lives = 5
score = 0 
pygame.mouse.set_visible(False)
#OK********************************************************
#位置变量
ball_x = random.randint(0,1000)
ball_y = -50
ball_vy = 0.7
mouse_x = mouse_y = 0 

block_x,block_y =400,700

v_x,v_y=1,2
pos = (block_x,block_y,200,40)  #前面是位置 后面是长宽
radius = 30
width = 0

#位图准备
#背景
BackGround = pygame.image.load("background.png").convert()

#球
Ball = pygame.image.load("heart.png").convert_alpha()
Ball_width,Ball_height = Ball.get_size()
Ball = pygame.transform.smoothscale(Ball,(Ball_width//2,Ball_height//2))
#板子
Bang = pygame.image.load("cloud.png").convert_alpha()
Bang_width,Bang_height = Bang.get_size()
Bang = pygame.transform.smoothscale(Bang,(Bang_width//3,Bang_height//3))



while True :
#事件的响应处理
	for event in pygame.event.get():
		if event.type == QUIT:  #事件的状态
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouse_x,mouse_y = event.pos 
			move_x,move_y = event.rel 
		elif event.type == MOUSEBUTTONUP:
			if game_over:
				game_over = False 
				lives = 5 
				score = 0 
			
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()
	screen.blit(BackGround,(0,0))
#OK********************************************************
#游戏过程
#绘制 动态 
	if game_over:
		print_text(font1,400,400,"<Click To Play>",black)
	else:
		

	#小球落下
		ball_y += ball_vy 
		if ball_y > 800:
			ball_x = random.randint(0,500)
			ball_y = -50 
			lives -= 1 
			if lives == 0:
				game_over = True 
		elif ball_y > block_y:
			#保证在板子范围内，即接住
			if ball_x > block_x and ball_x < block_x+200:
				score += 10 
				ball_x = random.randint(0,1000)
				ball_y = -50 
		#画圆
		screen.blit(Ball,(ball_x-50,ball_y))
		#pygame.draw.circle(screen,pink,(ball_x,int(ball_y)),radius,width)

		#动态 木板移动		
		block_x = mouse_x 
		if block_x < 0:
			block_x = 0
		elif block_x > 1000:
			block_x = 1000 
		#画矩形
		screen.blit(Bang,(block_x,block_y))
		#pygame.draw.rect(screen,yellow,(block_x,block_y,200,40),width)
#OK********************************************************
		
#碰撞...

#提示
	print_text(font1,0,0,"Lives: "+ str(lives),white)
	print_text(font1,0,40,"Score: " + str(score),black)
	print_text(font1,400,0,"BaLL--Game",white)
#主题
	pygame.display.set_caption("Ball Game")
	pygame.display.update()
	