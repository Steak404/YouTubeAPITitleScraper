import pygame as pg

class TextIMGCreator():
    '''Renders text within the width_lim'''

    def centerRender(self,win,text,font_name,font_size,color,x,y,width_lim,speed):
        font = pg.font.SysFont(font_name,font_size)
        words = text.split()
        lines = []
        while len(words)>0:
            line_elements = []
            while len(words)>0:
                line_elements.append(words.pop(0))
                font_w,font_h = font.size(' '.join(line_elements+words[:1]))
                if font_w > width_lim:
                    break
            line = ' '.join(line_elements)
            lines.append(line)

        dy = 0
        for line in lines:
            fw,fh = font.size(line)
            font_surf = font.render(line,True,color)
            win.blit(font_surf,(x,y+dy))
            dy+=(fh+speed)

    def delimitedRender(self,win,text,font_name,font_size,color,x,y,delimiter,speed):
        font = pg.font.SysFont(font_name,font_size)
        words = text.split(delimiter)
        dy=0
        for word in words:
            fw,fh = font.size(word)
            font_surf = font.render(word,True,color)
            win.blit(font_surf,(x,y+dy))
            dy += (fh+speed)


    def createTextSprite(self,text,font,size,color,x,y):
        """returns tuple of text and rect"""
        FONT = pg.font.SysFont(font,size)
        TEXT = FONT.render(text,True,color)
        TEXT_RECT = TEXT.get_rect()
        TEXT_RECT.center = (x,y)

        return (TEXT,TEXT_RECT)

    def createIMGSprite(self,img_path,x,y):
        """returns tuple of image and rect"""
        IMG = pg.image.load(img_path)
        IMG_RECT = IMG.get_rect()
        IMG_RECT.center = (x,y)
        
        return (IMG,IMG_RECT)

