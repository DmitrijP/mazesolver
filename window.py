from tkinter import Tk, BOTH, Canvas

from line import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver V0.1")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        pass
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.__window_running = False
    
    def draw_line(self, l:Line, fill_color):
        l.draw(self.__canvas, fill_color=fill_color)
        

        