from line import Line
from point import Point
from window import Window   
    
    
def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(70, 70)), "red")
    win.wait_for_close()

main()