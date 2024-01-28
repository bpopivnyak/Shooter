import pygame

from bullet import Bullet


class Character:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.bullets = []


    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))
        for bullet in self.bullets:
            bullet.move()
            bullet.render(window)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
            is_step = True
        if keys[pygame.K_s]:
            self.hit_box.y += self.speed
            is_step = True
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed
            is_step = True
        if keys[pygame.K_w]:
            self.hit_box.y -= self.speed
        if keys[pygame.K_RIGHT]:
            self.hit_box.x += self.speed
            is_step = True
        if keys[pygame.K_DOWN]:
            self.hit_box.y += self.speed
            is_step = True
        if keys[pygame.K_LEFT]:
            self.hit_box.x -= self.speed
            is_step = True
        if keys[pygame.K_UP]:
            self.hit_box.y -= self.speed
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.hit_box.x, self.hit_box.y, 20, 20, 5, "bullet.png"))