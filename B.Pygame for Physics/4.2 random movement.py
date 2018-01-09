# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:01:47 2017

@author: Hunbeom Bak

참고 사이트 : http://www.petercollingridge.co.uk/pygame-physics-simulation/movement
"""


import pygame
import random
import math

#기본 셋팅
background_color = (255,255,255) #흰색
(width, height) = (600, 480)    #300X200

class Particle:
    def __init__(self, position, size): #position = (x,y), size:반지름
        self.x = position[0] 
        self.y = position[1]
        self.size = size
        self.color = (0, 0,0)
        self.thickness = 1
        self.speed =0 #속도
        self.angle=0 #각도

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
    
    def move(self):
        self.x += math.sin(self.angle) * self.speed 
        self.y -= math.cos(self.angle) * self.speed


screen = pygame.display.set_mode((width, height)) #창 크기 설정
pygame.display.set_caption('4.무작위 운동') # 창 제목 설정
screen.fill(background_color) #배경색 설정

#반경이 10~20 픽셀인 여러개의 입자를 임의의 위치에 그리기
number_of_particles = 100 #입자의 갯수
my_particles = [] #입자에 대한 정보를 집어 넣음

#입자에 대한 정보를  n번 생성

for n in range(number_of_particles):
    size = random.randint(1,20) #사이즈를 괄호에 있는 숫자 사이 값을 반환
    x= random.randint(size, width - size) # x의 위치는 size와 (화면 넓이)-(size) 사이에서 임의의 값: 원이 화면밖으로 나가는것을 방지
    y= random.randint(size, height - size)#y도 x와 마찬가지 
    
    particle =Particle((x,y),size) #위에서 랜덤으로 뽑은 값을 Particle에 넣음
    particle.speed = random.random() 
    particle.angle =random.uniform(0,math.pi*2)
    my_particles.append(particle) # 랜덤으로 나온 값을 my_particles에 집어 넣음


#창을 닫을때 까지 계속 열려있음

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit ()
    screen.fill(background_color) #배경색 설정 및 입자 움직이면 잔상이 남으므로 while문 안에 넣어서 잔상을 없애버림       
            
        #창을 닫을때 까지 입자들이 움직임 따라서 while루프 안으로 이동 
    for particle in my_particles: #my_particles = [] 안에 있는 각각 정보마다 반복
        particle.move()
        particle.display() #그려라
    pygame.display.flip()#창을 띄운다