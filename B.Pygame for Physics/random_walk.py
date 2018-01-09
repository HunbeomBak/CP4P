# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:12:41 2017

@author: Hunbeom Bak

건우형이 올린 예제 수정함
"""

import pygame
import random


class Main :
    
    def __init__(self) :
        
        self.BLACK = (0, 0, 0)                  # 검은색 
        self.WHITE = (255, 255, 255)            # 흰색
        self.RED   = (255, 0, 0)                # 붉은색
        
        self.screen_width   = 640               # 화면 가로 길이
        self.screen_height  = 400               # 화면 세로 길이
        
        self.done = False                       # 게임 플레이 변수 
        
        # 파이게임 화면 설정
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
          
    def initializeGame(self) :
        
        r=320 # 초기위치=중심
        
        # 종료 이벤트가 발생할 때까지 업데이트 !
        while not self.done:
             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()           
            self.screen.fill(self.WHITE)        # 배경은 흰색
            
            a=random.choice([0,1]) #0과 1중 하나 선택=확률 1/2
           
            if a==1:
                r=r+1 #앞으로 한칸
            else :
                r=r-1 #뒤로 한칸
                
            
            self.drawCircle(r)                    # 원 그리기
            
            self.drawLine()                       #선 그리기
            
            
            
            pygame.display.flip()               # 화면 업데이트
            
    def drawCircle(self,r) :
         pygame.draw.circle(self.screen,self.RED,(r,200),5,1)
         
    def drawLine(self):
         pygame.draw.line(self.screen,self.BLACK,(0,200),(640,200),1)
       
pygame.init()                                   # 파이게임 모듈 초기화
game = Main()                                   # Main 인스턴스 생성 
game.initializeGame()                           # 게임화면 실행 ! 