# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:22:14 2017

@author: Hunbeom Bak

참고 사이트 : http://www.petercollingridge.co.uk/pygame-physics-simulation/creating-pygame-window
"""

import pygame

background_colour =(255,255,255) #배경색
(width, height) = (300,200)      #창크기 

screen = pygame.display.set_mode((width,height)) #띄울 창크기를 설정
pygame.display.set_caption('튜토리얼1') #창의 제목 설정
screen.fill(background_colour)           #배경색

pygame.display.flip() # 창띄우기

#창이 나타났다가 사라짐, 계속 볼려면 루프로 계속 볼 수 있게 해야함
#창 닫기: 파이게임의 pygame.event.get() 함수를 이용해 종료하면 창이 꺼지도록 설정

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit ()
            