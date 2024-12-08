
from __future__ import annotations
from line import Line
from point import Point
from window import Window

class Cell:
    def __init__(self, p1:Point, p2:Point, window:Window,
                 right_wall:bool = True, left_wall:bool = True, 
                 top_wall:bool = True, bottom_wall:bool = True):
        self.__p1 = p1
        self.__p2 = p2
        self.__window = window
        self.right_wall = right_wall
        self.left_wall = left_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
    
    def draw(self, line_color = "black"):
        if self.left_wall:
            tl = self.__p1
            bl = Point(self.__p1.x, self.__p2.y)
            self.__window.draw_line(Line(tl,bl), line_color)
        if self.top_wall:
            tl = self.__p1
            tr = Point(self.__p2.x, self.__p1.y)
            self.__window.draw_line(Line(tl,tr), line_color)
        if self.bottom_wall:
            bl = Point(self.__p1.x, self.__p2.y)
            br = Point(self.__p2.x, self.__p2.y)
            self.__window.draw_line(Line(bl,br), line_color)
        if self.right_wall:
            tl = Point(self.__p2.x, self.__p1.y)
            br = Point(self.__p2.x, self.__p2.y)
            self.__window.draw_line(Line(tl,br), line_color)
            
    def draw_move(self, other: Cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        # to cell on right side
        if (self.__p1.y == other.__p1.y and self.__p2.y == other.__p2.y and 
            self.__p1.x < other.__p1.x and self.__p2.x < other.__p2.x):
            cntrY = self.__p1.y + ((self.__p2.y - self.__p1.y) / 2 )
            strtX = self.__p1.x + ((self.__p2.x - self.__p1.x) / 2 )
            endX = other.__p2.x - ((other.__p2.x - other.__p1.x) / 2 )
            p1 = Point(strtX, cntrY)
            p2 = Point(endX, cntrY)
            l = Line(p1, p2)
            print(f'To cell right side {l}')
            self.__window.draw_line(l, line_color)
        
        ## to cell on left side
        if (self.__p1.y == other.__p1.y and self.__p2.y == other.__p2.y and 
            self.__p1.x > other.__p1.x and self.__p2.x > other.__p2.x):
            cntrY = self.__p1.y + ((self.__p2.y - self.__p1.y) / 2 )
            strtX = self.__p2.x - ((self.__p2.x - self.__p1.x) / 2 )
            endX = other.__p1.x + ((other.__p2.x - other.__p1.x) / 2 )
            p1 = Point(strtX, cntrY)
            p2 = Point(endX, cntrY)
            l = Line(p1, p2)
            print(f'To cell left side {l}')
            self.__window.draw_line(l, line_color)
        
        # to cell above
        if (self.__p1.x == other.__p1.x and self.__p2.x == other.__p2.x and 
            self.__p1.y > other.__p1.y and self.__p2.y > other.__p2.y):
            cntrX = self.__p1.x + ((self.__p2.x - self.__p1.x) / 2 )
            strtY = self.__p2.y - ((self.__p2.y - self.__p1.y) / 2 )
            endY = other.__p1.y + ((other.__p2.y - other.__p1.y) / 2 )
            p1 = Point(cntrX, strtY)
            p2 = Point(cntrX, endY)
            l = Line(p1, p2)
            print(f'To cell above {l}')
            self.__window.draw_line(l, line_color)
        
        # to cell below
        if (self.__p1.x == other.__p1.x and self.__p2.x == other.__p2.x and 
            self.__p1.y < other.__p1.y and self.__p2.y < other.__p2.y):
            cntrX = self.__p1.x + ((self.__p2.x - self.__p1.x) / 2 )
            strtY = self.__p1.y + ((self.__p2.y - self.__p1.y) / 2 )
            endY = other.__p2.y - ((other.__p2.y - other.__p1.y) / 2 )
            p1 = Point(cntrX, strtY)
            p2 = Point(cntrX, endY)
            l = Line(p1, p2)
            print(f'To cell below {l}')
            self.__window.draw_line(l, line_color)
    
            
            