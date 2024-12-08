from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window   
    
    
def main():
    win = Window(800, 600)

    #draw_cells_test(win=win)
    draw_maze_test(win=win)
    
    win.wait_for_close()

def draw_maze_test(win: Window):
    maze = Maze(Point(10, 10), 10, 10, 50, 50, win)
    maze.draw()
    
def draw_cells_test(win: Window):
    p1 = Point(10, 10)
    p2 = Point(70, 70)
    cell1 = Cell(p1=p1, p2=p2, window= win, right_wall=False)
    cell1.draw()

    p3 = Point(70, 10)
    p4 = Point(140, 70)
    cell2 = Cell(p1=p3, p2=p4, window= win, left_wall=False, bottom_wall=False)
    cell2.draw()
    
    #cell right test
    cell1.draw_move(cell2)
    
    p5 = Point(70, 70)
    p6 = Point(140, 140)
    cell3 = Cell(p1=p5, p2=p6, window= win, top_wall=False, left_wall=False)
    cell3.draw()
    
    #cell below test
    cell2.draw_move(cell3, True)
    
    p7 = Point(10, 70)
    p8 = Point(70, 140)
    cell4 = Cell(p1= p7, p2= p8, window= win, right_wall=False, bottom_wall=False)
    cell4.draw()
    
    #cell left test
    cell3.draw_move(cell4)
    
    p9 = Point(10, 140)
    p10 = Point(70, 210)
    cell5 = Cell(p1=p9, p2=p10, window= win, top_wall=False)
    cell5.draw()
    
    #Cell above test
    cell5.draw_move(cell4)

main()