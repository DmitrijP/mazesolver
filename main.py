from cell import Cell
from line import Line
from point import Point
from window import Window   
    
    
def main():
    win = Window(800, 600)

    p1 = Point(10, 10)
    p2 = Point(70, 70)
    cell1 = Cell(p1, p2, win)
    cell1.draw()

    p3 = Point(70, 70)
    p4 = Point(140, 140)
    cell2 = Cell(p3, p4, win)
    cell2.draw()
    
    p3 = Point(70, 70)
    p4 = Point(140, 140)
    cell2 = Cell(p3, p4, win)
    cell2.draw()
    
    win.wait_for_close()

main()