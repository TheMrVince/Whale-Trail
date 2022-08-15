import pygame
import sys
import random

def game_floor():
    screen.blit(floor_base, (floor_x_pos, 450))
    screen.blit(floor_base, (floor_x_pos + 850, 450))

def check_collision(clouds):
    #collision with cloud
    for cloud in clouds:
        if whale_rect.colliderect(cloud):
            return False
    #check floor is not hit
    if whale_rect.top <= -50 or whale_rect.bottom >= 575:
        return False
    return True

def create_cloud():
    random_cloud_pos = random.choice(cloud_height)
    cloud = cloud_surface.get_rect(center = (1000, random_cloud_pos,))
    
    return cloud

def move_clouds(clouds):
    for cloud in clouds:
        cloud.centerx -= 5

    return clouds

def draw_clouds(clouds):
    for cloud in clouds:
        screen.blit(cloud_surface, cloud)

pygame.init()
clock = pygame.time.Clock()

#background music
music = pygame.mixer.Sound("sound/background_music.wav")
music.play(-1)

#vars
whale_movement = 0
floor_x_pos = 0
gravity = 0.20

screen = pygame.display.set_mode((900, 600))

background = pygame.image.load("assets/cartoon-cloud-sky-background.jpeg").convert()
background = pygame.transform.scale(background, (900, 600))

whale = pygame.image.load("assets/whale.png").convert_alpha()
whale = pygame.transform.scale(whale, (177, 123))
whale_rect = whale.get_rect(center=(125, 250))

floor_base = pygame.image.load("assets/clouds.png").convert_alpha()
floor_base = pygame.transform.scale(floor_base, (900, 200))

start_screen = pygame.image.load("assets/start screen.png").convert_alpha()
start_screen = pygame.transform.scale(start_screen, (800, 500))
game_over_rect = start_screen.get_rect(center=(450, 250))

#clouds


cloud_surface = pygame.image.load("assets/cloud2.png").convert_alpha()
cloud_surface = pygame.transform.scale(cloud_surface, (200, 150))
cloud_list = []
cloud_height = [50, 100, 150, 200, 250, 300, 350, 400, 450]

SPAWNCLOUD = pygame.USEREVENT
pygame.time.set_timer(SPAWNCLOUD, 1200)

game_active = True
while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                whale_movement = 0
                whale_movement -= 5
            if event.key == pygame.K_SPACE and game_active == False:
                whale_rect.center = (100, 250)
                whale_movement = 0
                cloud_list = []
                game_active = True
        if event.type == SPAWNCLOUD and game_active:
            cloud_list.append(create_cloud())
            

    screen.blit(background, (0, 0))
    if game_active:
        whale_movement += gravity
        whale_rect.centery += whale_movement
        screen.blit(whale, whale_rect)
        #check for check_collision
        game_active = check_collision(cloud_list)

        #Draw clouds
        cloud_list = move_clouds(cloud_list)
        draw_clouds(cloud_list)

    else:
        screen.blit(start_screen, game_over_rect)

    #Create floor
    floor_x_pos -= 1 
    game_floor()

    if floor_x_pos <= -850:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)