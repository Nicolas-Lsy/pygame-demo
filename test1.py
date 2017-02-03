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


#精灵类实现 
'''
获得一张多帧的图形，按照序列切换帧，循环往复实现动态精灵
是对原有pygame的sprite扩展，增加自己需要的功能
'''
class MySprite(pygame.sprite.Sprite):
	def __init__(self): 
		pygame.sprite.Sprite.__init__(self) 
		self.master_image = None  #主图
		self.frame = 0       #帧
		
		pass 
	#为了操作方便，讲函数变为属性，赋予X	
	def _getx(self): return self.rect.x 
	def _setx(self,value):self.rect.x = value 
	X = property(_getx,_setx) 
	
	
	#为了操作方便，讲函数变为属性，赋予Y	
	def _gety(self): return self.rect.y
	def _sety(self,value): self.rect.y = value 
	Y = property(_gety, _sety)  
	
	#为了操作方便，讲函数变为属性，赋予position
	def _getpos(self): return self.rect.topleft
	def _setpos(self,pos): self.rect.topleft = pos
	position = property(_getpos,_setpos)
	
	#图片加载功能,参数只需要知道“列”就好
	def load(self, filename, width=0,height=0,columns=1):
		self.master_image = pygame.image.load(filename).convert_alpha() 
		self.set_image(self.master_image, width, height,columns) 
		
	def set_image(self, image, width = 0, height=0, colums = 1):
		self.master_image = image 
		if width == 0 and height == 0: 
			self.frame_width = image.get_width() 
			self.frame_height = image.get_height() 
		else:
		#得到每一帧 长和宽  以及  主图的 大小 （长宽）
			self.frame_width = width
			self.frame_height = height
			rect = self.master_image.get_rect()
        #通过计算，求得 几行 几列 共有几帧
			self.last_frame = (rect.width//width) * (rect.height//height) - 1  #因为从0开始，所以减去1
			self.rect = Rect(0,0,self.frame_width,self.frame_height)#每一帧所占矩形 大学
			self.colums = columns #列数 

	def update(self, current_time, rate=30):
		if self.last_frame > self.first_frame:
            #update animation frame number
			if current_time > self.last_time + rate:
				self.frame += 1
				if self.frame > self.last_frame:
					self.frame = self.first_frame
				self.last_time = current_time
		else:
			self.frame = self.first_frame

        #build current frame only if it changed
		if self.frame != self.old_frame:
			frame_x = (self.frame % self.columns) * self.frame_width
			frame_y = (self.frame // self.columns) * self.frame_height
			rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
			self.image = self.master_image.subsurface(rect)
			self.old_frame = self.frame

	def __str__(self):
		return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)			
	
			
#点 类 
class Point(object):
	def __init__(self, x, y):
		self.__x = x 
		self.__y = y 
		
	#为x赋予属性 ， 能删除能设置 
	def getx(self): return self.__x 
	def setx(self,x): self.__x = x 
	x = property(getx, setx) 
	
	#Y property
	def gety(self): return self.__y
	def sety(self, y): self.__y = y
	y = property(gety, sety)
	
	def __str__(self):
		return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"

'''
__str__的作用理解： http://blog.csdn.net/lwnylslwnyls/article/details/10375677
'''










































	

