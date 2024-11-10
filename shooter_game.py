import pygame
from random import*
miss = 0
def game():
    global miss 
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('fire.ogg')
    pygame.mixer.music.play()

    window = pygame.display.set_mode((700,500))
    fps = pygame.time.Clock()

    fon = pygame.image.load('galaxy.jpg')
    fon = pygame.transform.scale(fon, (700,500))

    class GameObject(pygame.sprite.Sprite):
        def __init__(self, image, visota, shirina, x,y, speed):
            super().__init__()
            self.img_sprite = pygame.image.load(image)
            self.img_sprite = pygame.transform.scale(self.img_sprite, (visota, shirina))
            self.rect = self.img_sprite.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = speed
            self.move = ""
        def show(self):
            window.blit(self.img_sprite, self.rect)

    class GamePlayer(GameObject):
        def ypravlenie(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d] and self.rect.x < 650:
                self.rect.x += self.speed
            if keys[pygame.K_a] and self.rect.x > 0:
                self.rect.x -= self.speed

        def vistrel(self):
            puly = Puly('bullet.png', 15, 20, self.rect.x, self.rect.y, 10)
            pulys.add(puly)

    class Enemy(GameObject):
        def forward(self):
            global miss
            self.rect.y += 2
            if self.rect.y > 400:
                self.rect.y = randint(-40,0)
                miss += 1
            

            
                

    class Puly(GameObject):
        def update(self):
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.kill()

    pulys = pygame.sprite.Group()


    monsters = pygame.sprite.Group()
    for i in range(5):
        monster = Enemy('ufo.png', 60, 60, randint(50, 600), randint(-10, 10), 5)
        monsters.add(monster)


    player = GamePlayer('rocket.png', 60,60, 20, 430, 10)

    run = True
    score = 0
    miss = 0

    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    player.vistrel()
        window.blit(fon, (0,0))
        player.show()
        player.ypravlenie()

        for i in pulys:
            i.show()
            i.update()

        result = f'Вы уничтожили: {str(score)}'
        bed = pygame.font.Font(None, 35).render(result, True, (255, 255, 255))
        window.blit(bed,(50, 40))

        result1 = f'Вы пропустили: {str(miss)}'
        bed1 = pygame.font.Font(None, 35).render(result1, True, (255, 255, 255))
        window.blit(bed1, (300, 40))
        if miss ==15:
            run = False


        kill = pygame.sprite.groupcollide(pulys, monsters, True, True)

        for i in kill:
            score += 1
            monster = Enemy('ufo.png', 60, 60, randint(50, 600), randint(-10, 10), 5)
            monsters.add(monster)


        for i in monsters:
            i.show()
            i.forward()

        

            if player.rect.colliderect(i.rect):
                run = False


        pygame.display.update()
        fps.tick(60)

