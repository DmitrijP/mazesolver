from tkinter import Canvas
from point import Point

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2
        
    def draw(self, c: Canvas, fill_color):
        c.create_line(self.__p1.x, self.__p1.y, 
                      self.__p2.x, self.__p2.y, 
                      fill=fill_color, width=2)
        
    def __str__(self):
        return f'p1: {self.__p1} p2:{self.__p2}' 