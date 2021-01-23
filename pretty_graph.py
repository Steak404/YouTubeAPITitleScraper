import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import os

class prettyPie():
    def __init__(self,x,y,rad,name):
        self.CWD = os.getcwd()
        self.GRAPH_FLDR = os.path.join(self.CWD,'graphs')
        self.x = x
        self.y = y
        r = lambda:random.randint(0,255)
        self.colors = ['#%02X%02X%02X' % (r(),r(),r()) for i in range(len(y))]
        self.rad = rad
        self.percent = [100*i/y.sum() for i in y]

        #file name
        self.FILE_NAME = "{}.png".format(os.path.join(self.GRAPH_FLDR,name))

    def plot(self):
        patches,text = plt.pie(self.y,colors=self.colors,startangle=90,radius=self.rad)
        labels = ['{0} - {1:1.2f}%'.format(i,j) for i,j in zip(self.x,self.percent)]

        plt.legend(patches,labels,loc='upper left',bbox_to_anchor=(-0.1,1.),fontsize=9)
        plt.tight_layout()
        plt.savefig(fname=self.FILE_NAME)
        return self.FILE_NAME

        
# series = pd.read_csv('DAY_FREQ_SERIES.csv',names = ['Day','Frequency'])
# x, y = series['Day'],series['Frequency']

# pp = prettyPie(x,y,rad=1,name='test')
# pp.plot()
