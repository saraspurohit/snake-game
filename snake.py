import pygame
import random
import time
import os
pygame.mixer.init()

pygame.init()



# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
pink =(233,220,229)
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake with Saras")
#
bgimg = pygame.image.load("backgroun.jpg")
bgimg= pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
kks = pygame.image.load("game over.jpeg")
kks= pygame.transform.scale(kks,(screen_width,screen_height)).convert_alpha()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
fps=60
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
 exit_game=False
 while not exit_game:
     gameWindow.fill(pink)
     text_screen("Welcome To Snake By Saras", black,150,230)
     text_screen("Press space bar to play", black,200,280)
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             exit_game=True
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 pygame.mixer.music.load('song.mp3')
                 pygame.mixer.music.play()
                 
                 gameloop()
      
     pygame.display.update()
     clock.tick(fps)
     

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width - 40)
    food_y = random.randint(20, screen_height - 40)
    score = 0
    init_velocity = 5
    snk_list = []
    
    snk_length = 1
    
    try:
        if (not os.path.exists("hiscore.txt")):
            with open("hiscore.txt","w") as f:
                f.write("0")
        with open("hiscore.txt", "r") as f:
            hiscore = int(f.read())
    except:
        hiscore = 0

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(kks,(0,0))
            text_screen("Game Over! Press Enter To Continue", red, screen_width/20, screen_height/2)
            text_screen(f"Score: {score}  Hiscore: {hiscore}", black, screen_width/15, screen_height/15)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('song.mp3')
                        pygame.mixer.music.play()
                        return gameloop

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    
                    if event.key == pygame.K_q:
                        score+=10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, screen_width - 40)
                food_y = random.randint(20, screen_height - 40)
                snk_length += 5
                if score > hiscore:
                    hiscore = score
                    with open("hiscore.txt", "w") as f:
                        f.write(str(hiscore))

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen(f"Score: {score}  Hiscore: {hiscore}", black, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1] : 
                time.sleep(1)
                game_over = True
                pygame.mixer.music.load('game  over.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('game  over.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()

welcome()
