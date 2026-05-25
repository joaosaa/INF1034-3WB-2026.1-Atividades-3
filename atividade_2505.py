import pygame, sys
from pygame.locals import QUIT

clock = pygame.time.Clock()

timmy_img = pygame.image.load('timmysurf.gif')

hero_img = pygame.image.load('assets/assets/hero_walk_01.png')

curr_frame = 0
anim_time = 0
hero_walk_list = []

curr_frame_mm = 0
anim_time_mm = 0
megaman_spritesheet = pygame.image.load('megaman_spritesheet.png')

for i in range(4):
    hero_walk_list.append(pygame.image.load(f'assets/assets/hero_walk_0{i+1}.png'))

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Animation')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run_animation = True

    clock.tick(60)
    dt = clock.get_time()

    run_animation = False

    anim_time = anim_time + dt
    anim_time_sec = anim_time/1000

    if anim_time_sec > 0.15:
        curr_frame = curr_frame + 1
        if curr_frame > len(hero_walk_list) - 1:
            curr_frame = 0
        anim_time = 0

    anim_time_mm = anim_time_mm + dt
    anim_time_mm_sec = anim_time_mm/1000    

    if run_animation:
        anim_time_mm = anim_time_mm + dt
        anim_time_mm_sec + anim_time_mm/1000
        if anim_time_mm_sec > 0.1:
            curr_frame_mm = curr_frame_mm + 1
        if curr_frame_mm > len(hero_walk_list) - 1:
            curr_frame_mm = 0
        anim_time_mm = 0



    screen.fill((255,255,255))

    screen.blit(hero_walk_list[curr_frame], (0, 0))

    screen.blit(megaman_spritesheet, (200,200), (60 * (curr_frame_mm%5), 60 * (curr_frame_mm//5), 60, 60))

    pygame.display.update()


