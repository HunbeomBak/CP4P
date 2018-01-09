# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:05:41 2017

@author: Hunbeom Bak

참고 사이트 :http://www.petercollingridge.co.uk/pygame-physics-simulation/drawing-circles
"""

import pygame

'''
원 그리기
pygame.draw.circle(screen, 색 RGB값, 위치, 반지름, 두께)
pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)

'''



background_color = (255,255,255) #흰색
(width, height) = (300, 200)    #300X200

class Particle:
    def __init__(self, positon, size): #position = (x,y), size:반지름
        self.x = positon[0] 
        self.y = positon[1]
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

screen = pygame.display.set_mode((width, height)) #창 크기 설정
pygame.display.set_caption('원 그리기') # 창 제목 설정
screen.fill(background_color) #배경색 설정

my_first_particle = Particle((150, 50), 15) #x:150, y:50, 반지름:15
my_first_particle.display()  #위 클래스의 display를 사용한다; 위에서 언급한 위치와 반지름의 원을 그린다.

pygame.display.flip() #창을 띄운다

#창을 닫을때 까지 계속 열려있음
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit ()