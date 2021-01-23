from info_extractor import infoExtractor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
from settings import DEV_KEY,PLAYLIST_ID

class DataManipulator():
    ''''Handles all data manipulation'''
    def __init__(self):
        self.DEV_KEY = DEV_KEY
        self.PLAYLIST_ID = PLAYLIST_ID
        self.EXTRACTOR = infoExtractor(self.DEV_KEY,self.PLAYLIST_ID)
        #is a list of lists
        self.INFO_LIST = None
        self.DF = None
        self.DRINKS = None
        self.DAYS = None
        self.DRINK_FREQ_SERIES = None
        self.DAY_FREQ_SERIES = None
        self.MOST_FREQ_DRINKS = None

    def initialize(self):
        self.INFO_LIST = self.EXTRACTOR.grabVidInfo()
        self.createDFs()

    def createDFs(self):
        self.DF = pd.DataFrame(self.INFO_LIST,columns = ['Drink','Day of Week'])
        self.DRINKS = self.DF['Drink']
        self.DAYS = self.DF['Day of Week']

        self.DRINK_FREQ_SERIES = pd.Index(self.DRINKS).value_counts()
        self.DAY_FREQ_SERIES = pd.Index(self.DAYS).value_counts()
        self.MOST_FREQ_DRINKS = (i for i in self.DRINKS.mode())

    def createCSV(self,df,name):
        df.to_csv(name,header=None)

    def closeGraphs(self):
        plt.close('all')

    def piePlot(self,data,label,title):
        data.plot.pie(label=label,title=title)

        plt.tight_layout()
        plt.show()

    def piePlotWeekDays(self):
        self.piePlot(self.DAY_FREQ_SERIES,label='',title='Drinking by Weekday')

    def piePlotDrinkFreq(self):
        self.piePlot(self.DRINK_FREQ_SERIES,label='',title='Beverage and freqency')

    def closePlot(self):
        plt.close()
        
    
# t = DataManipulator()
# t.initialize()
# # #t.piePlotDrinkFreq()
# s = t.MOST_FREQ_DRINKS
# print(len)
# s = t.DRINK_FREQ_SERIES
# l = zip(s.index,s.values)
# d = []
# for i in l:
#     d.append("{}:{}".format(i[0],i[1]))
# d = '\n'.join(d)

# print(d)

#print(s.values)
#for i,v in s.items():
#    print(i,v)









