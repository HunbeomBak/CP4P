# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:22:18 2017

@author: Hunbeom Bak

참고 사이트 :http://www.petercollingridge.co.uk/pygame-physics-simulation/randomness
"""
import pygame
import random

'''
랜덤

random() - 0.0과 1.0 사이의 난수를 반환합니다.

uniform(a, b)- a 와 b 사이의 난수를 반환합니다.

randint(a, b)- a 와 b 사이의 임의의 정수를 반환합니다.

choice(list)- 목록 에서 임의의 요소를 반환 합니다.

shuffle(list) - 목록의 순서를 재정렬합니다

자세한 랜덤모듈에 관한 것은 https://docs.python.org/3/library/random.html 

'''

#기본 셋팅
background_color = (255,255,255) #흰색
(width, height) = (300, 200)    #300X200

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
pygame.display.set_caption('랜덤으로 원 그리기') # 창 제목 설정
screen.fill(background_color) #배경색 설정

#반경이 10~20 픽셀이고 임의의 위치에 원을 그리기

size = random.randint(10,20) #10과 20 사이의 난수를 반환
x= random.randint(size, width - size) # x의 위치는 size와 (화면 넓이)-(size) 사이에서 임의의 값: 원이 화면밖으로 나가는것을 방지
y= random.randint(size, height - size)#y도 x와 마찬가지 

my_random_particle= Particle((x,y),size)
my_random_particle.display()

pygame.display.flip() #창을 띄운다

#창을 닫을때 까지 계속 열려있음
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit ()