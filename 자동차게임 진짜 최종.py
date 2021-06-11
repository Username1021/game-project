import pygame
import random
import os
line=[40,260,520,760,1000]
pygame.init()


BLACK = (0, 0, 0)
size = [1160, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

def runGame():
    bomb_image = pygame.image.load('images/bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (120, 200))
    bombs = []
    배경=pygame.image.load('images/도로.png')
    배경=pygame.transform.scale(배경,(1160,800))

    for i in range(5):
        rect = pygame.Rect(bomb_image.get_rect())
        rect.left = random.choice(line)
        rect.top = -100
        dy = random.randint(9, 18)
        bombs.append({'rect': rect, 'dy': dy})

    person_image = pygame.image.load('images/person.png')
    person_image = pygame.transform.scale(person_image, (120, 200))
    person = pygame.Rect(person_image.get_rect())
    person.left = size[0] // 2 - person.width // 2
    person.top = size[1] - person.height
    person_dx = 0
    person_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_dx = -30
                elif event.key == pygame.K_RIGHT:
                    person_dx = 30
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_dx = 0
                elif event.key == pygame.K_RIGHT:
                    person_dx = 0

        for bomb in bombs:
            bomb['rect'].top += bomb['dy']
            if bomb['rect'].top > size[1]:
                bombs.remove(bomb)
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.choice(line)
                rect.top = -100
                dy = random.randint(9, 18)
                bombs.append({'rect': rect, 'dy': dy})

        person.left = person.left + person_dx
        screen.blit(배경,(0,0))
        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width

        screen.blit(person_image, person)


        for bomb in bombs:
            if bomb['rect'].colliderect(person):
                done = True
            screen.blit(bomb_image, bomb['rect'])

        pygame.display.update()


runGame()
pygame.quit()
