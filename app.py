import pygame
import random

# GLOBAL VARS
s_width = 400
s_height = 400
block_size = 10

win = pygame.display.set_mode((s_width, s_height))

class Food(object):
    def __init__(self, pos):
        self.pos = pos
    
    def draw(self):
        pygame.draw.rect(win, (255,0,0), (self.pos[0]-1, self.pos[1]-1, block_size-1, block_size-1), 0)
    
    def change_pos(self, pos):
        self.pos = pos

class Snake(object):
    def __init__(self, headx, heady):
        self.headx = 10
        self.heady = 10
        self.body = [()]
        self.dx = 1
        self.dy = 0

    def move(self, food):

        self.body.append((self.headx, self.heady))

        self.headx += self.dx * block_size
        self.heady += self.dy * block_size
        
        self.body.pop(0)

        if self.headx == food.pos[0] and self.heady == food.pos[1]:
            food.change_pos(generate_food())
            self.body.append((self.headx, self.heady))

        for item in self.body:
            if self.headx == item[0] and self.heady == item[1]:
                pass
            pygame.draw.rect(win, (255,255,255), (item[0]-1,item[1]-1, block_size-1, block_size-1), 0)
            

        pygame.draw.rect(win, (255,255,255), (self.headx-1, self.heady-1, block_size-1, block_size-1), 0)
        pygame.display.flip()

def generate_food():
    return (random.randint(0, (s_width/block_size)-1)*block_size, random.randint(0, (s_height/block_size)-1)*block_size)

def main():
    run = True

    clock = pygame.time.Clock()

    snake = Snake(10,10)
    food = Food(generate_food())
    print(food.pos)
    move_time = 0
    move_speed = 0.05
    
    while run:
        
        move_time += clock.get_rawtime()
        clock.tick()

        if move_time / 1000 > move_speed:
            win.fill((0,0,0))
            move_time = 0
            snake.move(food)
            food.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dy = 1
                    snake.dx = 0
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dy = -1
                    snake.dx = 0
        pygame.display.update()
    
    pygame.display.quit()

main()