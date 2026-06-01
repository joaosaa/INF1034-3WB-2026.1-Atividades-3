import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Animation')

clock = pygame.time.Clock()

#imagens
hero_walk_list = []
boneco_list = []

mario_raw = pygame.image.load('mario_spritesheet.png').convert()
mario_raw.set_colorkey((0, 0, 0))
mario_frames = []
for i in range(3):
    frame = pygame.Surface((168, 233))
    frame.set_colorkey((0, 0, 0))
    frame.blit(mario_raw, (0, 0), (i * 168, 0, 168, 233))
    frame = pygame.transform.scale(frame, (120, 150))
    mario_frames.append(frame)

for i in range(8):
    hero_walk_list.append(pygame.image.load(f'assets/Hero_Walk_0{i+1}.png'))

for i in range(9):
    img = pygame.image.load(f'assets2/boneco_walk{i+1}.png')
    img = pygame.transform.scale(img, (130, 150))
    boneco_list.append(img)

#animações
curr_frame = 0
anim_time = 0

curr_frame_boneco = 0
anim_time_boneco = 0

curr_frame_mario = 0
anim_time_mario = 0

mario_x = 500
mario_y = 230

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    anim_time = anim_time + dt
    anim_time_sec = anim_time / 1000
    if anim_time_sec > 0.15:
        curr_frame = curr_frame + 1
        if curr_frame > len(hero_walk_list) - 1:
            curr_frame = 0
        anim_time = 0

    anim_time_boneco_sec = anim_time_boneco / 1000
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        anim_time_boneco = anim_time_boneco + dt
        anim_time_boneco_sec = anim_time_boneco / 1000
        if anim_time_boneco_sec > 0.1:
            curr_frame_boneco = curr_frame_boneco + 1
            if curr_frame_boneco > len(boneco_list) - 1:
                curr_frame_boneco = 0
            anim_time_boneco = 0

    if keys[pygame.K_d]:
        mario_x = mario_x + 5
        anim_time_mario = anim_time_mario + dt
        anim_time_mario_sec = anim_time_mario / 1000
        if anim_time_mario_sec > 0.15:
            curr_frame_mario = curr_frame_mario + 1
            if curr_frame_mario > 2:
                curr_frame_mario = 0
            anim_time_mario = 0
        if mario_x > 800:
            mario_x = 450

    screen.fill((255, 255, 255))

    screen.blit(hero_walk_list[curr_frame], (130, 230))
    screen.blit(boneco_list[curr_frame_boneco], (330, 230))
    screen.blit(mario_frames[curr_frame_mario], (mario_x, mario_y))

    pygame.display.update()