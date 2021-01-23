from info_extractor import infoExtractor
import numpy as np
import pandas as pd
import os
import pygame as pg
import matplotlib.pyplot as plt
from sprites import Load_Screen,MainSprite
from settings import WIN_HEIGHT,WIN_WIDTH



class App():
    
    def __init__(self):
        self.CWD = os.getcwd()
        self.AUDIO_FLDR = os.path.join(self.CWD,'audio')
        self.DF = ""
        self.KP = os.path.join(self.AUDIO_FLDR,'kp.mp3')
        self.MAIN_THEME = os.path.join(self.AUDIO_FLDR,
        'KazumiTotakaMiiPlaza.mp3')
        

        #pg stuff
        pg.init()
        pg.mixer.init()
        pg.mixer.set_num_channels(8)
        self.WIN_WIDTH = WIN_WIDTH
        self.WIN_HEIGHT = WIN_HEIGHT
        self.WIN = pg.display.set_mode((self.WIN_WIDTH,self.WIN_HEIGHT))
        self.FONT = pg.font.SysFont('comicsansms',30)
        self.INTRO_CHANNEL = pg.mixer.Channel(1)
        self.RUN = True

    def getSND(self,f):
        snd = pg.mixer.Sound(f)
        return snd

    def playTheme(self):
        pg.mixer.music.load(self.MAIN_THEME)
        pg.mixer.music.play(loops=-1)

    def initialize(self):
        clock = pg.time.Clock()

        LOAD_SCREEN = Load_Screen(self.WIN,self.WIN_WIDTH//2,self.WIN_HEIGHT//2)
        MAIN_TEXT = MainSprite(self.WIN,self.WIN_WIDTH//20,self.WIN_HEIGHT//2)

        KP_FLAG = True
        FIRST = True

        while self.RUN:
            self.WIN.fill((0,0,0))
            if FIRST:
                if KP_FLAG:
                    kanpai = self.getSND(self.KP)
                    self.INTRO_CHANNEL.play(kanpai)
                    KP_FLAG = False
                self.WIN.fill((0, 0, 0))
                LOAD_SCREEN.update()
                if not self.INTRO_CHANNEL.get_busy():
                    self.playTheme()
                    FIRST = False

            else:
                if not MAIN_TEXT.STOP:
                    MAIN_TEXT.update()
                if MAIN_TEXT.STOP:
                    self.RUN = False
                    break
                    
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.RUN = False
                    break

            pg.display.update()
            clock.tick(60)

if __name__ == "__main__":
    app = App()
    app.initialize()







