
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
    
    def draw(self):
        #
        if self.left_wall:
            tl = self.__p1
            bl = Point(self.__p1.x, self.__p2.y)
            self.__window.draw_line(Line(tl,bl), "red")
        if self.top_wall:
            tl = self.__p1
            tr = Point(self.__p2.x, self.__p1.y)
            self.__window.draw_line(Line(tl,tr), "red")
        if self.bottom_wall:
            bl = Point(self.__p1.x, self.__p2.y)
            br = Point(self.__p2.x, self.__p2.y)
            self.__window.draw_line(Line(bl,br), "red")
        if self.right_wall:
            tl = Point(self.__p2.x, self.__p1.y)
            br = Point(self.__p2.x, self.__p2.y)
            self.__window.draw_line(Line(tl,br), "red")
            
            