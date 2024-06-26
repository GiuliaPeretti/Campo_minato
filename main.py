import pygame
from settings import *
import random

random.seed(0)

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def init_cell(size):
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

    print(selected)
    match selected:
        case 0:
            font = pygame.font.SysFont('arial', 80)
            y_offset,x_offset=20,-4
        case 1:
            font = pygame.font.SysFont('arial', 60)
            y_offset,x_offset=14,-4
        case 2:
            font = pygame.font.SysFont('arial', 40)
            y_offset,x_offset=11,-1
        case 3:
            font = pygame.font.SysFont('arial', 25)
            y_offset,x_offset=8,2
    for row in range (size):
        for col in range (size):
            n=cells[row][col]
            if n==0:
                pass
                # text=font.render('', True, PINK)
                # # screen.blit(text, (row*cell_width+20+x_offset, col*cell_width+20+y_offset))
                # screen.blit(text, (col*cell_width+20+y_offset, row*cell_width+20+x_offset))
            elif n==9:
                # text=font.render(str(n), True, RED)
                # # screen.blit(text, (row*cell_width+20+x_offset, col*cell_width+20+y_offset))
                # screen.blit(text, (col*cell_width+20+y_offset, row*cell_width+20+x_offset))
                draw_bomb(col*cell_width+20, row*cell_width+20)
            else:
                text=font.render(str(n), True, colors[n-1])
                # screen.blit(text, (row*cell_width+20+x_offset, col*cell_width+20+y_offset))
                screen.blit(text, (col*cell_width+20+y_offset, row*cell_width+20+x_offset))


def reveal_cell(row,col):
    if (status_cells[row][col]==0):
        status_cells[row][col]=1
        colors=[(0, 0, 200), (0, 150, 0), (150, 0, 209), (207, 100, 0), (33, 114, 145), (1, 77, 5), (191, 186, 42), (255, 0, 242)]

        pygame.draw.rect(screen, GRAY, (cell_width*col+20,cell_width*row+20,cell_width,cell_width))

        for i in range (20,581,cell_width):
            pygame.draw.line(screen, BACKGROUND_COLOR, (i,20),(i,580), 2)
            pygame.draw.line(screen, BACKGROUND_COLOR, (20,i),(580,i), 2)
        match select_game:
            case 0:
                font = pygame.font.SysFont('arial', 80)
                y_offset,x_offset=20,-4
            case 1:
                font = pygame.font.SysFont('arial', 60)
                y_offset,x_offset=14,-4
            case 2:
                font = pygame.font.SysFont('arial', 40)
                y_offset,x_offset=11,-1
            case 3:
                font = pygame.font.SysFont('arial', 25)
                y_offset,x_offset=8,2

        n=cells[row][col]
        print("n:" + str(n))
        if n==0:
            pass
        elif n==9:
            draw_bomb(col*cell_width+20, row*cell_width+20)
        else:
            text=font.render(str(n), True, colors[n-1])
            screen.blit(text, (col*cell_width+20+y_offset, row*cell_width+20+x_offset))
    
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
    global flag_counter
    if(status_cells[row][col]==0):
        flag_counter-=1
        set_flag_counter()
        status_cells[row][col]=2

        x=col*cell_width+20
        y=row*cell_width+20

        match select_game:
            case 0:
                x,y=x+35,y+14
                w,h=30,30
            case 1:
                x,y=x+24,y+10
                w,h=20,20
            case 2:
                x,y=x+16,y+7
                w,h=15,15
            case 3:
                x,y=x+11,y+5
                w,h=10,10

        pygame.draw.polygon(screen, RED, [(x,y),(x+w,y+w/2),(x,y+h)])
        pygame.draw.rect(screen, BROWN, (x-(w/5), y, w/5, h*1.8))
    elif(status_cells[row][col]==2):
        flag_counter+=1
        set_flag_counter()
        status_cells[row][col]=0
        draw_hidden_cell(row,col)

def draw_hidden_cell(row,col):
    x=col*cell_width+20
    y=row*cell_width+20
    pygame.draw.rect(screen, GRAY, (x,y,cell_width,cell_width))

    offset=cell_width/8

    pygame.draw.polygon(screen, DARK_GRAY, [(x+cell_width, y), (x+cell_width-offset,y+offset), (x+cell_width-offset,cell_width+y-offset), (x+cell_width, cell_width+y)])
    pygame.draw.polygon(screen, DARK_GRAY, [(x, y+cell_width), (x+offset,y+cell_width-offset), (x+cell_width-offset,cell_width+y-offset), (x+cell_width, cell_width+y)])

    pygame.draw.polygon(screen, LIGHT_GRAY, [(x, y), (x+offset,y+offset), (x+cell_width-offset,y+offset), (x+cell_width, y)])
    pygame.draw.polygon(screen, LIGHT_GRAY, [(x, y), (x+offset,y+offset), (x+offset,cell_width+y-offset), (x, cell_width+y)])

    for i in range (20,581,cell_width):
        pygame.draw.line(screen, BACKGROUND_COLOR, (i,20),(i,580), 2)
        pygame.draw.line(screen, BACKGROUND_COLOR, (20,i),(580,i), 2)

def fill_cell(start_row,start_col):
    n=0
    while n<n_bomb:
        row,col=random.randint(0,size-1), random.randint(0,size-1)
        if cells[row][col]==0 and row!=start_row and col!=start_col:
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

def start_the_game(start_row,start_col):
    fill_cell(start_row,start_col)
    row=start_row
    col=start_col
    cell_revealed=[]
    cell_to_reveal=[(row,col)]
    reveal_cell(row,col)
    while len((cell_to_reveal))>0:
        row,col=cell_to_reveal[0]
        
        if(cells[row][col]!=9):
            if(row-1>=0 and col-1>=0 and cells[row-1][col-1]!=9 and ((row-1,col-1) not in cell_revealed) ):
                if(cells[row-1][col-1]==0):
                    cell_to_reveal.append((row-1,col-1))
                reveal_cell(row-1,col-1)

            if(row-1>=0 and cells[row-1][col]!=9 and ((row-1,col) not in cell_revealed)):
                if(cells[row-1][col]==0):
                    cell_to_reveal.append((row-1,col))
                reveal_cell(row-1,col)

            if(row-1>=0 and col+1<size and cells[row-1][col+1]!=9 and ((row-1,col+1) not in cell_revealed)):
                if(cells[row-1][col+1]==0):
                    cell_to_reveal.append((row-1,col+1))
                reveal_cell(row-1,col+1)

            if(col-1>=0 and cells[row][col-1]!=9 and ((row,col-1) not in cell_revealed)):
                if(cells[row][col-1]==0):
                    cell_to_reveal.append((row,col-1))
                reveal_cell(row,col-1)

            if(col+1<size and cells[row][col+1]!=9 and ((row,col+1) not in cell_revealed)):
                if(cells[row][col+1]==0):
                    cell_to_reveal.append((row,col+1))
                reveal_cell(row,col+1)

            if(row+1<size and col+1<size and cells[row+1][col+1]!=9 and ((row+1,col+1) not in cell_revealed)):
                if(cells[row+1][col+1]==0):
                    cell_to_reveal.append((row+1,col+1))
                reveal_cell(row+1,col+1)

            if(row+1<size and cells[row+1][col]!=9 and ((row+1,col) not in cell_revealed)):
                if(cells[row+1][col]==0):
                    cell_to_reveal.append((row+1,col))
                reveal_cell(row+1,col)

            if(row+1<size and col-1>=0 and cells[row+1][col-1]!=9 and ((row+1,col-1) not in cell_revealed)):
                if(cells[row+1][col-1]==0):
                    cell_to_reveal.append((row+1,col-1))
                reveal_cell(row+1,col-1)
        cell_to_reveal.pop(0)
        cell_revealed.append((row,col))

def check_win():
    win=True
    loose=False
    for row in range (size):
        for col in range (size):
            if(win and cells[row][col]!=9 and status_cells[row][col]==0):
                win=False
            if(cells[row][col]==9 and status_cells[row][col]==1):
                loose=True
                win=False
                break
        if(loose):
            break
    return(win,loose)
                
def end():
    show_result()
    font = pygame.font.SysFont('arial', 40)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (640,490,100,100))
    if(loose):
        text=font.render("Lost", True, RED)
        screen.blit(text, (650, 500))
    else:
        text=font.render("Win", True, RED)
        screen.blit(text, (650, 500))

def draw_bomb(x,y):
    pygame.draw.circle(screen, (20,20,20), (x+cell_width/2, y+cell_width/2+cell_width/7), cell_width/3)
    pygame.draw.rect(screen, (20,20,20), (x+(3*cell_width/8), y+cell_width/4, cell_width/4, cell_width/6))
    # pygame.draw.polygon(screen, RED, [(x+(3*cell_width/8), y+cell_width/4), (x+(3*cell_width/8)+cell_width/8, y+cell_width/6), (x+(3*cell_width/8)+(cell_width/4), y+cell_width/4)])
    pygame.draw.polygon(screen, RED, [(x+(3*cell_width/8)-1, y+cell_width/4-1), (x+(3*cell_width/8)+cell_width/8, y+cell_width/7), (x+(3*cell_width/8)+(cell_width/4)-1, y+cell_width/4-1)])

def set_flag_counter():
    global flag_counter
    x,y,w,h=700,220,25,25
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x-70,y-7,100,70))
    pygame.draw.polygon(screen, RED, [(x,y),(x+w,y+w/2),(x,y+h)])
    pygame.draw.rect(screen, BROWN, (x-(w/5), y, w/5, h*1.8))
    font = pygame.font.SysFont('arial', 40)

    text=font.render(str(flag_counter), True, GRAY)
    if flag_counter>9:
        screen.blit(text, (x-60,y))
    else:
        screen.blit(text, (x-40,y))




if __name__=='__main__':

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
    first_cell=True
    loose=False
    win=False
    flag_counter=0

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
                        row=(y-20)//cell_width
                        col=(x-20)//cell_width
                        if(first_cell):
                            first_cell=False
                            start_the_game(row,col)
                        else:
                            reveal_cell(row, col)
                            win,loose=check_win()
                            print(win,loose)

                    else:

                        for i in range (len(buttons)):
                            if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                                if(i<len(buttons)-1):
                                    selected=i
                                    if(not(game_started)):
                                        select_game=selected
                                    draw_buttons(selected)
                                    break
                                elif(i==4):
                                    if(selected!=-1):
                                        pygame.draw.rect(screen, BACKGROUND_COLOR, (640,490,100,100))   
                                        select_game=selected
                                        win=False
                                        loose=False
                                        game_started=True
                                        first_cell=True
                                        cell_width, size, n_bomb=get_cell_size()
                                        flag_counter=n_bomb
                                        set_flag_counter()
                                        draw_hidden_cells(cell_width)
                                        draw_hidden_cells(cell_width)
                                        cells,status_cells=init_cell(size)
                                        buttons=gen_buttons()
                                        draw_buttons(selected)
                                    break
                        else:
                            selected=-1
                        draw_buttons(selected)
                elif(event.button==3):
                    if(game_started and x>=20 and x<=560 and y>=20 and x<=560):
                        row=(y-20)//cell_width
                        col=(x-20)//cell_width
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
        
        if (loose and game_started):
            print('LOST')
            end()
            game_started=False
        elif(win and game_started):
            print('WIN')
            end()
            game_started=False

        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()