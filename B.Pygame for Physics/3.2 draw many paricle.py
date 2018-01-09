# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:45:56 2017

@author: Hunbeom Bak

참고 사이트:http://www.petercollingridge.co.uk/pygame-physics-simulation/randomness
"""

import pygame
import random


#기본 셋팅
background_color = (255,255,255) #흰색
(width, height) = (600, 480)    #300X200

class Particle:
    def __init__(self, positon, size): #position = (x,y), size:반지름
        self.x = positon[0] 
        self.y = positon[1]
        self.size = size
        self.color = (0, 0,0)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

screen = pygame.display.set_mode((width, height)) #창 크기 설정
pygame.display.set_caption('입자 여러개 그리기') # 창 제목 설정
screen.fill(background_color) #배경색 설정

#반경이 10~20 픽셀인 여러개의 입자를 임의의 위치에 그리기

number_of_particles = 10 #입자의 갯수
my_particles = [] #입자에 대한 정보를 집어 넣음

#입자에 대한 정보를  n번 생성

for n in range(number_of_particles):
    size = random.randint(1,20) #사이즈를 괄호에 있는 숫자 사이 값을 반환
    x= random.randint(size, width - size) # x의 위치는 size와 (화면 넓이)-(size) 사이에서 임의의 값: 원이 화면밖으로 나가는것을 방지
    y= random.randint(size, height - size)#y도 x와 마찬가지 
    my_particles.append(Particle((x, y), size)) # 랜덤으로 나온 값을 my_particles에 집어 넣음

for particle in my_particles: #my_particles = [] 안에 있는 각각 정보마다 반복
    particle.display() #그려라
    


pygame.display.flip() #창을 띄운다

#창을 닫을때 까지 계속 열려있음
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit ()
            