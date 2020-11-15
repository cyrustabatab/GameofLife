import pygame
from copy import deepcopy


pygame.init()


clock = pygame.time.Clock()

WIDTH = HEIGHT = 400

NUMBER_OF_SQUARES = 20

SQUARE_SIZE = 20 

screen =pygame.display.set_mode((400,400))

RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


class Block:
    


    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.alive = False
        self.color = RED

    
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,SQUARE_SIZE,SQUARE_SIZE))
        pygame.draw.rect(screen,BLACK,(self.x,self.y,SQUARE_SIZE,SQUARE_SIZE),2)





    def switch_alive(self):
        self.alive = not self.alive

        if self.alive:
            self.color = GREEN
        else:
            self.color = RED



    






def change_states(blocks):

    blocks_copy = deepcopy(blocks)
    for row in range(len(blocks)):
        for col in range(len(blocks[0])):
            block = blocks_copy[row][col]
            alive = block.alive
            live_neighbors = 0
            for x_diff in (-1,0,1):
                for y_diff in (-1,0,1):
                    if x_diff == y_diff == 0:
                        continue

                    neighbor_row,neighbor_col = row + x_diff,col + y_diff
                    if 0 <= neighbor_row < len(blocks) and 0 <= neighbor_col < len(blocks[0]) and blocks_copy[neighbor_row][neighbor_col].alive:
                        live_neighbors += 1

            

            if alive:
                if live_neighbors < 2 or live_neighbors > 3:
                    blocks[row][col].switch_alive()
            else:
                if live_neighbors == 3:
                    blocks[row][col].switch_alive()









blocks = []
boundary = 0
for i in range(NUMBER_OF_SQUARES):
    row = []
    for j in range(NUMBER_OF_SQUARES):
        block = Block(j * (SQUARE_SIZE + boundary),i * (SQUARE_SIZE + boundary))
        row.append(block)
    blocks.append(row)


blocks[10][10].switch_alive()
blocks[10][11].switch_alive()
blocks[10][12].switch_alive()


done = False

paused = False
while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            row ,col= y // 20 ,x//20
            blocks[row][col].switch_alive()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        change_states(blocks)    


    screen.fill(RED)
    
    for row in range(len(blocks)):
        for col in range(len(blocks[0])):
            blocks[row][col].draw()
    pygame.display.update()
    clock.tick(10)








