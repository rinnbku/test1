import pygame 
import shooter_game
pygame.init()

back = (125, 0, 255)

window = pygame.display.set_mode((800, 500))
window.fill(back)

fps = pygame.time.Clock()

button_rect = pygame.Rect(200, 200, 200, 50)
button_exit = pygame.Rect(200, 270, 200, 50)

bed = pygame.font.Font(None, 35).render("Начать игру", True, (255, 255, 255))
exit_b = pygame.font.Font(None, 35).render("выход", True, (255, 255, 255))


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                shooter_game.game()
                pygame.quit()

            elif button_exit.collidepoint(event.pos):
                running = False
                pygame.quit()
    
    pygame.draw.rect(window, (22, 66, 168), button_rect)
    pygame.draw.rect(window, (22, 66, 168), button_exit)

    window.blit(bed, (225, 210))
    window.blit(exit_b, (250, 280))

    pygame.display.update()
    fps.tick(120)