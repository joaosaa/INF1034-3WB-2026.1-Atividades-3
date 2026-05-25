import pygame, random, sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
fonte = pygame.font.SysFont("arial", 13)
clock = pygame.time.Clock()

lista = [10, 22, 35, 47, 58, 63, 71, 82, 90, 95,
         12, 25, 38, 44, 55, 67, 73, 84, 91, 97,
         15, 28, 33, 49, 52, 66, 78, 86, 93, 99,
         11, 24, 36, 48, 57, 64, 72, 83, 92, 96,
         14, 27, 39, 46, 53, 68, 75, 87, 94, 98,]
random.shuffle(lista)
lista = lista[:random.randint(30, 50)]

num_faixas = 4
minimo = min(lista)
maximo = max(lista)
tamanho_faixa = (maximo - minimo) / num_faixas

faixas = []
for i in range(num_faixas):
    ini = minimo + i * tamanho_faixa
    fim = ini + tamanho_faixa
    contagem = 0
    for v in lista:
        if i < num_faixas - 1:
            if ini <= v < fim:
                contagem += 1
        else:
            if ini <= v <= fim:
                contagem += 1
    faixas.append((ini, fim, contagem))

cores = [(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)) for _ in range(num_faixas)]

while True:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill((30, 30, 30))

    maior = max(f[2] for f in faixas)
    bw = 130
    base_y = 520

    pygame.draw.line(tela, (200, 200, 200), (60, 60), (60, base_y), 2)
    pygame.draw.line(tela, (200, 200, 200), (60, base_y), (700, base_y), 2)

    for i in range(6):
        y = base_y - int(i / 5 * 420)
        val = int(i / 5 * maior)
        lbl = fonte.render(str(val), True, (180, 180, 180))
        tela.blit(lbl, (10, y - 7))

    for i, (ini, fim, cnt) in enumerate(faixas):
        bx = 80 + i * (bw + 10)
        altura = int((cnt / maior) * 420)
        by = base_y - altura
        pygame.draw.rect(tela, cores[i], (bx, by, bw, altura))
        lbl = fonte.render(f"{ini:.0f}", True, (200, 200, 200))
        tela.blit(lbl, (bx, base_y + 5))

    pygame.display.flip()
