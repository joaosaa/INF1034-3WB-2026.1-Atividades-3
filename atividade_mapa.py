import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

tileset_raw = pygame.image.load('terrain.png').convert_alpha()

tile_topo  = pygame.Surface((16, 16), pygame.SRCALPHA)
tile_topo.blit(tileset_raw, (0, 0), (7 * 16, 0 * 16, 16, 16))
tile_topo = pygame.transform.scale(tile_topo, (48, 48))

tile_terra = pygame.Surface((16, 16), pygame.SRCALPHA)
tile_terra.blit(tileset_raw, (0, 0), (7 * 16, 1 * 16, 16, 16))
tile_terra = pygame.transform.scale(tile_terra, (48, 48))

tile_caixa = pygame.Surface((16, 16), pygame.SRCALPHA)
tile_caixa.blit(tileset_raw, (0, 0), (12 * 16, 1 * 16, 16, 16))
tile_caixa = pygame.transform.scale(tile_caixa, (48, 48))

MAPA = [
    "CCCCCCCCCCCCCCCCC",
    "CCCCCCCCCCCCCCCCC",
    "CCCCCCCCCCCCCCCCC",
    "CCCCCCCCCCCCCCCCC",
    "CCCCCCCCCCCCCCCCC",
    "CCCCBBBCCCCCCCCCC",
    "CCCCCCCCCCCCCCCCC",
    "CCCCCCCCCBCCCCCCC",
    "RRRRRRRR_GRRRRRRR",
    "DDDDDDDD_DDDDDDDD",
]

collider_list = []
for i in range(len(MAPA)):
    for j in range(len(MAPA[i])):
        if MAPA[i][j] == "R" or MAPA[i][j] == "B":
            collider_list.append(pygame.Rect(j * 48, 120 + i * 48, 48, 48))

mario_raw = pygame.image.load('mario_spritesheet.png').convert()
mario_raw.set_colorkey((0, 0, 0))

mario_frames_right = []
mario_frames_left  = []
for i in range(3):
    frame = pygame.Surface((168, 233))
    frame.set_colorkey((0, 0, 0))
    frame.blit(mario_raw, (0, 0), (i * 168, 0, 168, 233))
    frame = pygame.transform.scale(frame, (48, 67))
    mario_frames_right.append(frame)
    mario_frames_left.append(pygame.transform.flip(frame, True, False))

mario_x      = 100.0
mario_y      = 437.0
velocidade_y     = 0.0
no_chao    = False
virado_direita = True

curr_frame_mario = 0
anim_time_mario  = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()
    keys = pygame.key.get_pressed()

    movendo = False
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        mario_x += 5
        virado_direita = True
        movendo = True
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        mario_x -= 5
        virado_direita = False
        movendo = True

    collider_mario = pygame.Rect(int(mario_x), int(mario_y), 48, 67)
    for col in collider_list:
        if collider_mario.colliderect(col):
            if virado_direita:
                mario_x = col.left - 48
            else:
                mario_x = col.right
            collider_mario = pygame.Rect(int(mario_x), int(mario_y), 48, 67)

    if keys[pygame.K_w] and no_chao:
        velocidade_y = -13
        no_chao = False

    velocidade_y += 0.6
    mario_y  += velocidade_y

    no_chao = False
    collider_mario = pygame.Rect(int(mario_x), int(mario_y), 48, 67)
    for col in collider_list:
        if collider_mario.colliderect(col):
            if velocidade_y > 0:
                mario_y   = col.top - 67
                velocidade_y  = 0
                no_chao = True
            elif velocidade_y < 0:
                mario_y  = col.bottom
                velocidade_y = 0
            collider_mario = pygame.Rect(int(mario_x), int(mario_y), 48, 67)

    if mario_x < 0: mario_x = 0
    if mario_x + 48 > 800: mario_x = 800 - 48

    if movendo:
        anim_time_mario += dt
        if anim_time_mario > 150:
            curr_frame_mario = (curr_frame_mario + 1) % 3
            anim_time_mario  = 0
    else:
        curr_frame_mario = 0
        anim_time_mario  = 0

    screen.fill((107, 140, 255))

    for i in range(len(MAPA)):
        for j in range(len(MAPA[i])):
            if MAPA[i][j] == "R" or MAPA[i][j] == "G":
                screen.blit(tile_topo, (j * 48, 120 + i * 48))
            elif MAPA[i][j] == "D":
                screen.blit(tile_terra, (j * 48, 120 + i * 48))
            elif MAPA[i][j] == "B":
                screen.blit(tile_caixa, (j * 48, 120 + i * 48))

    frames = mario_frames_right if virado_direita else mario_frames_left
    screen.blit(frames[curr_frame_mario], (int(mario_x), int(mario_y)))

    pygame.display.update()