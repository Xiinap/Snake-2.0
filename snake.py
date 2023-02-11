'''
importing
'''
import pygame
import random
import sys
pygame.init()
'''
colors
'''
WHITE = [225, 225, 225]
BLACK = [0, 0, 0]
GREEN = [0, 225, 0]
BLUE = [0, 0, 225]
RED = [225, 0, 0]
YELLOW = [222, 163, 0]
GREEM = [57, 130, 49]
SNAKE_CL = [102, 12, 225]
SNAKE_COL = [102, 21, 215]
BG = [50, 110, 44]
GRAY = [40, 40, 40]
HEADER_CL = [57, 130, 49]
'''
Sizes
'''
SIZE_BLOCK = 25
COUNT_BLOCK = 25
MARGIN = 1
HEADER = 70

size = [SIZE_BLOCK * COUNT_BLOCK + MARGIN * COUNT_BLOCK + 2 * SIZE_BLOCK,
        SIZE_BLOCK * COUNT_BLOCK + MARGIN * COUNT_BLOCK + 2 * SIZE_BLOCK + HEADER]
#print(size) #window size print
'''
window settings
'''
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SNAKE')
pygame.display.set_icon(pygame.image.load("qqq.png"))
font = pygame.font.SysFont("courier", 36)
time = pygame.time.Clock()

field = [[0 for i in range(COUNT_BLOCK)] for j in range(COUNT_BLOCK)]

class Snake:
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def is_inside(self):
                return 0 <= self.x < COUNT_BLOCK and 0 <= self.y < COUNT_BLOCK

        def __eq__(self, other):
                return isinstance(other, Snake) and self.x == other.x and self.y == other.y


def draw_block(color, row, col):
        pygame.draw.rect(screen, color, [SIZE_BLOCK + col * SIZE_BLOCK + MARGIN * (col + 1),
                                         HEADER + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])

'''
apple
'''
def get_random_block(): #apple function
        x = random.randint(0, COUNT_BLOCK - 1)
        y = random.randint(0, COUNT_BLOCK - 1)
        empty_block = Snake(x, y)
        while empty_block in snake: #it's command cant make apples on the snake
                empty_block.x = random.randint(0, COUNT_BLOCK - 1)
                empty_block.y = random.randint(0, COUNT_BLOCK - 1)
        return empty_block

total = 0 #score
speed = 1 #speed
snake = [Snake(11, 11), Snake(11, 12), Snake(11, 13)]
apple = get_random_block()
d_row = buf_row = 0
d_col = buf_col = 1

while True:
        for event in pygame.event.get():  # window creating №2
                if event.type == pygame.QUIT:
                        sys.exit()  # exit
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and d_col !=0:  # move left(arrow left)
                                buf_row = -1
                                buf_col = 0
                        elif event.key == pygame.K_DOWN and d_col !=0:  # move down(arrow down)
                                buf_row = 1
                                buf_col = 0
                        elif event.key == pygame.K_RIGHT and d_row !=0:  # move right(arrow right)
                                buf_row = 0
                                buf_col = 1
                        elif event.key == pygame.K_LEFT and d_row !=0:  # move left(arrow left)
                                buf_row = 0
                                buf_col = -1

                        elif event.key == pygame.K_ESCAPE:  #cheat code
                                speed += 1

                        elif event.key == pygame.K_q:  #exit
                                sys.exit()


        screen.fill(BG)

        pygame.draw.rect(screen, GREEM, [0, 0, size[0], HEADER])
        text_total = font.render(f"Count {total}", 0, WHITE)
        text_speed = font.render(f"Speed {speed}", 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK + 30, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK + 400, SIZE_BLOCK))


        for col in range(COUNT_BLOCK):
                for row in range(COUNT_BLOCK):
                        if(row + col) % 2 == 0:
                                color = YELLOW
                        else:
                                color = GREEM

                        draw_block(color, row, col)

        head = snake[-1] #make snake head

        if not head.is_inside():
                break

        draw_block(RED, apple.x, apple.y)

        for block in snake:
                draw_block(SNAKE_COL, block.x, block.y)
        pygame.display.flip()

        if apple == head:
                total += 1
                speed = total // 3 + 1
                snake.append(apple)
                apple = get_random_block()

        d_row = buf_row
        d_col = buf_col

        new_head = Snake(head.x + d_row, head.y + d_col)

        if new_head in snake:
                sys.exit()
                break

        snake.append(new_head)
        snake.pop(0)

        time.tick(4+speed)
        pygame.display.update()  # window update
        
a = input('')
