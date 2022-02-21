import pygame

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
# Pour la création d'un fichier de réglage (FPS)
FPS = 144

getResolution = pygame.display.Info()
screen = pygame.display.set_mode((getResolution.current_w, getResolution.current_h))

pygame.display.set_caption("Pas Encore De Nom ^^")

font = pygame.font.SysFont("Arial", 18)


# pygame.display.set_mode((3840, 2160))

def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text


# UTILISER CETTE BOUCLE !!!!

running = True
while running:

    clock.tick(FPS)
    screen.fill((0, 0, 0))
    screen.blit(update_fps(), (10, 0))
    print(clock.get_fps())
    if 59 >= clock.get_fps():
        print("Fréquence d'image faible")

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Jeu quitté")


