import pygame
from settings import *

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def init_cell(size):
    cells=[]
    for i in range (size):
        temp=[]
        for j in range(size):
            temp.append(0)
        cells.append(temp)

def draw_cells(cell_width):
    pygame.draw.rect(screen, GRAY, (20,20,560,560))

    pygame.draw.polygon(screen, DARK_GRAY, [(0+cell_width+20, 20), ((0+cell_width+20-1,20+10)])

    
    for i in range (20,581,cell_width):
        pygame.draw.line(screen, BACKGROUND_COLOR, (i,20),(i,580), 3)
        pygame.draw.line(screen, BACKGROUND_COLOR, (20,i),(580,i), 3)


pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Campo minato')
font = pygame.font.SysFont('arial', 20)

cell_width=56
size=560//20
draw_background()
draw_cells(cell_width)






run  = True

number=0

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            # if(x>b_set_goal[0][0] and x<=b_set_goal[0][1] and y>=b_set_goal[1][0] and y<=b_set_goal[1][1]):
            #     print("set goal")
            #     set_ticket_goal(number)
            #     display_progress()
            # elif(x>b_add_hours[0][0] and x<=b_add_hours[0][1] and y>=b_add_hours[1][0] and y<=b_add_hours[1][1]):
            #     print("add hours")
            #     add_hours(number)
            #     display_progress()
            # elif(x>b_add_ticket[0][0] and x<=b_add_ticket[0][1] and y>=b_add_ticket[1][0] and y<=b_add_ticket[1][1]):
            #     print("add ticket")
            #     add_ticket(number)
            #     display_progress()
            # elif(x>b_reset[0][0] and x<=b_reset[0][1] and y>=b_reset[1][0] and y<=b_reset[1][1]):
            #     print("reset")
            #     reset()
            #     display_progress()
            # elif(x>text_bar_area[0][0] and x<=text_bar_area[0][1] and y>=text_bar_area[1][0] and y<=text_bar_area[1][1]):
            #     print("select text")
            #     selected_bar=True
            #     write_in_textbar(number,selected_bar)
            # else:
            #     selected_bar=False
            #     write_in_textbar(number,selected_bar)
        if (event.type == pygame.KEYDOWN):
            pass
            # if(selected_bar):
            #     if (event.key==pygame.K_BACKSPACE):
            #         number=number//10
            #         print(number)
            #         write_in_textbar(number,selected_bar)
            #     else:
            #         for i in range(len(INPUTS)):
            #             if (event.key==INPUTS[i]):
            #                 number=number*10+i
            #                 print(number)
            #                 write_in_textbar(number,selected_bar)
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()