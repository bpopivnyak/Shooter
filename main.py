import pygame
import rocket
import ufo
import asteroid

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
Asteroid = []
Ufo.append(ufo.Enemy(50, 50, 70, 80, 10, "ufo.png"))
Asteroid.append(asteroid.Enemy(150, 50, 70, 80, 10, "asteroid.png"))
Ufo.append(ufo.Enemy(250, 50, 70, 80, 10, "ufo.png"))
Asteroid.append(asteroid.Enemy(370, 50, 70, 80, 10, "asteroid.png"))
Ufo.append(ufo.Enemy(470, 50, 70, 80, 10, "ufo.png"))
Asteroid.append(asteroid.Enemy(590, 50, 70, 80, 10, "asteroid.png"))
Ufo.append(ufo.Enemy(690, 50, 70, 80, 10, "ufo.png"))
Asteroid.append(asteroid.Enemy(810, 50, 70, 80, 10, "asteroid.png"))
Ufo.append(ufo.Enemy(910, 50, 70, 80, 10, "ufo.png"))
Asteroid.append(asteroid.Enemy(1030, 50, 70, 80, 10, "asteroid.png"))
Ufo.append(ufo.Enemy(1130, 50, 70, 80, 10, "ufo.png"))
Asteroid.append(asteroid.Enemy(1250, 50, 70, 80, 10, "asteroid.png"))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()


    Rocket.move()
    for ufo in Ufo:
        ufo.move()
    for asteroid in Asteroid:
        asteroid.move()

    window.fill((123,123,123))
    window.blit(backgroundImage, (0, 0))
    Rocket.render((window))
    for ufo in Ufo:
        ufo.render(window)
    for asteroid in Asteroid:
        asteroid.render(window)
    pygame.display.flip()
    fps.tick(60)