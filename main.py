import pygame
from settings import *
import random

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def init_cell(size, n_bomb):
    cells=[]
    status_cells=[]

    for i in range (size):
        t1=[]
        t2=[]
        for j in range(size):
            t1.append(0)
            t2.append(0)
        cells.append(t1)
        status_cells.append(t2)
    n=0
    while n<n_bomb:
        row,col=random.randint(0,size-1), random.randint(0,size-1)
        if cells[row][col]==0:
            cells[row][col]=9
            n+=1

    for row in range(size):
        for col in range(size):
            if(cells[row][col]!=9):
                if(row-1>=0 and col-1>=0 and cells[row-1][col-1]==9):
                    cells[row][col]+=1
                if(row-1>=0 and cells[row-1][col]==9):
                    cells[row][col]+=1
                if(row-1>=0 and col+1<size and cells[row-1][col+1]==9):
                    cells[row][col]+=1
                if(col-1>=0 and cells[row][col-1]==9):
                    cells[row][col]+=1
                if(col+1<size and cells[row][col+1]==9):
                    cells[row][col]+=1
                if(row+1<size and col+1<size and cells[row+1][col+1]==9):
                    cells[row][col]+=1
                if(row+1<size and cells[row+1][col]==9):
                    cells[row][col]+=1
                if(row+1<size and col-1>=0 and cells[row+1][col-1]==9):
                    cells[row][col]+=1

    return(cells,status_cells)
    
def draw_hidden_cells(cell_width):
    pygame.draw.rect(screen, GRAY, (20,20,560,560))

    x,y =20,20
    offset=cell_width/8
    for i in range(size):
        x=20
        for j in range (size):
            pygame.draw.polygon(screen, DARK_GRAY, [(x+cell_width, y), (x+cell_width-offset,y+offset), (x+cell_width-offset,cell_width+y-offset), (x+cell_width, cell_width+y)])
            pygame.draw.polygon(screen, DARK_GRAY, [(x, y+cell_width), (x+offset,y+cell_width-offset), (x+cell_width-offset,cell_width+y-offset), (x+cell_width, cell_width+y)])


            pygame.draw.polygon(screen, LIGHT_GRAY, [(x, y), (x+offset,y+offset), (x+cell_width-offset,y+offset), (x+cell_width, y)])
            pygame.draw.polygon(screen, LIGHT_GRAY, [(x, y), (x+offset,y+offset), (x+offset,cell_width+y-offset), (x, cell_width+y)])
            x=x+cell_width
        y=y+cell_width
    
    for i in range (20,581,cell_width):
        pygame.draw.line(screen, BACKGROUND_COLOR, (i,20),(i,580), 2)
        pygame.draw.line(screen, BACKGROUND_COLOR, (20,i),(580,i), 2)

def gen_buttons():
    x,y,w,h=640,20,100,30
    buttons=[]
    for i in range (1,5):
        buttons.append({'name': 'Level '+str(i), 'coordinates': (x,y,w,h)})
        y=y+h+10
    buttons.append({'name': 'Play', 'coordinates': (x,y,w,h)})

    return(buttons)

def draw_buttons(selected):
    
    for b in buttons[:len(buttons)]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+17,b['coordinates'][1]+3))
    
    if selected!=-1:
        pygame.draw.rect(screen, PINK, buttons[selected]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
        text=font.render(buttons[selected]['name'], True, BLACK)
        screen.blit(text, (buttons[selected]['coordinates'][0]+17,buttons[selected]['coordinates'][1]+3))

    pygame.draw.rect(screen, GRAY, buttons[-1]['coordinates'])
    pygame.draw.rect(screen, BLACK,  buttons[-1]['coordinates'], 3)
    text=font.render( buttons[-1]['name'], True, BLACK)
    screen.blit(text, ( buttons[-1]['coordinates'][0]+30, buttons[-1]['coordinates'][1]+3))

def show_result():
    colors=[(0, 0, 200), (0, 150, 0), (150, 0, 209), (207, 100, 0), (33, 114, 145), (1, 77, 5), (191, 186, 42), (255, 0, 242)]
    # x=0
    # for i in colors:
    #     pygame.draw.rect(screen, i, (x,0,20,20))
    #     x=x+20
    pygame.draw.rect(screen, GRAY, (20,20,560,560))

    for i in range (20,581,cell_width):
        pygame.draw.line(screen, BACKGROUND_COLOR, (i,20),(i,580), 2)
        pygame.draw.line(screen, BACKGROUND_COLOR, (20,i),(580,i), 2)

    match selected:
        case 0:
            font = pygame.font.SysFont('arial', 80)
            x_offset,y_offset=20,-4
        case 1:
            font = pygame.font.SysFont('arial', 60)
            x_offset,y_offset=14,-4
        case 2:
            font = pygame.font.SysFont('arial', 40)
            x_offset,y_offset=11,-1
        case 3:
            font = pygame.font.SysFont('arial', 25)
            x_offset,y_offset=8,2
    for row in range (size):
        for col in range (size):
            text=cells[row][col]
            if text==0:
                text=''
                text=font.render(text, True, PINK)
                screen.blit(text, (row*cell_width+20+x_offset, col*cell_width+20+y_offset))
            elif text==9:
                text=font.render(str(text), True, RED)
                screen.blit(text, (row*cell_width+20+x_offset, col*cell_width+20+y_offset))
            else:
                print(text)
                text=font.render(str(text), True, colors[text-1])
                screen.blit(text, (row*cell_width+20+x_offset, col*cell_width+20+y_offset))

def reveal_cell(row,col):
    print(select_game)
    #  TODO: controllo di perdita/vincita
    # status_cells[row][col]=1
    colors=[(0, 0, 200), (0, 150, 0), (150, 0, 209), (207, 100, 0), (33, 114, 145), (1, 77, 5), (191, 186, 42), (255, 0, 242)]

    pygame.draw.rect(screen, GRAY, (cell_width*col+20,cell_width*row+20,cell_width,cell_width))

    for i in range (20,581,cell_width):
        pygame.draw.line(screen, BACKGROUND_COLOR, (i,20),(i,580), 2)
        pygame.draw.line(screen, BACKGROUND_COLOR, (20,i),(580,i), 2)

    match select_game:
        case 0:
            print("livello 1")
            font = pygame.font.SysFont('arial', 80)
            x_offset,y_offset=20,-4
        case 1:
            print("livello 2")
            font = pygame.font.SysFont('arial', 60)
            x_offset,y_offset=14,-4
        case 2:
            print("livello 3")
            font = pygame.font.SysFont('arial', 40)
            x_offset,y_offset=11,-1
        case 3:
            print("livello 4")
            font = pygame.font.SysFont('arial', 25)
            x_offset,y_offset=8,2

    text=cells[row][col]
    if text==0:
        text=''
        text=font.render(text, True, PINK)
        screen.blit(text, (col*cell_width+20+x_offset, row*cell_width+20+y_offset))
    elif text==9:
        text=font.render(str(text), True, RED)
        screen.blit(text, (col*cell_width+20+x_offset, row*cell_width+20+y_offset))
    else:
        print(text)
        text=font.render(str(text), True, colors[text-1])
        screen.blit(text, (col*cell_width+20+x_offset, row*cell_width+20+y_offset))

def get_cell_size():
    match select_game:
        case 0:
            return(80, 560//80, 10)
        case 1:
            return(56, 560//56, 20)
        case 2:
            return(40, 560//40, 40)
        case 3:
            return(28, 560//28, 60)
        
def flag_cell(row,col):
    x=col*cell_width
    y=row*cell_width
    pygame.draw.polygon(screen, RED, (X))




pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
pygame.display.set_caption('Campo minato♥')
font = pygame.font.SysFont('arial', 20)

#28, 40, 56, 80
#20, 14, 10, 7
cell_width=0
size=0
selected = -1

buttons=gen_buttons()
draw_buttons(-1)
game_started=False
select_game=-1


run  = True

number=0

while run:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if (event.button==1):
                if(game_started and x>=20 and x<=560 and y>=20 and x<=560):
                    row=y//cell_width
                    col=x//cell_width
                    reveal_cell(row, col)
                else:

                    for i in range (len(buttons)):
                        print("for "+str(i))
                        if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                            print("entra nel bottone")
                            if(i<len(buttons)-1):
                                print("cambia selected")
                                selected=i
                                if(not(game_started)):
                                    select_game=selected
                                print(selected)
                                draw_buttons(selected)
                                break
                            elif(i==4):
                                print("paley")
                                print(selected)
                                #TODO: it dosent works
                                if(selected!=-1):
                                    select_game=selected
                                    print("play")
                                    game_started=True
                                    cell_width, size, n_bomb=get_cell_size()
                                    print("cell width"+str(cell_width))
                                    print("size "+str(size))
                                    draw_hidden_cells(cell_width)
                                    cells,status_cells=init_cell(size, n_bomb)
                                    buttons=gen_buttons()
                                    draw_buttons(selected)
                                break
                    else:
                        print("entra nell'ultimo")
                        selected=-1
                    draw_buttons(selected)
        elif(event.button==3):
            if(game_started and x>=20 and x<=560 and y>=20 and x<=560):
                row=y//cell_width
                col=x//cell_width
                flag_cell(row, col)


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