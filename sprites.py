import pygame as pg
import os
from data_manip import DataManipulator
from settings import WIN_HEIGHT,WIN_WIDTH,TEXT_D,TODAY
from text_img_creator import TextIMGCreator
from pretty_graph import prettyPie

class Load_Screen():
    
    def __init__(self, surf, x,y):

        self.CWD = os.getcwd()
        self.IMG_FLDR = os.path.join(self.CWD,'img')
        self.KP = os.path.join(self.IMG_FLDR,'kp.png')

        #pg stuff
        self.SURF = surf
        self.FRAME_RATE = 60
        self.LAST_UPDATE = pg.time.get_ticks()
        self.FRAME = 0 

        self.VEL_X = 10
        self.VEL_Y = 10

        #text / img manipulation  - tuple in form (item, rect)
        self.TXT_IMG_MANIP = TextIMGCreator()

        self.K = self.TXT_IMG_MANIP.createTextSprite('K','comicsansmc',200,
        (87, 222, 123),x,y)

        self.P = self.TXT_IMG_MANIP.createTextSprite('P','comicsansmc',500,
        (190, 26, 219),x,y)
        
        self.KP = self.TXT_IMG_MANIP.createIMGSprite(self.KP,x,y-WIN_HEIGHT//2)

        self.STOP = False

    def draw(self,img,rect):
        self.SURF.blit(img,rect)

    def update(self):
        START = 7
        SND_BOUND = 10
        now = pg.time.get_ticks()
        if now - self.LAST_UPDATE > self.FRAME_RATE:
            self.LAST_UPDATE = now
            self.FRAME += 1
        #draw img
        if START < self.FRAME < SND_BOUND:
            self.draw(self.K[0],self.K[1])
            self.K[1].centery -=self.VEL_X
            self.K[1].centerx -=self.VEL_Y

        elif SND_BOUND < self.FRAME < 15:
            self.draw(self.P[0],self.P[1])
            self.P[1].centery += self.VEL_X
            self.P[1].centerx += self.VEL_Y
        
        elif self.FRAME > 15:
            self.draw(self.KP[0],self.KP[1])
            self.KP[1].centery += self.VEL_Y

                

class MainSprite():
    
    def __init__(self,surf, x,y):
        self.CWD = os.getcwd()
        self.GRAPH_FLDR = os.path.join(self.CWD,'graphs')
        
        self.SURF = surf
        self.FRAME_RATE = 60
        self.X = x
        self.Y = y

        
        #data manip / data
        self.DATA = DataManipulator()
        self.DATA.initialize()

        #text / img manipulation 
        self.TXT_IMG_MANIP = TextIMGCreator()

        #create an image of each graph, note prettyPie returns the path to png file
        self.DAY_FREQ_PIE_FILE = prettyPie(x=self.DATA.DAY_FREQ_SERIES.index,
        y=self.DATA.DAY_FREQ_SERIES.values,rad=1.0,name='day_freq_pie').plot()

        self.DRINK_FREQ_PIE_FILE = prettyPie(x=self.DATA.DRINK_FREQ_SERIES.index,
        y=self.DATA.DRINK_FREQ_SERIES.values,rad=1.5,name='drink_freq_plot').plot()

        self.DAY_FREQ_PIE = self.TXT_IMG_MANIP.createIMGSprite(self.DAY_FREQ_PIE_FILE,
        x=WIN_WIDTH//2,y=WIN_HEIGHT*0.75)

        self.DRINK_FREQ_PIE = self.TXT_IMG_MANIP.createIMGSprite(self.DRINK_FREQ_PIE_FILE,
        x=WIN_WIDTH//2,y=WIN_HEIGHT*0.5)

        #text
        self.INTRO_TEXT = TEXT_D['intro_text']
        self.INTRO_TEXT_Y = self.Y

        self.DAY_FREQ_TEXT = TEXT_D['day_freq_text']
        self.DRINK_FREQ_TEXT = TEXT_D['drink_freq_text']
        
        #tuple of text, text_rect
        self.BEGINNING_TEXT =self.TXT_IMG_MANIP.createTextSprite(
            TEXT_D['beginning_text'],'comicsansmc',150,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        self.TRANS_01 = self.TXT_IMG_MANIP.createTextSprite(
        TEXT_D['transistion_1'],'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        self.TRANS_02 = self.TXT_IMG_MANIP.createTextSprite(
        TEXT_D['transistion_2'],'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        self.TRANS_03 = self.TXT_IMG_MANIP.createTextSprite(
        TEXT_D['transistion_3'],'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        self.TRANS_04 = self.TXT_IMG_MANIP.createTextSprite(
        TEXT_D['transistion_4'],'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        self.END_TEXT = self.TXT_IMG_MANIP.createTextSprite(
        TEXT_D['end'],'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        #drink data
        self.DRINKS_LIST = []
        ZIP_DRINKS = zip(self.DATA.DRINK_FREQ_SERIES.index,self.DATA.DRINK_FREQ_SERIES.values)
        for i in ZIP_DRINKS:
            self.DRINKS_LIST.append("{}: {} time(s)".format(i[0],i[1]))
        self.DRINKS_LIST = '\n'.join(self.DRINKS_LIST)
        self.DRINKS_LIST_Y = self.Y
        self.MOST_FREQ_DRINKS = [i for i in self.DATA.MOST_FREQ_DRINKS]
        self.MOST_FREQ_DRINKS = '\n'.join(self.MOST_FREQ_DRINKS)

        self.MOST_FREQ_DRINKS_TEXT = self.TXT_IMG_MANIP.createTextSprite(
        self.MOST_FREQ_DRINKS,'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)

        #video count
        self.VIDEO_COUNT = str(len(self.DATA.INFO_LIST))
        self.VIDEO_COUNT_TEXT = self.TXT_IMG_MANIP.createTextSprite(
        self.VIDEO_COUNT,'comicsansmc',50,(255,255,255),WIN_WIDTH//2,WIN_HEIGHT//2)



        #pg timing
        self.FRAME = 0
        self.FPS = 60
        self.LAST_UPDATE = pg.time.get_ticks()
        #to stop the sprite
        self.STOP = False

    def draw(self,img,rect):
        self.SURF.blit(img,rect)

    def update(self):
        BORDER = -2*WIN_HEIGHT
        if self.INTRO_TEXT_Y > BORDER:
            self.TXT_IMG_MANIP.centerRender(self.SURF,self.INTRO_TEXT,'comicsansmc',100,(255,255,255),
            self.X,self.INTRO_TEXT_Y,WIN_WIDTH-self.X,10)
            self.INTRO_TEXT_Y -= 2
            
        elif self.INTRO_TEXT_Y <= BORDER:
            now = pg.time.get_ticks()
            if now - self.LAST_UPDATE > self.FRAME_RATE:
                self.LAST_UPDATE = now
                self.FRAME +=1
            if self.FRAME < 30:
                self.draw(self.BEGINNING_TEXT[0],self.BEGINNING_TEXT[1])

            elif 35 < self.FRAME < 95:
                self.draw(self.DAY_FREQ_PIE[0],self.DAY_FREQ_PIE[1])
                self.TXT_IMG_MANIP.centerRender(self.SURF,self.DAY_FREQ_TEXT,'comicsansmc',50,(255,255,255),
                10,20,WIN_WIDTH-self.X,10)

            elif  100 < self.FRAME < 155:
                self.draw(self.DRINK_FREQ_PIE[0],self.DRINK_FREQ_PIE[1])
                self.TXT_IMG_MANIP.centerRender(self.SURF,self.DRINK_FREQ_TEXT,'comicsansmc',50,(255,255,255),
              10,20,WIN_WIDTH-self.X,10)

            elif 160 < self.FRAME < 215:
                self.draw(self.TRANS_01[0],self.TRANS_01[1])

            elif 220 < self.FRAME < 515:
                self.TXT_IMG_MANIP.delimitedRender(self.SURF,self.DRINKS_LIST,'comicsansmc',50,(255,255,255),
                WIN_WIDTH//4,self.DRINKS_LIST_Y,'\n',10)
                self.DRINKS_LIST_Y -=5

            elif 520 < self.FRAME < 545:
                self.draw(self.TRANS_02[0],self.TRANS_02[1])

            elif 550 < self.FRAME < 605:
                self.draw(self.TRANS_03[0],self.TRANS_03[1])

            elif 610 < self.FRAME < 655:
                self.draw(self.MOST_FREQ_DRINKS_TEXT[0],self.MOST_FREQ_DRINKS_TEXT[1])

            elif 660 < self.FRAME < 695:
                self.draw(self.TRANS_04[0],self.TRANS_04[1])

            elif 700 < self.FRAME < 745:
                self.draw(self.VIDEO_COUNT_TEXT[0],self.VIDEO_COUNT_TEXT[1])
            
            elif 750 < self.FRAME < 800:
                self.draw(self.END_TEXT[0],self.END_TEXT[1])
            
            elif self.FRAME > 800:
                self.STOP = True


            

            


            



                
        
            








        


