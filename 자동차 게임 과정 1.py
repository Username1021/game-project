import pygame

pygame.init()

black=(000,000,051)
size=[600,900]
screen=pygame.display.set_mode(size)

done=False
clock=pygame.time.Clock()

car=pygame.image.load('images/그냥 네모.jpg')
car=pygame.transform.scale(car,(100,100))

def rungame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(balck)
        pygame.display

