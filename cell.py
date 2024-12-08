
from __future__ import annotations
from line import Line
from point import Point
from window import Window

class Cell:
    def __init__(self, window:Window, 
                 p1:Point = None, p2:Point = None, 
                 right_wall:bool = True, left_wall:bool = True, 
                 top_wall:bool = True, bottom_wall:bool = True):
        self.p1 = p1
        self.p2 = p2
        self.__window = window
        self.right_wall = right_wall
        self.left_wall = left_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
    
    def draw(self, line_color = "black"):
        
        tl = self.p1
        bl = Point(self.p1.x, self.p2.y)
        if self.left_wall:
            self.__window.draw_line(Line(tl,bl), line_color)
        else:
            self.__window.draw_line(Line(tl,bl), "white")
        
        tl = self.p1
        tr = Point(self.p2.x, self.p1.y)
        if self.top_wall:
            self.__window.draw_line(Line(tl,tr), line_color)
        else:
            self.__window.draw_line(Line(tl,tr), "white")
        
        bl = Point(self.p1.x, self.p2.y)
        br = Point(self.p2.x, self.p2.y)
        if self.bottom_wall:
            self.__window.draw_line(Line(bl,br), line_color)
        else:
            self.__window.draw_line(Line(bl,br), "white")
            
        tl = Point(self.p2.x, self.p1.y)
        br = Point(self.p2.x, self.p2.y)
        if self.right_wall:
            self.__window.draw_line(Line(tl,br), line_color)
        else:
            self.__window.draw_line(Line(tl,br), "white")
    
    def draw_move(self, other: Cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        # to cell on right side
        if (self.p1.y == other.p1.y and self.p2.y == other.p2.y and 
            self.p1.x < other.p1.x and self.p2.x < other.p2.x):
            cntrY = self.p1.y + ((self.p2.y - self.p1.y) / 2 )
            strtX = self.p1.x + ((self.p2.x - self.p1.x) / 2 )
            endX = other.p2.x - ((other.p2.x - other.p1.x) / 2 )
            p1 = Point(strtX, cntrY)
            p2 = Point(endX, cntrY)
            l = Line(p1, p2)
            print(f'To cell right side {l}')
            self.__window.draw_line(l, line_color)
        
        ## to cell on left side
        if (self.p1.y == other.p1.y and self.p2.y == other.p2.y and 
            self.p1.x > other.p1.x and self.p2.x > other.p2.x):
            cntrY = self.p1.y + ((self.p2.y - self.p1.y) / 2 )
            strtX = self.p2.x - ((self.p2.x - self.p1.x) / 2 )
            endX = other.p1.x + ((other.p2.x - other.p1.x) / 2 )
            p1 = Point(strtX, cntrY)
            p2 = Point(endX, cntrY)
            l = Line(p1, p2)
            print(f'To cell left side {l}')
            self.__window.draw_line(l, line_color)
        
        # to cell above
        if (self.p1.x == other.p1.x and self.p2.x == other.p2.x and 
            self.p1.y > other.p1.y and self.p2.y > other.p2.y):
            cntrX = self.p1.x + ((self.p2.x - self.p1.x) / 2 )
            strtY = self.p2.y - ((self.p2.y - self.p1.y) / 2 )
            endY = other.p1.y + ((other.p2.y - other.p1.y) / 2 )
            p1 = Point(cntrX, strtY)
            p2 = Point(cntrX, endY)
            l = Line(p1, p2)
            print(f'To cell above {l}')
            self.__window.draw_line(l, line_color)
        
        # to cell below
        if (self.p1.x == other.p1.x and self.p2.x == other.p2.x and 
            self.p1.y < other.p1.y and self.p2.y < other.p2.y):
            cntrX = self.p1.x + ((self.p2.x - self.p1.x) / 2 )
            strtY = self.p1.y + ((self.p2.y - self.p1.y) / 2 )
            endY = other.p2.y - ((other.p2.y - other.p1.y) / 2 )
            p1 = Point(cntrX, strtY)
            p2 = Point(cntrX, endY)
            l = Line(p1, p2)
            print(f'To cell below {l}')
            self.__window.draw_line(l, line_color)
    
            
            