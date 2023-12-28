import pygame

import rocket

pygame.init()
window = pygame.display.set_mode((1370, 705))
fps = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)

backgroundImage = pygame.image.load("galaxy.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (1370, 705))


Rocket = rocket.Character(600, 598, 70, 100, 10, "rocket.png")
Ufo = []
Ufo.append(ufo.Enemy(50, 50, 70, 80, 10, "ufo.png"))


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()


    Rocket.move()
    ufo.move()

    window.fill((123,123,123))
    window.blit(backgroundImage, (0, 0))
    Rocket.render((window))
    for ufo in Ufo:
        ufo.Render(window)
    pygame.display.flip()
    fps.tick(60)