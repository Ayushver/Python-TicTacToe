import pygame,sys,os,random
from time import *

os.environ['SDL_VIDEO_WINDOW_POS']='400,80'
  
pygame.init()
win=pygame.display.set_mode((600,600))
pygame.display.set_caption('TicTacToe')
win.fill((255,255,255))

class TicTacToe1:

    def __init__(self,m):
        self.m=m
        
    def button(self,action=None,action1=None):
        a=0
        click=0
        rect1=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
        pygame.draw.ellipse(win,(0,0,255),rect1,0)
        rect2=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
        pygame.draw.ellipse(win,(255,0,0),rect2,0)
        pygame.display.update()
        while(a>=0):
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        a=-1
                        pygame.quit()
                        sys.exit()
                pos=pygame.mouse.get_pos()
                

                if(pos[0]>=400 and pos[0]<=500):
                        if(pos[1]>=400 and pos[1]<=450):
                            rect3=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
                            pygame.draw.ellipse(win,(100,100,255),rect3,0)
                else:
                    rect4=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
                    pygame.draw.ellipse(win,(255,0,0),rect4,0)

                if(pos[0]>=100 and pos[0]<=200):
                        if(pos[1]>=400 and pos[1]<=450):
                            rect5=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
                            pygame.draw.ellipse(win,(100,100,255),rect5,0)
                else:
                    rect6=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
                    pygame.draw.ellipse(win,(0,0,255),rect6,0)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    click=1
                    if(pos[0]>=100 and pos[0]<=200):
                        if(pos[1]>=400 and pos[1]<=450):
                            if(click==1) and action=='play':
                                a=-1
                                m.clear()
                                for i in range(3):
                                    m.append(['1','1','1'])
                                a=0
                                while(a<50):
                                    pygame.time.delay(10)
                                    a+=1
                                    for event in pygame.event.get():
                                        if event.type==pygame.QUIT:
                                            a=301
                                            pygame.quit()
                                            sys.exit()
                                obj.Main()
                    elif(pos[0]>=400 and pos[0]<=500):
                        if(pos[1]>=400 and pos[1]<=450):
                            if(click==1) and action1=='quit':
                                a=-1
                                pygame.quit()
                                sys.exit()
                self.Font()
                pygame.display.update()

    def Font(self):
        text1=font1.render('Restart',1,(255,255,255))
        win.blit(text1, (107,410))
        text1=font1.render('Quit',1,(255,255,255))
        win.blit(text1, (423,410))


    
    def Draw(self):
        x=0
        y=0
        w=600
        for i in range(600):
            pygame.draw.line(win,(0,255,0),(x,0),(x,w),5)
            pygame.draw.line(win,(0,255,0),(0,y),(w,y),5)
            x+=200
            y+=200
            pygame.display.update()

    def Circle(self,i,j):
        pygame.draw.circle(win,(0,0,255),(100+200*j,100+200*i),80,4)
        pygame.display.update()

    def Cross(self,i,j):
        pygame.draw.line(win,(255,0,0),[30+200*j,30+200*i],[170+200*j,170+200*i],6)
        pygame.draw.line(win,(255,0,0),[30+200*j,170+200*i],[170+200*j,30+200*i],6)
        pygame.display.update()

    def Move(self):
        mov=0
        a=0
        while(a>=0):
            a+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        a=-1
                        pygame.quit()
                        sys.exit()
                        break
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() and mov==0:
                        pos=pygame.mouse.get_pos()
                        mov=1
                        b=self.check(pos[1]//200,pos[0]//200)
                        if(b):
                            m[pos[1]//200][pos[0]//200]='O'
                            self.Circle(pos[1]//200,pos[0]//200)
                        else:
                            self.Move()
                        
                        self.win()
                        a=-1
                    else:
                        continue

    def Move1(self):
        mov=0
        a=0
        while(a>=0):
            a+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        a=-1
                        pygame.quit()
                        sys.exit()
                        break
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() and mov==0:
                        pos=pygame.mouse.get_pos()
                        mov=1
                        b=self.check(pos[1]//200,pos[0]//200)
                        if(b):
                            m[pos[1]//200][pos[0]//200]='X'
                            self.Cross(pos[1]//200,pos[0]//200)
                        else:
                            self.Move1()
                        
                        self.win1()
                        a=-1
                    else:
                        continue

    def check(self,i,j):
        if((m[i][j]=='O')|(m[i][j]=='X')):
            return False
        else:
            return True
        
    def win(self):
        sleep(0.5)
        if(((m[0][0]=='O')&(m[0][1]=='O')&(m[0][2]=='O'))|((m[1][0]=='O')&(m[1][1]=='O')&(m[1][2]=='O'))|((m[2][0]=='O')&(m[2][1]=='O')&(m[2][2]=='O'))|((m[0][0]=='O')&(m[1][0]=='O')&(m[2][0]=='O'))|((m[0][1]=='O')&(m[1][1]=='O')&(m[2][1]=='O'))|((m[0][2]=='O')&(m[1][2]=='O')&(m[2][2]=='O'))|((m[0][0]=='O')&(m[1][1]=='O')&(m[2][2]=='O'))|((m[0][2]=='O')&(m[1][1]=='O')&(m[2][0]=='O'))):
            win.fill((255,255,255))   
            pygame.display.update()
            text1=font.render('Player 1 Won',1,(0,0,255))
            win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))))
            pygame.display.update()
            self.button('play','quit')
            
    def win1(self):
        sleep(0.5)
        if(((m[0][0]=='X')&(m[0][1]=='X')&(m[0][2]=='X'))|((m[1][0]=='X')&(m[1][1]=='X')&(m[1][2]=='X'))|((m[2][0]=='X')&(m[2][1]=='X')&(m[2][2]=='X'))|((m[0][0]=='X')&(m[1][0]=='X')&(m[2][0]=='X'))|((m[0][1]=='X')&(m[1][1]=='X')&(m[2][1]=='X'))|((m[0][2]=='X')&(m[1][2]=='X')&(m[2][2]=='X'))|((m[0][0]=='X')&(m[1][1]=='X')&(m[2][2]=='X'))|((m[0][2]=='X')&(m[1][1]=='X')&(m[2][0]=='X'))):
            win.fill((255,255,255))   
            pygame.display.update()
            text1=font.render('Player 2 Won',1,(0,0,255))
            win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))))
            pygame.display.update()
            self.button('play','quit')
                        

    def Equal(self):
        sleep(0.5)
        win.fill((255,255,255))   
        pygame.display.update()
        text1=font.render('Draw',1,(0,0,255))
        win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))))
        pygame.display.update()
        self.button('play','quit')

    def Main(self):
        win.fill((255,255,255))   
        pygame.display.update()
        text1=font.render('Player 1 click where you',1,(0,0,255))
        win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))-50))
        text1=font.render(' want your circle',1,(0,0,255))
        win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))+50))
        pygame.display.update()     
        a=0
        while(a<300):
            pygame.time.delay(10)
            a+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    a=301
                    pygame.quit()
                    sys.exit()
        win.fill((255,255,255))   
        pygame.display.update()
        
        self.Draw()
        self.Move()
        self.Move1()
        self.Move()
        self.Move1()
        self.Move()
        self.Move1()
        self.Move()
        self.Move1()
        self.Move()
        self.Equal()


class TicTacToe:

    def __init__(self,m):
        self.m=m
        
    def button(self,action=None,action1=None):
        a=0
        click=0
        rect1=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
        pygame.draw.ellipse(win,(0,0,255),rect1,0)
        rect2=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
        pygame.draw.ellipse(win,(255,0,0),rect2,0)
        pygame.display.update()
        while(a>=0):
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        a=-1
                        pygame.quit()
                        sys.exit()
                pos=pygame.mouse.get_pos()

                if(pos[0]>=400 and pos[0]<=500):
                        if(pos[1]>=400 and pos[1]<=450):
                            rect3=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
                            pygame.draw.ellipse(win,(100,100,255),rect3,0)
                else:
                    rect4=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
                    pygame.draw.ellipse(win,(255,0,0),rect4,0)

                if(pos[0]>=100 and pos[0]<=200):
                        if(pos[1]>=400 and pos[1]<=450):
                            rect5=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
                            pygame.draw.ellipse(win,(100,100,255),rect5,0)
                else:
                    rect6=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
                    pygame.draw.ellipse(win,(0,0,255),rect6,0)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    click=1
                    if(pos[0]>=100 and pos[0]<=200):
                        if(pos[1]>=400 and pos[1]<=450):
                            if(click==1) and action=='play':
                                a=-1
                                m.clear()
                                for i in range(3):
                                    m.append(['1','1','1'])
                                a=0
                                while(a<50):
                                    pygame.time.delay(10)
                                    a+=1
                                    for event in pygame.event.get():
                                        if event.type==pygame.QUIT:
                                            a=301
                                            pygame.quit()
                                            sys.exit()
                                ob.Main()
                    elif(pos[0]>=400 and pos[0]<=500):
                        if(pos[1]>=400 and pos[1]<=450):
                            if(click==1) and action1=='quit':
                                a=-1
                                pygame.quit()
                                sys.exit()
                self.Font()
                pygame.display.update()

    def Font(self):
        text1=font1.render('Restart',1,(255,255,255))
        win.blit(text1, (107,410))
        text1=font1.render('Quit',1,(255,255,255))
        win.blit(text1, (423,410))

    def Level(self,action=None,action1=None):
        a=0
        s.clear()
        click=0
        rect1=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
        pygame.draw.ellipse(win,(0,0,255),rect1,0)
        rect2=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
        pygame.draw.ellipse(win,(255,0,0),rect2,0)
        pygame.display.update()
        while(a>=0):
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        a=-1
                        pygame.quit()
                        sys.exit()
                pos=pygame.mouse.get_pos()

                if(pos[0]>=400 and pos[0]<=500):
                        if(pos[1]>=400 and pos[1]<=450):
                            rect3=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
                            pygame.draw.ellipse(win,(100,100,255),rect3,0)
                else:
                    rect4=pygame.draw.rect(win,(255,255,255),(400,400,100,50))
                    pygame.draw.ellipse(win,(255,0,0),rect4,0)

                if(pos[0]>=100 and pos[0]<=200):
                        if(pos[1]>=400 and pos[1]<=450):
                            rect5=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
                            pygame.draw.ellipse(win,(100,100,255),rect5,0)
                else:
                    rect6=pygame.draw.rect(win,(255,255,255),(100,400,100,50))
                    pygame.draw.ellipse(win,(0,0,255),rect6,0)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    click=1
                    if(pos[0]>=100 and pos[0]<=200):
                        if(pos[1]>=400 and pos[1]<=450):
                            if(click==1) and action=='easy':
                                a=-1
                                s.append('easy')
                                
                    elif(pos[0]>=400 and pos[0]<=500):
                        if(pos[1]>=400 and pos[1]<=450):
                            if(click==1) and action1=='hard':
                                a=-1
                                s.append('hard')
                self.Font1()
                pygame.display.update()

    def Font1(self):
        text1=font1.render('Easy',1,(255,255,255))
        win.blit(text1, (120,410))
        text1=font1.render('Hard',1,(255,255,255))
        win.blit(text1, (423,410))

    
    def Draw(self):
        x=0
        y=0
        w=600
        for i in range(600):
            pygame.draw.line(win,(0,255,0),(x,0),(x,w),5)
            pygame.draw.line(win,(0,255,0),(0,y),(w,y),5)
            x+=200
            y+=200
            pygame.display.update()

    def Circle(self,i,j):
        pygame.draw.circle(win,(0,0,255),(100+200*j,100+200*i),80,4)
        pygame.display.update()

    def Cross(self,i,j):
        pygame.draw.line(win,(255,0,0),[30+200*j,30+200*i],[170+200*j,170+200*i],6)
        pygame.draw.line(win,(255,0,0),[30+200*j,170+200*i],[170+200*j,30+200*i],6)
        pygame.display.update()

    def Move(self):
        mov=0
        a=0
        while(a>=0):
            a+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        a=-1
                        pygame.quit()
                        sys.exit()
                        break
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() and mov==0:
                        pos=pygame.mouse.get_pos()
                        
                        mov=1
                        b=self.check(pos[1]//200,pos[0]//200)
                        if(b):
                            m[pos[1]//200][pos[0]//200]='O'
                            self.Circle(pos[1]//200,pos[0]//200)
                        else:
                            self.Move()
                        
                        self.win()
                        a=-1
                    else:
                        continue
                    

    def check(self,i,j):
        if((m[i][j]=='O')|(m[i][j]=='X')):
            return False
        else:
            return True
        
    def win(self):
        sleep(0.5)
        if(((m[0][0]=='O')&(m[0][1]=='O')&(m[0][2]=='O'))|((m[1][0]=='O')&(m[1][1]=='O')&(m[1][2]=='O'))|((m[2][0]=='O')&(m[2][1]=='O')&(m[2][2]=='O'))|((m[0][0]=='O')&(m[1][0]=='O')&(m[2][0]=='O'))|((m[0][1]=='O')&(m[1][1]=='O')&(m[2][1]=='O'))|((m[0][2]=='O')&(m[1][2]=='O')&(m[2][2]=='O'))|((m[0][0]=='O')&(m[1][1]=='O')&(m[2][2]=='O'))|((m[0][2]=='O')&(m[1][1]=='O')&(m[2][0]=='O'))):
            win.fill((255,255,255))   
            pygame.display.update()
            text1=font.render('You Won',1,(0,0,255))
            win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))))
            pygame.display.update()
            self.button('play','quit')
            
    def loss(self):
        sleep(0.5)
        if(((m[0][0]=='X')&(m[0][1]=='X')&(m[0][2]=='X'))|((m[1][0]=='X')&(m[1][1]=='X')&(m[1][2]=='X'))|((m[2][0]=='X')&(m[2][1]=='X')&(m[2][2]=='X'))|((m[0][0]=='X')&(m[1][0]=='X')&(m[2][0]=='X'))|((m[0][1]=='X')&(m[1][1]=='X')&(m[2][1]=='X'))|((m[0][2]=='X')&(m[1][2]=='X')&(m[2][2]=='X'))|((m[0][0]=='X')&(m[1][1]=='X')&(m[2][2]=='X'))|((m[0][2]=='X')&(m[1][1]=='X')&(m[2][0]=='X'))):
            win.fill((255,255,255))   
            pygame.display.update()
            text1=font.render('You Lost',1,(0,0,255))
            win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))))
            pygame.display.update()
            self.button('play','quit')
                        
    def compMove(self):
        sleep(1)
        if((m[0][0]=='X')&(m[0][1]=='X')&(m[0][2]=='1')) or ((m[0][2]=='1')&(m[1][2]=='X')&(m[2][2]=='X')) or ((m[0][2]=='1')&(m[1][1]=='X')&(m[2][0]=='X')):
           m[0][2]='X'
           i=0
           j=2
        elif((m[0][0]=='X')&(m[0][1]=='1')&(m[0][2]=='X')) or ((m[0][1]=='1')&(m[1][1]=='X')&(m[2][1]=='X')):
           m[0][1]='X'
           i=0
           j=1
        elif((m[0][0]=='1')&(m[0][1]=='X')&(m[0][2]=='X')) or ((m[0][0]=='1')&(m[1][0]=='X')&(m[2][0]=='X')) or ((m[0][0]=='1')&(m[1][1]=='X')&(m[2][2]=='X')):
           m[0][0]='X'
           i=0
           j=0
        elif((m[1][0]=='X')&(m[1][1]=='X')&(m[1][2]=='1')) or ((m[0][2]=='X')&(m[1][2]=='1')&(m[2][2]=='X')):
           m[1][2]='X'
           i=1
           j=2
        elif((m[1][0]=='X')&(m[1][1]=='1')&(m[1][2]=='X')) or ((m[0][1]=='X')&(m[1][1]=='1')&(m[2][1]=='X')) or ((m[0][2]=='X')&(m[1][1]=='1')&(m[2][0]=='X')) or ((m[0][0]=='X')&(m[1][1]=='1')&(m[2][2]=='X')):
           m[1][1]='X'
           i=1
           j=1
        elif((m[1][0]=='1')&(m[1][1]=='X')&(m[1][2]=='X')) or ((m[0][0]=='X')&(m[1][0]=='1')&(m[2][0]=='X')):
           m[1][0]='X'
           i=1
           j=0
        elif((m[2][0]=='X')&(m[2][1]=='X')&(m[2][2]=='1')) or ((m[0][2]=='X')&(m[1][2]=='X')&(m[2][2]=='1')) or ((m[0][0]=='X')&(m[1][1]=='X')&(m[2][2]=='1')):
           m[2][2]='X'
           i=2
           j=2
        elif((m[2][0]=='X')&(m[2][1]=='1')&(m[2][2]=='X')) or ((m[0][1]=='X')&(m[1][1]=='X')&(m[2][1]=='1')):
           m[2][1]='X'
           i=2
           j=1
        elif((m[2][0]=='1')&(m[2][1]=='X')&(m[2][2]=='X')) or ((m[0][0]=='X')&(m[1][0]=='X')&(m[2][0]=='1')) or ((m[0][2]=='X')&(m[1][1]=='X')&(m[2][0]=='1')):
           m[2][0]='X'
           i=2
           j=0
   
        elif((m[0][0]=='O')&(m[0][1]=='O')&(m[0][2]=='1')) or ((m[0][2]=='1')&(m[1][2]=='O')&(m[2][2]=='O')) or ((m[0][2]=='1')&(m[1][1]=='O')&(m[2][0]=='O')):
           m[0][2]='X'
           i=0
           j=2
        elif((m[0][0]=='O')&(m[0][1]=='1')&(m[0][2]=='O')) or ((m[0][1]=='1')&(m[1][1]=='O')&(m[2][1]=='O')):
           m[0][1]='X'
           i=0
           j=1
        elif((m[0][0]=='1')&(m[0][1]=='O')&(m[0][2]=='O')) or ((m[0][0]=='1')&(m[1][0]=='O')&(m[2][0]=='O')) or ((m[0][0]=='1')&(m[1][1]=='O')&(m[2][2]=='O')):
           m[0][0]='X'
           i=0
           j=0
        elif((m[1][0]=='O')&(m[1][1]=='O')&(m[1][2]=='1')) or ((m[0][2]=='O')&(m[1][2]=='1')&(m[2][2]=='O')):
           m[1][2]='X'
           i=1
           j=2
        elif((m[1][0]=='O')&(m[1][1]=='1')&(m[1][2]=='O')) or ((m[0][1]=='O')&(m[1][1]=='1')&(m[2][1]=='O')) or ((m[0][2]=='O')&(m[1][1]=='1')&(m[2][0]=='O')) or ((m[0][0]=='O')&(m[1][1]=='1')&(m[2][2]=='O')):
           m[1][1]='X'
           i=1
           j=1
        elif((m[1][0]=='1')&(m[1][1]=='O')&(m[1][2]=='O')) or ((m[0][0]=='O')&(m[1][0]=='1')&(m[2][0]=='O')):
           m[1][0]='X'
           i=1
           j=0
        elif((m[2][0]=='O')&(m[2][1]=='O')&(m[2][2]=='1')) or ((m[0][2]=='O')&(m[1][2]=='O')&(m[2][2]=='1')) or ((m[0][0]=='O')&(m[1][1]=='O')&(m[2][2]=='1')):
           m[2][2]='X'
           i=2
           j=2
        elif((m[2][0]=='O')&(m[2][1]=='1')&(m[2][2]=='O')) or ((m[0][1]=='O')&(m[1][1]=='O')&(m[2][1]=='1')):
           m[2][1]='X'
           i=2
           j=1
        elif((m[2][0]=='1')&(m[2][1]=='O')&(m[2][2]=='O')) or ((m[0][0]=='O')&(m[1][0]=='O')&(m[2][0]=='1')) or ((m[0][2]=='O')&(m[1][1]=='O')&(m[2][0]=='1')):
           m[2][0]='X'
           i=2
           j=0
            
        else:
            if(m[1][1]=='1'):
                m[1][1]='X'
                i=1
                j=1
            elif(m[1][1]=='O') and (m[0][0]=='1') and s[0]=='hard':
                m[0][0]='X'
                i=0
                j=0
            elif(m[1][1]=='O') and (m[2][2]=='1') and s[0]=='hard':
                m[2][2]='X'
                i=2
                j=2
            elif(m[1][1]=='O') and (m[2][0]=='1') and s[0]=='hard':
                m[2][0]='X'
                i=2
                j=0
            elif(m[1][1]=='O') and (m[0][2]=='1') and s[0]=='hard':
                m[0][2]='X'
                i=0
                j=2
            else:
                for x in range(10):
                    a=random.randint(0,2)
                    b=random.randint(0,2)
                    
                    if(m[a][b]=='1'):
                        m[a][b]='X'
                        i=a
                        j=b
                        break
                    else:
                        continue 
        self.Cross(i,j) 
        self.loss()

    def Equal(self):
        sleep(0.5)
        win.fill((255,255,255))   
        pygame.display.update()
        text1=font.render('Draw',1,(0,0,255))
        win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))))
        pygame.display.update()
        self.button('play','quit')

    def Main(self):
        win.fill((255,255,255))   
        pygame.display.update()
        text1=font.render('Choose Difficulty',1,(0,0,255))
        win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))-25))
        self.Level('easy','hard')
        pygame.display.update()
        a=0
        while(a<100):
            pygame.time.delay(10)
            a+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    a=301
                    pygame.quit()
                    sys.exit()

        win.fill((255,255,255))   
        pygame.display.update()
        self.Draw()
        self.Move()
        self.compMove()
        self.Move()
        self.compMove()
        self.Move()
        self.compMove()
        self.Move()
        self.compMove()
        self.Move()
        self.Equal()

def opt(action=None,action1=None):
    a=0
    d.clear()
    click=0
    rect1=pygame.draw.rect(win,(255,255,255),(100,400,150,75))
    pygame.draw.ellipse(win,(0,0,255),rect1,0)
    rect2=pygame.draw.rect(win,(255,255,255),(400,400,150,75))
    pygame.draw.ellipse(win,(0,0,255),rect2,0)
    pygame.display.update()
    while(a>=0):
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    a=-1
                    pygame.quit()
                    sys.exit()
            pos=pygame.mouse.get_pos()

            if(pos[0]>=400 and pos[0]<=500):
                    if(pos[1]>=400 and pos[1]<=450):
                        rect3=pygame.draw.rect(win,(255,255,255),(400,400,150,75))
                        pygame.draw.ellipse(win,(100,100,255),rect3,0)
            else:
                rect4=pygame.draw.rect(win,(255,255,255),(400,400,150,75))
                pygame.draw.ellipse(win,(0,0,255),rect4,0)

            if(pos[0]>=100 and pos[0]<=200):
                    if(pos[1]>=400 and pos[1]<=450):
                        rect5=pygame.draw.rect(win,(255,255,255),(100,400,150,75))
                        pygame.draw.ellipse(win,(100,100,255),rect5,0)
            else:
                rect6=pygame.draw.rect(win,(255,255,255),(100,400,150,75))
                pygame.draw.ellipse(win,(0,0,255),rect6,0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                click=1
                if(pos[0]>=100 and pos[0]<=200):
                    if(pos[1]>=400 and pos[1]<=450):
                        if(click==1) and action=='Play':
                            a=-1
                            d.append('Play')
                            
                elif(pos[0]>=400 and pos[0]<=500):
                    if(pos[1]>=400 and pos[1]<=450):
                        if(click==1) and action1=='Comp':
                            a=-1
                            d.append('Comp')
            Font2()
            pygame.display.update()

def Font2():
    text1=font1.render('Vs Player',1,(255,255,255))
    win.blit(text1, (125,420))
    text1=font1.render('Vs Comp',1,(255,255,255))
    win.blit(text1, (425,420))

font=pygame.font.SysFont('cambria', 50)
font1=pygame.font.SysFont('cambria', 25)
m=[['1','1','1'],['1','1','1'],['1','1','1']]  
s=[]
d=[]
ob=TicTacToe(m)
obj=TicTacToe1(m)
win.fill((255,255,255))   
pygame.display.update()
text1=font.render('Choose Option',1,(0,0,255))
win.blit(text1, (300 - (text1.get_width()//2),(300 - (text1.get_height()//2))-25))
opt('Play','Comp')
pygame.display.update()
a=0
while(a<100):
    pygame.time.delay(10)
    a+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=301
            pygame.quit()
            sys.exit()
if(d[0]=='Comp'):
    ob.Main()
else:
    obj.Main()
#MAIN LOOP
a=True
while(a):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            a=False
pygame.quit()
sys.exit()

